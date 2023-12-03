import pygame as pg
from config import *
from Fuego import *

class Enemigo(pg.sprite.Sprite):
    def __init__(self, coordenadas, ruta_der, ruta_izq) -> None:
        super().__init__()
        self.enemigo_der = pg.image.load(ruta_der)
        self.enemigo_izq = pg.image.load(ruta_izq)
        self.image = self.enemigo_der
        self.rect = self.image.get_rect()
        self.rect.midbottom = coordenadas
        self.velocidad_x = 2
        self.direccion = 1
        self.puntaje = 150

    def update(self):
        # Mover en la dirección actual
        self.rect.x += self.velocidad_x * self.direccion

        # Verificar límites de pantalla
        if self.rect.right > WIDTH - 225:
            self.direccion = -1  # Cambiar a la izquierda cuando alcanza el límite derecho
            self.image = self.enemigo_izq
        elif self.rect.left < 200:
            self.direccion = 1  # Cambiar a la derecha cuando alcanza el límite izquierdo
            self.image = self.enemigo_der