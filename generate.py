from os import getcwd
from os.path import exists
from pathlib import Path
import shutil
import zipfile
import argparse
import json

# parse arguments

parser = argparse.ArgumentParser(description="Generate templated datapack.")

parser.add_argument(
    "--namespace",
    "-n",
    dest="namespace",
    help="the custom namespace to use",
    default="kaituo",
)
parser.add_argument(
    "--templates",
    "-t",
    dest="template_folder",
    help="template folder",
    default="templates",
)
parser.add_argument(
    "--out", "-o", dest="output_folder", help="output folder", default="out"
)
parser.add_argument(
    "--pack-format",
    "-f",
    type=int,
    dest="pack_format",
    help="pack format number",
    default=15,
)
parser.add_argument(
    "--output-zip-name",
    "-z",
    dest="output_zip_name",
    help="output zip name",
    default="kaituo.zip",
)
parser.add_argument(
    "--verbose", "-v", dest="verbose", action="store_true", help="show verbose output"
)
parser.add_argument(
    "--no-cleanup",
    "-c",
    dest="cleanup",
    action="store_false",
    help="stop clean up output folder after generating",
)

args = parser.parse_args()

# record the files
FILES: list[Path] = []
CWD = getcwd()

# make directories

out_path = Path(args.output_folder)
out_path.mkdir(exist_ok=True)

data_path = out_path / "data"
data_path.mkdir(exist_ok=True)

namespace_path = data_path / str(args.namespace)
namespace_path.mkdir(exist_ok=True)

categories = [
    "function",
    "structure",
    "tags",
    "advancement",
    "item_modifier",
    "loot_table",
    "number_provider",
    "predicate",
    "recipe",
    "slot_source",
]
for category in categories:
    path = namespace_path / category
    if path.exists():
        shutil.rmtree(path)

# generate pack.mcmeta

pack_meta_path = out_path / "pack.mcmeta"
with open(pack_meta_path, "w") as f:
    json.dump(
        {
            "pack": {
                "description": "Kaituo datapack",
                "min_format": args.pack_format,
                "max_format": args.pack_format,
            }
        },
        f,
        indent=2,
    )
FILES.append(pack_meta_path)
if args.verbose:
    print(f"[{__file__}] generated pack.mcmeta")

# generate from templates

templates_path = Path(args.template_folder).absolute()


def get_suffix(category: str) -> str:
    match category:
        case "function":
            return ".mcfunction"
        case "structure":
            return ".nbt"
        case _:
            return ".json"


def write_file(src: Path, content: str | None = None):
    dest = namespace_path / src.relative_to(templates_path)
    if not dest.parent.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
    if content:
        dest.write_text(content, encoding="utf-8")
    else:
        dest.write_bytes(src.read_bytes())
    FILES.append(dest)
    if args.verbose:
        print(f"[{__file__}] generated {dest.relative_to(data_path)}")


def do_templates(dir_path: Path, category: str):
    enum_json = (dir_path / "enum.json").read_text(encoding="utf-8")
    enum = json.loads(enum_json)
    for subdir_path, _, filenames in dir_path.walk():
        for filename in filenames:
            file_path = subdir_path / filename
            if file_path.suffix != get_suffix(category):
                continue
            if filename == "enum.json":
                continue
            for entry in enum:
                content = file_path.read_text(encoding="utf-8")
                content = content.replace("$$", entry)
                new_file_path = Path(str(file_path).replace("$$", entry))
                write_file(new_file_path, content)


for category in categories:
    category_path = templates_path / category
    if not category_path.exists():
        continue

    for dir_path, subdir_names, filenames in category_path.walk():
        for subdir_name in subdir_names.copy():
            subdir_path = dir_path / subdir_name
            if (subdir_path / "enum.json").exists():
                subdir_names.remove(subdir_name)
                do_templates(subdir_path, category)
        for filename in filenames:
            file_path = dir_path / filename
            if file_path.suffix == get_suffix(category):
                write_file(file_path)

# pack files into a zip

out_zip_path = out_path / args.output_zip_name
outzip = zipfile.ZipFile(out_zip_path, "w")
for file in FILES:
    outzip.write(file, file.absolute().relative_to(out_path.absolute()))
outzip.close()

# clean up

if args.cleanup:
    shutil.rmtree(data_path)
    pack_meta_path.unlink()
