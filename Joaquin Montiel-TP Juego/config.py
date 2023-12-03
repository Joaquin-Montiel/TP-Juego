import pygame as pg

#Configuro la ventana del juego
WIDTH = 800
HEIGTH  = 600
FPS = 20

RUTA_FONDO = r'./sprites_juego\fondo.jpg'

#Cargo los sprites
RUTA_DER = r'./sprites_juego\Idlle\Idlle_der.png'
RUTA_IZQ = r'./sprites_juego\Idlle\Idlle_izq.png'
RUTA_ENEMIGO_DER = r'./sprites_juego\Enemigo\enemigo_der.png'
RUTA_ENEMIGO_IZQ = r'./sprites_juego\Enemigo\enemigo_iz.png'
RUTA_PLATAFORMA_1 = r'./sprites_juego\Plataformas\plataforma1.png'
RUTA_PLATAFORMA_2 = r'./sprites_juego\Plataformas\plataforma2.png'
RUTA_FUEGO_DER = r'./sprites_juego\Defensa\llama_der.png'
RUTA_FUEGO_IZQ = r'./sprites_juego\Defensa\llama_izq.png'
RUTA_ASTEROIDE = r"./sprites_juego\Enemigo\meteorito.png"
RUTA_HUEVO = r'./sprites_juego\Energia\huevo_dino.png'
RUTA_ENERGIA = r'./sprites_juego\Energia\hueso_de_carne.png'

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

NEGRO = (0, 0, 0)
NUM_ENEMIGOS = 3
VELOCIDAD_ASTEROIDE = 1
MAX_ASTEROID = 3


