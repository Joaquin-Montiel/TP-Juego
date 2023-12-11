import pygame, random
from config import *

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, path_imagen, center:tuple, velocidad:int=3):
        super().__init__()

        self.asteroide = pygame.image.load(path_imagen).convert_alpha()
        self.image = self.asteroide
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.velocidad = velocidad
        self.aceleracion = 1.2
        self.puntaje = 50

    def update(self):
        self.aceleracion += 0.1
        self.rect.y += self.velocidad * self.aceleracion

        #Verifico si la trampa está fuera de la pantalla
        if self.rect.top >= ALTO:
            self.kill()

    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)

def generar_trampas(g_sprites, g_trampas, pantalla: pygame.Surface, cantidad: int=8):
    if len(g_trampas) == 0:
        for i in range(cantidad):
            x = random.randint(40, pantalla.get_width() - 40)
            y = random.randint(40, pantalla.get_height() // 2)
            trampa = Asteroide(RUTA_TRAMPA, (x, y), VELOCIDAD_ASTEROIDE)
            g_sprites.add(trampa)
            g_trampas.add(trampa)

