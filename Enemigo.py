import pygame as pg
from config import *

class Enemigo(pg.sprite.Sprite):
    def __init__(self, path_imagen_der, path_imagen_izq, x, y) -> None:
        super().__init__()
        self.enemigo_der = pg.image.load(path_imagen_der)
        self.enemigo_izq = pg.image.load(path_imagen_izq)
        self.image = self.enemigo_der
        self.rect = self.image.get_rect()
        self.rect.midbottom =(x, y)
        self.velocidad_x = 2
        self.direccion = 1
        self.puntaje = 200

    def update(self):
        # Mover en la dirección actual
        self.rect.x += self.velocidad_x * self.direccion
    
        # Verificar límites de pantalla
        if self.rect.right > ANCHO - 225:
            self.direccion = -1  # Cambiar a la izquierda cuando alcanza el límite derecho
            self.image = self.enemigo_izq
        elif self.rect.left < 200:
            self.direccion = 1  # Cambiar a la derecha cuando alcanza el límite izquierdo
            self.image = self.enemigo_der

    def debugger_enemigo(self, pantalla):
        pg.draw.rect(pantalla, (ROJO), self.rect, 3)