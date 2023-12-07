import pygame as pg
from config import *

class Plataforma(pg.sprite.Sprite):
    def __init__(self, path_imagen, x, y, ancho, alto):
        super().__init__()

        self.image = pg.image.load(path_imagen)
        self.image = pg.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect(topleft=(x, y))
        #self.rect = pg.Rect(x, y, ancho, alto)
        

    # def ger_rect(self):
    #     return self.rect
    
    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)

    def debugger_plataformas(self, pantalla):
        pg.draw.rect(pantalla, (VERDE), self.rect, 3)
