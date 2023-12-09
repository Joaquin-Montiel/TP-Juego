import pygame as pg, json

#Configuro la ventana del juego
ANCHO = 800
ALTO = 600
FPS = 60

RUTA_FONDO = r'sprites_juego\Fondo\fondo.jpg'

#Cargo los sprites
RUTA_DER = r'./sprites_juego\Idlle\Idlle_der.png'
RUTA_IZQ = r'./sprites_juego\Idlle\Idlle_izq.png'
RUTA_PLATAFORMA_1 = r'./sprites_juego\Plataformas\piedras.png'
RUTA_PLATAFORMA_2 = r'./sprites_juego\Plataformas\tierra.png'

RUTA_PLATAFORMA_3 = r'./sprites_juego\Plataformas\plataforma1.png'
RUTA_PLATAFORMA_4 = r'./sprites_juego\Plataformas\plataforma2.png'
RUTA_FUEGO_DER = r'./sprites_juego\Defensa\llama_der.png'
RUTA_FUEGO_IZQ = r'./sprites_juego\Defensa\llama_izq.png'
RUTA_JSON = r'./juego.json'
RUTA_ENEMIGO_DER = r'./sprites_juego\Enemigo\enemigo_der.png'
RUTA_ENEMIGO_IZQ = r'./sprites_juego\Enemigo\enemigo_iz.png'
RUTA_OBJETIVO = r'./sprites_juego\Energia\huevo_dino.png'
RUTA_ENERGIA = r'./sprites_juego\Energia\hueso_de_carne.png'
RUTA_TRAMPA = r'./sprites_juego\Enemigo\meteorito.png'
RUTA_VIDA = r'sprites_juego\vida\vida.png'

dinosaurio_camina_der = [
    pg.image.load(r'./sprites_juego\Walk\Walk(1).png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(2).png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(3).png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(4).png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(5).png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(6).png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(7).png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(8).png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(9).png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(10).png')
]
dinosaurio_camina_izq = [
    pg.image.load(r'./sprites_juego\Walk\Walk(1)iz.png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(2)iz.png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(3)iz.png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(4)iz.png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(5)iz.png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(6)iz.png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(7)iz.png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(8)iz.png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(9)iz.png'),
    pg.image.load(r'./sprites_juego\Walk\Walk(10)iz.png')
]
ANCHO_JUGADOR_HITBOX = 50
ALTO_JUGADOR_HITBOX = 50

NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
NUM_ENEMIGOS = 3
VELOCIDAD_ASTEROIDE = 1
MAX_ASTEROID = 3

def abrir_json() -> dict:
    with open(RUTA_JSON, 'r', encoding='utf-8') as config:
        return json.load(config)

    #  self.plataforma_1 = Plataforma(RUTA_PLATAFORMA_1, 510, 335, 120, 120)
    #     self.plataforma_2 = Plataforma(RUTA_PLATAFORMA_1, 225, 345, 120, 120)
    #     self.plataforma_3 = Plataforma(RUTA_PLATAFORMA_2, 560, 510, 100, 100)
    #     self.plataforma_4 = Plataforma(RUTA_PLATAFORMA_2, 100, 510, 100, 100)