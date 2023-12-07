import pygame as pg
from config import *
from Jugador import Jugador

class Nivel:
    def __init__(self, pantalla, ancho_pantalla, alto_pantalla, nombre_del_nivel):
        self.configuracion = abrir_json().get(nombre_del_nivel)
        self.configuracion_jugador = self.configuracion("jugador")
        self.jugador_sprites = Jugador((0, alto_pantalla), 
                                        self.configuracion_jugador.get("jugador_parado_der"),
                                        self.configuracion_jugador.get("jugador_parado_izq"),
                                        self.configuracion_jugador.get("jugador_camina_der"),
                                        self.configuracion_jugador.get("jugador_camina_izq"))
        #Configuro el nivel
        self.configuracion_nivel = self.configuracion.get("nivel")
        #Configuro los enemigos
        self.configuracion_enemigo = self.configuracion.get("enemigo")
        #Configuro los objetivos
        self.configuracion_objetivo = self.configuracion.get("objetivo")
        #Configuro la energia
        self.configuracion_energia = self.configuracion.get("energia")
        #configuro la trampa 
        self.configuracion_trampa = self.configuracion.get("trampa")
        #Configuro la vida
        self.configuracion_vida = self.configuracion.get("vidas")
        #Configuro las plataformas
        self.configuracion_plataformas = self.configuracion.get("plataformas")
