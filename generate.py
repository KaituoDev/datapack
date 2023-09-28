import os
import zipfile

# preparations

WOOD_TYPES = [    # all wood types in 1.20
    'oak',
    'spruce',
    'birch',
    'jungle',
    'acacia',
    'dark_oak',
    'crimson',
    'warped',
    'mangrove',
    'cherry',
    'bamboo'
]

PACK_FORMAT = 15    # 1.20.1

FILES = []

# generate pack.mcmeta

with open('pack.mcmeta', 'w', encoding='utf-8') as f:
    f.write( '{\n')
    f.write( '    "pack": {\n')
    f.write(f'        "pack_format": {PACK_FORMAT},\n')
    f.write( '        "description": "Kaituo Datapack"\n')
    f.write( '    }\n')
    f.write( '}\n')

# make directories

if not os.path.exists('data'):
    os.mkdir('data')

if not os.path.exists('data/kaituo'):
    os.mkdir('data/kaituo')

if not os.path.exists('data/kaituo/recipes'):
    os.mkdir('data/kaituo/recipes')

# generate stone cutting recipes

for woodtype in WOOD_TYPES:

    # planks -> slabs

    path = f'data/kaituo/recipes/{woodtype}_slab_cutting.json'
    FILES.append(path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write( '{\n')
        f.write( '    "type": "minecraft:stonecutting",\n')
        f.write(f'    "group": "minecraft:{woodtype}_planks_cutting",\n')
        f.write( '    "ingredient": {\n')
        f.write(f'        "item": "minecraft:{woodtype}_planks"\n')
        f.write( '    },\n')
        f.write(f'    "result": "minecraft:{woodtype}_slab",\n')
        f.write( '    "count": 2\n')
        f.write( '}\n')

    # planks -> stairs

    path = f'data/kaituo/recipes/{woodtype}_stairs_cutting.json'
    FILES.append(path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write( '{\n')
        f.write( '    "type": "minecraft:stonecutting",\n')
        f.write(f'    "group": "minecraft:{woodtype}_planks_cutting",\n')
        f.write( '    "ingredient": {\n')
        f.write(f'        "item": "minecraft:{woodtype}_planks"\n')
        f.write( '    },\n')
        f.write(f'    "result": "minecraft:{woodtype}_stairs",\n')
        f.write( '    "count": 1\n')
        f.write( '}\n')

# generate crafting recipes

# shaped

# logs -> chest

path = 'data/kaituo/recipes/chest_from_logs.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "lll",\n')
    f.write('        "l l",\n')
    f.write('        "lll"\n')
    f.write('    ],\n')
    f.write('    "key": {\n')
    f.write('        "l": {"tag": "minecraft:logs"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:chest",\n')
    f.write('        "count": 8\n')
    f.write('    }\n')
    f.write('}\n')

# dupe elytra

path = 'data/kaituo/recipes/elytra_duplication.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "pcp",\n')
    f.write('        "pep",\n')
    f.write('        "psp"\n')
    f.write('    ],')
    f.write('    "key": {\n')
    f.write('        "p": {"item": "minecraft:phantom_membrane"},\n')
    f.write('        "c": {"item": "minecraft:chorus_fruit"},\n')
    f.write('        "e": {"item": "minecraft:elytra"},\n')
    f.write('        "s": {"item": "minecraft:saddle"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:chest",\n')
    f.write('        "count": 2\n')
    f.write('    }\n')
    f.write('}\n')

# dupe shulker

path = 'data/kaituo/recipes/shulker_duplication.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "csc",\n')
    f.write('        "cfc",\n')
    f.write('        "csc"\n')
    f.write('    ],')
    f.write('    "key": {\n')
    f.write('        "c": {"item": "minecraft:chorus_fruit"},\n')
    f.write('        "f": {"item": "minecraft:chorus_flower"},\n')
    f.write('        "s": {"item": "minecraft:shulker_shell"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:shulker_shell",\n')
    f.write('        "count": 3\n')
    f.write('    }\n')
    f.write('}\n')

# wool -> sponge

path = 'data/kaituo/recipes/sponge_from_wool.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "ww",\n')
    f.write('        "ww"\n')
    f.write('    ],\n')
    f.write('    "key": {\n')
    f.write('        "w": {"item": "minecraft:white_wool"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:sponge",\n')
    f.write('        "count": 1\n')
    f.write('    }\n')
    f.write('}\n')

# rotten flesh -> crimson stems

path = 'data/kaituo/recipes/crimson_stems_from_rotten_flesh.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "ff",\n')
    f.write('        "ff"\n')
    f.write('    ],\n')
    f.write('    "key": {\n')
    f.write('        "f": {"item": "minecraft:rotten_flesh"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:crimson_stem",\n')
    f.write('        "count": 1\n')
    f.write('    }\n')
    f.write('}\n')

