import pygame as pg
from config import *
from Disparo import Defensa
from Vida import Vida

class Jugador(pg.sprite.Sprite):
    def __init__(self, coordenadas, path_imagen, path_imagen_2, dinosaurio_camina_der, dinosaurio_camina_izq) -> None:
        super().__init__()
        self.vidas = 3
        self.energia = 100
        self.dinosaurio_der = pg.image.load(path_imagen).convert_alpha()
        self.dinosaurio_izq = pg.image.load(path_imagen_2).convert_alpha()
        self.dinosaurio_camina_der = dinosaurio_camina_der
        self.dinosaurio_camina_izq = dinosaurio_camina_izq
        self.image = self.dinosaurio_der
        self.rect = self.image.get_rect()
        self.rect.midbottom = coordenadas
        self.piso = ALTO
        self.indice_sprite = 0  # Atributo para rastrear el índice del sprite actual
        self.en_el_aire = False
        self.velocidad_salto = -10 
        self.gravedad = 0.5
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.direccion = "derecha"
        self.defensa_cooldown = 0  # Tiempo de espera entre disparos
        self.defensa_cooldown_max = 10  # Máximo tiempo de espera entre disparos
        self.trampas_colisionadas = 0
        self.max_colisiones_trampa = 5
        self.energias_recolectadas = 0
        # Nuevos atributos para el rectángulo de colisión
        self.hitbox = pg.rect.Rect(self.rect.x, self.rect.y, ANCHO_JUGADOR_HITBOX, ALTO_JUGADOR_HITBOX)

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


    def colisionar_trampa(self):
        self.energia -= 20
        if self.energia == 0:
            self.vidas -= 1
        else:
            self.energia = 100  # Reiniciar la energía
            self.trampas_colisionadas = 0  # Reiniciar el contador de colisiones

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        self.aplicar_gravedad()
        self.actualizar_defensa()

    def aplicar_gravedad(self):
        if self.en_el_aire:
            self.rect.y += self.velocidad_y * 2
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

    def perder_energia(self, cantidad):
        self.energia -= cantidad
        if self.energia <= 0:
            self.vidas -= 1
            self.energia = 100  # Reiniciar la energía

    def colisionar_enemigo(self):
        self.perder_vida()
        if self.vidas == 0:
            print("GAME OVER")

    def colisionar_trampa(self):
        self.trampas_colisionadas += 1
        self.energia -= 20
        if self.trampas_colisionadas % self.max_colisiones_trampa == 0:
            if self.energia <= 0:
                self.vidas -= 1
            self.energia = 100

    def debugger(self, pantalla):
        pg.draw.rect(pantalla, (AZUL), self.rect, 3)

    # def aplicar_gravedad(self):
    #     if self.en_el_aire:
    #         self.rect.y += self.velocidad_y
    #         self.hitbox.y = self.rect.y + ALTO_JUGADOR_HITBOX - ALTO_JUGADOR_HITBOX
    #         self.velocidad_y += self.gravedad

    #         # Controlar límite inferior (suelo) con el hitbox
    #         if self.hitbox.y >= self.piso:
    #             self.rect.y = self.piso - ALTO_JUGADOR_HITBOX + ALTO_JUGADOR_HITBOX
    #             self.hitbox.y = self.rect.y + ALTO_JUGADOR_HITBOX - ALTO_JUGADOR_HITBOX
    #             self.en_el_aire = False
    #             self.velocidad_y = 0
    #         else:
    #             self.hitbox.y = self.rect.y + ALTO_JUGADOR_HITBOX - ALTO_JUGADOR_HITBOX

    