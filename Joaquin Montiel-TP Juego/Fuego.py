import pygame

class Fuego(pygame.sprite.Sprite):
    def __init__(self, path_imagen, tamaño):
        super().__init__()

        self.fuego = pygame.transform.scale(pygame.image.load(path_imagen), tamaño)
        self.image = self.fuego
        self.rect = self.image.get_rect()
        self.velocidad_x = 0
        self.velocidad_y = 0

    def update(self):
        # Actualizar las coordenadas del rectángulo por asignación directa
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y