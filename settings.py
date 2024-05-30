import pygame
from pygame.math import Vector2 as vector
from sys import exit

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
TILE_SIZE = 64
ANIMATION_SPEED = 6
BATTLE_OUTLINE_WIDTH = 4

COLORS={
    
}

WORLD_LAYERS = {
    'water' : 0,
    'bg' : 1,
    'shadow' : 2,
    'main' : 3,
    'top' : 4
}

BATTLE_POSITIONS ={}

BATTLE_LAYERS =   {}

BATTLE_CHOICES =  {}