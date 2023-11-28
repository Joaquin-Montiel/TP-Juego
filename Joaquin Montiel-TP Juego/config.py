import pygame, random
from Trampa import *

#Configuro la ventana del juego
WIDTH = 800
HEIGTH  = 600
FPS = 60

SIZE_PLATAFORMA = (120, 120)
RUTA_FONDO = r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\fondo.jpg'
RUTA_PLATAFORMA_1 = r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\plataforma1.png'
RUTA_PLATAFORMA_2 = r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\plataforma2.png'
RUTA_FUEGO = r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\llama_der.png'

#Cargo los sprites
RUTA_DER = r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Still.png'
RUTA_IZQ = r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Still(iz).png'
RUTA_ASTEROIDE = r"C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\meteorito.png"

dinosaurio_camina_der = [
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(1).png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(2).png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(3).png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(4).png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(5).png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(6).png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(7).png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(8).png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(9).png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(10).png')
]
dinosaurio_camina_izq = [
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(1)iz.png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(2)iz.png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(3)iz.png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(4)iz.png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(5)iz.png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(6)iz.png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(7)iz.png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(8)iz.png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(9)iz.png'),
    pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(10)iz.png')
]
TAMAÑO_FUEGO = (15, 15)
VELOCIDAD_FUEGO = 5
VELOCIDAD_ASTEROIDE = 1
MAX_ASTEROID = 3
def generate_meteoritos(g_sprites, g_meteoritos, pantalla: pygame.Surface, cantidad: int=10):
    if len(g_meteoritos) == 0:
        for i in range(cantidad):
            x = random.randrange(40, pantalla.get_width() -40)
            y = random.randrange(40, pantalla.get_height() // 2)
            meteoritos = Asteroide(RUTA_ASTEROIDE, (x, y), VELOCIDAD_ASTEROIDE)
            g_sprites.add(meteoritos)
            g_meteoritos.add(meteoritos)