# bone -> warped stems

path = 'data/kaituo/recipes/warped_stems_from_bone.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "bb",\n')
    f.write('        "bb"\n')
    f.write('    ],\n')
    f.write('    "key": {\n')
    f.write('        "b": {"item": "minecraft:bone"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:warped_stem",\n')
    f.write('        "count": 1\n')
    f.write('    }\n')
    f.write('}\n')

# bone meal -> bone blocks

path = 'data/kaituo/recipes/bone_blocks_from_bone_meal.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "bbb",\n')
    f.write('        "bbb",\n')
    f.write('        "bbb"\n')
    f.write('    ],\n')
    f.write('    "key": {\n')
    f.write('        "b": {"item": "minecraft:bone_meal"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:bone_block",\n')
    f.write('        "count": 1\n')
    f.write('    }\n')
    f.write('}\n')

# enchanted golden apple

path = 'data/kaituo/recipes/enchanted_golden_apple.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "ggg",\n')
    f.write('        "gag",\n')
    f.write('        "ggg"\n')
    f.write('    ],\n')
    f.write('    "key": {\n')
    f.write('        "g": {"item": "minecraft:gold_block"},\n')
    f.write('        "a": {"item": "minecraft:apple"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:enchanted_golden_apple",\n')
    f.write('        "count": 1\n')
    f.write('    }\n')
    f.write('}\n')

# fast dispenser

path = 'data/kaituo/recipes/dispenser_fast.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "sl ",\n')
    f.write('        "sdl",\n')
    f.write('        "sl "\n')
    f.write('    ],\n')
    f.write('    "key": {\n')
    f.write('        "s": {"item": "minecraft:string"},\n')
    f.write('        "l": {"item": "minecraft:stick"},\n')
    f.write('        "d": {"item": "minecraft:dropper"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:dispenser",\n')
    f.write('        "count": 1\n')
    f.write('    }\n')
    f.write('}\n')

# fast minecarts

# chest minecart

path = 'data/kaituo/recipes/chest_minecart.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "iXi",\n')
    f.write('        "iii"\n')
    f.write('    ],\n')
    f.write('    "key": {\n')
    f.write('        "i": {"item": "minecraft:iron_ingot"},\n')
    f.write('        "X": {"item": "minecraft:chest"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:chest_minecart",\n')
    f.write('        "count": 1\n')
    f.write('    }\n')
    f.write('}\n')

# furnace minecart

path = 'data/kaituo/recipes/furnace_minecart.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "iXi",\n')
    f.write('        "iii"\n')
    f.write('    ],\n')
    f.write('    "key": {\n')
    f.write('        "i": {"item": "minecraft:iron_ingot"},\n')
    f.write('        "X": {"item": "minecraft:furnace"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:furnace_minecart",\n')
    f.write('        "count": 1\n')
    f.write('    }\n')
    f.write('}\n')

# tnt minecart

path = 'data/kaituo/recipes/tnt_minecart.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "iXi",\n')
    f.write('        "iii"\n')
    f.write('    ],\n')
    f.write('    "key": {\n')
    f.write('        "i": {"item": "minecraft:iron_ingot"},\n')
    f.write('        "X": {"item": "minecraft:tnt"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:tnt_minecart",\n')
    f.write('        "count": 1\n')
    f.write('    }\n')
    f.write('}\n')

# hopper minecart

path = 'data/kaituo/recipes/hopper_minecart.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:crafting_shaped",\n')
    f.write('    "category": "misc",\n')
    f.write('    "pattern": [\n')
    f.write('        "iXi",\n')
    f.write('        "iii"\n')
    f.write('    ],\n')
    f.write('    "key": {\n')
    f.write('        "i": {"item": "minecraft:iron_ingot"},\n')
    f.write('        "X": {"item": "minecraft:hopper"}\n')
    f.write('    },\n')
    f.write('    "result": {\n')
    f.write('        "item": "minecraft:hopper_minecart",\n')
    f.write('        "count": 1\n')
    f.write('    }\n')
    f.write('}\n')

# fast blasting deepslate cobble

path = 'data/kaituo/recipes/deepslate_blasting_deepslate_cobble_fast.json'
FILES.append(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write('{\n')
    f.write('    "type": "minecraft:blasting",\n')
    f.write('    "ingredient": {\n')
    f.write('        "item": "minecraft:cobbled_deepslate"\n')
    f.write('    },\n')
    f.write('    "result": "minecraft:deepslate",\n')
    f.write('    "experience": 0.5,\n')
    f.write('    "cookingtime": 10\n')
    f.write('}\n')

zipfile = zipfile.ZipFile('kaituo.zip', 'w')
for file in FILES:
    zipfile.write(file)
zipfile.write("pack.mcmeta")
zipfile.close()