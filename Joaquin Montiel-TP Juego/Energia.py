import pygame as pg

class Energia(pg.sprite.Sprite):
    def __init__(self, image_path, x, y, ancho, alto):
        super().__init__()
        self.rect = pg.Rect(x, y, ancho, alto)
        self.image = pg.image.load(image_path).convert_alpha()
        self.image = pg.transform.scale(self.image, (ancho, alto))  # Escalamos la imagen según el tamaño proporcionado
        self.puntaje = 20
    def get_rect(self):
        return self.rect

    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)