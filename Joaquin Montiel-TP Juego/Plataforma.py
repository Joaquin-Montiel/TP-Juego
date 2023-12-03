import pygame as pg

class Plataforma(pg.sprite.Sprite):
    def __init__(self, path_imagen, x, y, ancho, alto):
        super().__init__()

        self.rect = pg.Rect(x, y, ancho, alto)
        self.image = pg.image.load(path_imagen)
        self.image = pg.transform.scale(self.image, (ancho, alto))
        

    def ger_rect(self):
        return self.rect
    
    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)
