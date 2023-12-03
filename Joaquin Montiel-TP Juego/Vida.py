import pygame as pg

class Vida(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load(r'./sprites_juego\vida.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.jugador = None
        
    def update(self):
        pass