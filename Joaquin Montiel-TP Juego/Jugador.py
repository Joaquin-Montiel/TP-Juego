import pygame
from config import *
from Fuego import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self, coordenadas, ruta_der, ruta_izq, dinosaurio_camina_der, dinosaurio_camina_izq) -> None:
        super().__init__()
        # self.nombre =  input("Ingrese el nombre de su dino")
        self.vidas = 3
        self.dinosaurio_der = pygame.image.load(ruta_der)
        self.dinosaurio_izq = pygame.image.load(ruta_izq)
        self.image = self.dinosaurio_der
        self.rect = self.image.get_rect()
        self.piso = HEIGTH
        self.rect.midbottom = coordenadas
        self.dinosaurio_camina_der = dinosaurio_camina_der
        self.dinosaurio_camina_izq = dinosaurio_camina_izq
        self.indice_sprite = 0  # Nuevo atributo para rastrear el índice del sprite actual
        self.en_el_aire = False
        self.velocidad_salto = -10 # Ajusta según sea necesario
        self.gravedad = 1  # Ajusta según sea necesario
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.fuego_cooldown = 0  # Tiempo de espera entre disparos
        self.fuego_cooldown_max = 30  # Máximo tiempo de espera entre disparos

    def mover_der(self, pixeles):
        self.rect.x += pixeles
        self.image = self.dinosaurio_camina_der[self.indice_sprite]
        self.indice_sprite = (self.indice_sprite + 1) % len(self.dinosaurio_camina_der)

    def mover_izq(self, pixeles):
        self.rect.x -= pixeles
        self.image = self.dinosaurio_camina_izq[self.indice_sprite]
        self.indice_sprite = (self.indice_sprite + 1) % len(self.dinosaurio_camina_izq)

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

    def saltar(self):
        if not self.en_el_aire:
            self.velocidad_y = self.velocidad_salto
            self.en_el_aire = True

    def aplicar_gravedad(self):
        if self.en_el_aire:
            self.velocidad_y += self.gravedad
            self.rect.y += self.velocidad_y

            # Controlar límite inferior (suelo)
            self.rect.y = min(self.rect.y, self.piso)

            if self.rect.y == self.piso:
                self.en_el_aire = False
                self.velocidad_y = 0


    def disparar_fuego(self, sprites_grupo):
        if self.fuego_cooldown <= 0:
            nuevo_fuego = Fuego(RUTA_FUEGO, TAMAÑO_FUEGO)
            nuevo_fuego.rect.x = self.rect.x + self.rect.width if self.velocidad_x > 0 else self.rect.x - nuevo_fuego.rect.width
            nuevo_fuego.rect.y = self.rect.y + self.rect.height // 2 - nuevo_fuego.rect.height // 2
    
            sprites_grupo.add(nuevo_fuego)
            self.fuego_cooldown = 0  # Es

    def actualizar_fuego_cooldown(self):
        # Actualizar el tiempo de espera entre disparos
        if self.fuego_cooldown > 0:
            self.fuego_cooldown -= 1
