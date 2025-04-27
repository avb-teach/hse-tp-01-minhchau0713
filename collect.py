import shutil
import os
from pathlib import Path
import sys

def collect(input_dir, output_dir):
    output_path = Path(output_dir) # https://docs.python.org/3/library/pathlib.html
    list_names = {}
    for root, _, files in os.walk(input_dir): # https://pythoner.name/walk
        for filename in files:
            src_path = Path(root) / filename
            dest_name = filename
            if dest_name in list_names:
                list_names[dest_name] += 1
                name, ext = os.path.splitext(filename) # https://pythonworld.ru/moduli/modul-os-path.html
                dest_name = f"{name}{list_names[dest_name]}{ext}"
            else:
                list_names[filename] = 0
            dest_path = output_path / dest_name
            shutil.copy2(src_path, dest_path) # https://sky.pro/media/kak-skopirovat-fajly-v-python/


args = sys.argv[1:]
collect(args[0], args[1])
