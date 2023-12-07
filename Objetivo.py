import pygame as pg


class Huevo(pg.sprite.Sprite):
    def __init__(self, path_imagen, x, y, ancho, alto):
        super().__init__()
        self.image = pg.image.load(path_imagen).convert_alpha()
        self.image = pg.transform.scale(self.image, (ancho, alto))  # Escalamos la imagen según el tamaño proporcionado
        self.rect = pg.Rect(x, y, ancho, alto)
        self.puntaje = 300

    def get_rect(self):
        return self.rect

    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)