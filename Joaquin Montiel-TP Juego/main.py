import pygame, sys
from config import *
from Jugador import *
from Trampa import *
from Plataforma import *


#Inicializo pygame
pygame.init()

reloj = pygame.time.Clock()

#Creo la ventana
pantalla = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Juego con Dinosaurios")

#Cargar imagen de fondo y platasformas 
fondo = pygame.transform.scale(pygame.image.load(RUTA_FONDO), (WIDTH, HEIGTH))

#Inicializo los grupos:
sprites = pygame.sprite.Group()
meteoritos = pygame.sprite.Group()

#Inicializo las instancias:
plataforma_1 = Plataforma(RUTA_PLATAFORMA_1, SIZE_PLATAFORMA)
plataforma_2 = Plataforma(RUTA_PLATAFORMA_2, SIZE_PLATAFORMA)
dinosaurio = Jugador((WIDTH // 2, HEIGTH), RUTA_DER, RUTA_IZQ, dinosaurio_camina_der, dinosaurio_camina_izq)
sprites.add(dinosaurio)
nuevo_fuego = Fuego(RUTA_FUEGO, TAMAÑO_FUEGO)

#Bucle principal
clock = pygame.time.Clock()
while True:
    reloj.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE]:
        dinosaurio.saltar()
    elif teclas[pygame.K_RIGHT]:
        dinosaurio.mover_der(5)
        # dinosaurio.image = dinosaurio.dinosaurio_der
    elif teclas[pygame.K_LEFT]:
        dinosaurio.mover_izq(5)
        # dinosaurio.image = dinosaurio.dinosaurio_izq
    # Lógica para disparar fuego con la tecla 'Z'
    elif teclas[pygame.K_z]:
        dinosaurio.disparar_fuego(sprites)
    else:
        # Si no se presionan las teclas de movimiento, establecer el sprite de estar quieto
        dinosaurio.indice_sprite = 0
        dinosaurio.velocidad_x = 0
        if dinosaurio.velocidad_x > 0:
            dinosaurio.image = dinosaurio.dinosaurio_der
        elif dinosaurio.velocidad_x < 0:
            dinosaurio.image = dinosaurio.dinosaurio_izq
    

    #Aplicar gravedad
    dinosaurio.aplicar_gravedad()

    #Limites
    if dinosaurio.rect.left <= 0:
        dinosaurio.rect.left = 0
    elif dinosaurio.rect.right >= WIDTH:
        dinosaurio.rect.right = WIDTH
    elif dinosaurio.rect.top <= 0:
        dinosaurio.rect.top = 0
    elif dinosaurio.rect.bottom >= HEIGTH:
        dinosaurio.rect.bottom = HEIGTH

    for meteorito in meteoritos:
        if meteorito.rect.top >= HEIGTH:
            meteorito.kill()
    
    generate_meteoritos(sprites, meteoritos, pantalla, MAX_ASTEROID)

    dinosaurio.actualizar_fuego_cooldown()

    sprites.update()

    #Dibujar en pantalla
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(plataforma_1.image, (500, 310))
    pantalla.blit(plataforma_1.image, (300, 390))
    pantalla.blit(plataforma_2.image, (150, 490))
    pantalla.blit(plataforma_2.image, (550, 490))

    sprites.draw(pantalla)
    
    # Actualizar pantalla
    pygame.display.flip()

    # Añadir un pequeño retardo para controlar la velocidad de la animación
    clock.tick(20)