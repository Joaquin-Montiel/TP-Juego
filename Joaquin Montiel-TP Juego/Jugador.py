import pygame as pg
from config import *
from Fuego import Defensa
from Vida import Vida

class Jugador(pg.sprite.Sprite):
    def __init__(self, coordenadas, ruta_der, ruta_izq, dinosaurio_camina_der, dinosaurio_camina_izq) -> None:
        super().__init__()
        # self.nombre =  input("Ingrese el nombre de su dino")
        self.vidas = 3
        self.energia = 100
        self.dinosaurio_der = pg.image.load(ruta_der)
        self.dinosaurio_izq = pg.image.load(ruta_izq)
        self.dinosaurio_camina_der = dinosaurio_camina_der
        self.dinosaurio_camina_izq = dinosaurio_camina_izq
        self.image = self.dinosaurio_der
        self.rect = self.image.get_rect()
        self.rect.midbottom = coordenadas
        self.piso = HEIGTH
        self.indice_sprite = 0  # Atributo para rastrear el índice del sprite actual
        self.en_el_aire = False
        self.velocidad_salto = -10 
        self.gravedad = 1  
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.direccion = "derecha"
        self.defensa_cooldown = 0  # Tiempo de espera entre disparos
        self.defensa_cooldown_max = 10  # Máximo tiempo de espera entre disparos
        self.trampas_colisionadas = 0
        self.max_colisiones_trampa = 5
        self.energias_recolectadas = 0

    def mover_der(self, pixeles):
        self.rect.x += pixeles
        self.direccion = "derecha"
        self.image = self.dinosaurio_camina_der[self.indice_sprite]
        self.indice_sprite = (self.indice_sprite + 1) % len(self.dinosaurio_camina_der)

    def mover_izq(self, pixeles):
        self.rect.x -= pixeles
        self.direccion = "izquierda"
        self.image = self.dinosaurio_camina_izq[self.indice_sprite]
        self.indice_sprite = (self.indice_sprite + 1) % len(self.dinosaurio_camina_izq)

    # def colocar_vidas(self, g_sprites):
    #     vidas = pg.sprite.Group()
    #     for i in range(self.vidas):
    #         x = (WIDTH -(20 * self.vidas)) // 2 + i * 30
    #         y = 25
    #         vida = Vida(x, y)
    #         vida.jugador
    #         vidas.add(vida)

    #     vidas.update(self.vidas)
    #     g_sprites.add(vidas)

    def colisionar_trampa(self):
        self.trampas_colisionadas += 1
        self.energia -= 20
        if self.trampas_colisionadas % self.max_colisiones_trampa == 0:
            if self.energia == 0:
                # Cuando el jugador se queda sin energía después de colisionar con trampas
                self.vidas -= 1
                self.energia = 100  # Reiniciar la energía

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        self.aplicar_gravedad()

    def aplicar_gravedad(self):
        if self.en_el_aire:
            self.rect.y += self.velocidad_y
            self.velocidad_y += self.gravedad

            # Controlar límite inferior (suelo)
            if self.rect.y >= self.piso:
                self.rect.y = self.piso
                self.en_el_aire = False
                self.velocidad_y = 0
        
    def saltar(self):
        if not self.en_el_aire:
            self.velocidad_y = self.velocidad_salto
            self.en_el_aire = True

    def disparar(self, g_sprites, g_disparo):
        if self.defensa_cooldown <= 0:
            direccion = self.direccion
            disparo = Defensa(self.rect.centerx, self.rect.centery, direccion)
            g_sprites.add(disparo)
            g_disparo.add(disparo)
            self.defensa_cooldown = self.defensa_cooldown_max

    def actualizar_defensa(self):
        # Actualizar el tiempo de espera entre disparos
        if self.defensa_cooldown > 0:
            self.defensa_cooldown -= 1

    def perder_vida(self):
        self.vidas -= 1
        if self.vidas <= 0:
            print("GAME OVER")

    def perder_energia(self, cantidad):
        self.energia -= cantidad
        if self.energia <= 0:
            # Acciones cuando el jugador se queda sin energía (por ejemplo, mostrar game over)
            self.vidas -= 1
            self.energia = 100  # Reiniciar la energía

    def colisionar_enemigo(self):
        # Llamar a este método cuando haya colisión con un enemigo
        self.perder_vida()

    def colisionar_trampa(self):
        # Llamar a este método cada vez que haya colisión con una trampa
        self.trampas_colisionadas += 1
        self.energia -= 20
        if self.energia == 0:
            # Acciones cuando el jugador se queda sin energía después de colisionar con trampas
            self.perder_vida()
            self.energia = 100  # Reiniciar la energía
