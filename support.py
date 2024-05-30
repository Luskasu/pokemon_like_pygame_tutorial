from settings import *
from os.path import join
from os import walk
from pytmx.util_pygame import load_pygame

#imports
def importFolder(*path):
    frames = []
    for folder_paths, sub_folders, image_names in walk(join(*path)):
        for image_name in sorted(image_names, key=lambda name: int(name.split('.')[0])):
            