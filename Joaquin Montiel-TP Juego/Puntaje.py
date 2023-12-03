import pygame as pg

class Puntaje:
    def __init__(self):
        self.puntaje = 0

    def matar_enemigo(self, cantidad_puntos):
        self.puntaje += cantidad_puntos

    def recolectar_objetivo(self, cantidad_puntos):
        self.puntaje += cantidad_puntos
    
    def recolectar_energia(self, cantidad_puntos):
        self.puntaje += cantidad_puntos

    def destruir_trampa(self, cantidad_puntos):
        self.puntaje += cantidad_puntos

    def obtener_puntaje(self):
        return self.puntaje