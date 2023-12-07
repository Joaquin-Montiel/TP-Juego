import pygame as pg
from config import *

class Defensa(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direccion:str):
        super().__init__()

        self.fuego_der = pg.image.load(r'./sprites_juego\Defensa\llama_der.png')
        self.fuego_izq = pg.image.load(r'./sprites_juego\Defensa\llama_izq.png')
        self.image = self.fuego_der if direccion == "derecha" else self.fuego_izq
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.rect.centerx = pos_x
        self.rect.centery = pos_y
        self.direccion = direccion

    def update(self):
        if self.direccion == "derecha":
            self.rect.x += 10
        elif self.direccion == "izquierda":
            self.rect.x -= 10

        if self.rect.right > ANCHO or self.rect.left < 0:
            self.kill()