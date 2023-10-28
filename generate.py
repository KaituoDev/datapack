from os import getcwd
from pathlib import Path
import shutil
import zipfile
import argparse
import json

# parse arguments

parser = argparse.ArgumentParser(description='Generate templated datapack.')

parser.add_argument('--namespace', '-n', dest='namespace', help='the custom namespace to use', default='kaituo')
parser.add_argument('--recipe_templates', '--rt', '-t', dest='recipe_template_folder', help='recipe template folder',
                    default='templates')
parser.add_argument('--out', '-o', dest='output_folder', help='output folder', default='out')
parser.add_argument('--pack-format', '-f', type=int, dest='pack_format', help='pack format number', default=15)
parser.add_argument('--output-zip-name', '-z', dest='output_zip_name', help='output zip name', default='kaituo.zip')
parser.add_argument('--verbose', '-v', dest='verbose', action='store_true', help='show verbose output')
parser.add_argument('--no-cleanup', '-c', dest='cleanup', action='store_false',
                    help='stop clean up output folder after generating')

args = parser.parse_args()

# record the files

CWD = getcwd()
# make directories

out_path = Path(args.output_folder)
out_path.mkdir(exist_ok=True)

data_path = out_path / 'data'
data_path.mkdir(exist_ok=True)

namespace_path = data_path / args.namespace
namespace_path.mkdir(exist_ok=True)

# categories = [            # for later use
#     'advancements',
#     'functions',
#     'loot_tables',
#     'predicates',
#     'recipes',
#     'item_modifers',
#     'structures',
#     'tags'
# ]
categories = ['recipes']
for category in categories:
    p = namespace_path / category
    if p.exists():
        shutil.rmtree(p)
    p.mkdir()
# generate pack.mcmeta

pack_meta_path = out_path / 'pack.mcmeta'
pack_meta_path.write_text(f"""{{
    'pack': {{
        'pack_format': {args.pack_format},
        'description': 'Kaituo Datapack'
    }}
}}
""")
FILES = [pack_meta_path.absolute().relative_to(CWD)]
if args.verbose:
    print(f'[{__file__}] generated pack.mcmeta')

# generate recipe from templates

templates_path = Path(args.recipe_template_folder).absolute()

for daf_path in templates_path.iterdir():
    if daf_path.is_file() and daf_path.suffix == '.json':
        dest = namespace_path / 'recipes' / daf_path.name
        shutil.copy(daf_path, dest)
        FILES.append(dest.absolute().relative_to(CWD))
        if args.verbose:
            print(f'[{__file__}] generated {dest.name}')
    elif daf_path.is_dir() and (daf_path / 'enum.json').exists():
        enum = daf_path.joinpath("enum.json").read_text(encoding='utf-8')
        enum = json.loads(enum)
        recipes: list[Path] = []
        for recipe in daf_path.glob("**/*"):
            if recipe.is_file() and recipe.suffix == '.json':
                if recipe.name == "enum.json":
                    continue
                recipes.append(recipe)
        for item in enum:
            for recipe in recipes:
                content = recipe.read_text(encoding='utf-8')
                content = content.replace("$$", item)
                dest = (
                        namespace_path / 'recipes' /
                        recipe.absolute().relative_to(templates_path).name.replace("$$", item)
                )
                dest.write_text(content, encoding='utf-8')
                FILES.append(dest.absolute().relative_to(CWD))
                if args.verbose:
                    print(f'[{__file__}] generated {dest.name}')

# pack files into a zip

out_zip_path = out_path / args.output_zip_name
outzip = zipfile.ZipFile(out_zip_path, 'w')
for file in FILES:
    outzip.write(file, file.absolute().relative_to(out_path.absolute()))
outzip.close()

# clean up

if args.cleanup:
    shutil.rmtree(data_path)
    pack_meta_path.unlink()
