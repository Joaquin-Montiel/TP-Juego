import pygame as pg

class Vida(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load(r'./sprites_juego\vida\vida.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)

    def update(self):
        pass
