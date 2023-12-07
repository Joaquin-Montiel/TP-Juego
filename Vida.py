import pygame as pg

class Vida(pg.sprite.Sprite):
    def __init__(self, path_imagen, x, y):
        super().__init__()
        self.image = pg.image.load(path_imagen)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
                
    def update(self):
        pass
