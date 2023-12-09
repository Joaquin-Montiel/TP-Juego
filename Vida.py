import pygame as pg

class Vida(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load(r'./sprites_juego\vida\vida.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vidas = 3

    # def restar_vida(self, cantidad):
    #     self.vidas -= cantidad

    # def sumar_vida(self, cantidad):
    #     self.vidas += cantidad

    # def retornar_vida(self, cantidad):
    #     return self.vidas 

    def update(self):
        pass
