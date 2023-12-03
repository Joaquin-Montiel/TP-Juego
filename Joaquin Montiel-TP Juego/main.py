import pygame as pg, sys, random
from config import *
from Jugador import Jugador
from Trampa import Asteroide, generar_trampas
from Plataforma import Plataforma
from Objetivo import Huevo
from Energia import Energia
from Fuego import Defensa
from Enemigo import Enemigo
from Puntaje import Puntaje
from Vida import Vida

#Inicializo pygame
pg.init()

reloj = pg.time.Clock()

#Creo la ventana
pantalla = pg.display.set_mode((WIDTH, HEIGTH))
pg.display.set_caption("Juego con Dinosaurios")

#Cargar imagen de fondo
fondo = pg.transform.scale(pg.image.load(RUTA_FONDO), (WIDTH, HEIGTH))
fuente = pg.font.Font('./Fonts\BebasNeue-Regular.ttf', 36)
puntaje = Puntaje()

#Inicializo los grupos:
sprites = pg.sprite.Group()
trampas = pg.sprite.Group()
plataformas = pg.sprite.Group()
disparos = pg.sprite.Group()
objetivos = pg.sprite.Group()
energias = pg.sprite.Group()
enemigos = pg.sprite.Group()
vidas = pg.sprite.Group()


#Inicializo las instancias:
dinosaurio = Jugador((0, HEIGTH), RUTA_DER, RUTA_IZQ, dinosaurio_camina_der, dinosaurio_camina_izq)

for i in range(dinosaurio.vidas):
        x = (WIDTH - (20 * dinosaurio.vidas)) // 2 + i * 30
        y = 25
        vida = Vida(x, y)
        vidas.add(vida)
        sprites.add(vidas)

for vida in vidas:
    vida.jugador = dinosaurio  

plataforma_1 = Plataforma(RUTA_PLATAFORMA_1, 500, 310, 150, 150)
plataforma_2 = Plataforma(RUTA_PLATAFORMA_1, 210, 320, 150, 150)
plataforma_3 = Plataforma(RUTA_PLATAFORMA_2, 550, 470, 120, 150)
plataforma_4 = Plataforma(RUTA_PLATAFORMA_2, 100, 470, 120, 150)
plataformas.add(plataforma_1, plataforma_2, plataforma_3, plataforma_4)


for i in range(NUM_ENEMIGOS):
    x = random.randint(0, WIDTH)
    # Ajustar la posición y para estar cerca del borde inferior
    y =  HEIGTH - 3
    aliens = Enemigo((x, y), RUTA_ENEMIGO_DER, RUTA_ENEMIGO_IZQ)
    enemigos.add(aliens)

objetivo_1 = Huevo(RUTA_HUEVO, 530, 330, 40, 40)
objetivo_2 = Huevo(RUTA_HUEVO, 240, 340, 40, 40)
objetivo_3 = Huevo(RUTA_HUEVO, 400, 558, 40, 40)
objetivo_4 = Huevo(RUTA_HUEVO, 290, 340, 40, 40)
objetivos.add(objetivo_1, objetivo_2, objetivo_3, objetivo_4)

energia_1 = Energia(RUTA_ENERGIA, 380, 415, 40, 40)
energia_2 = Energia(RUTA_ENERGIA, 150, 515, 40, 40)
energia_3 = Energia(RUTA_ENERGIA, 410, 415, 40, 40)
energia_4 = Energia(RUTA_ENERGIA, 580, 330, 40, 40)
energia_5 = Energia(RUTA_ENERGIA, 390, 450, 40, 40)
energias.add(energia_1, energia_2, energia_3, energia_4, energia_5)

sprites.add(dinosaurio, plataformas, objetivos, energias, enemigos)


#Bucle principal
clock = pg.time.Clock()
while True:
    reloj.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    #Manejo del jugador
    teclas = pg.key.get_pressed()
    if teclas[pg.K_SPACE]:
        dinosaurio.saltar()
    elif teclas[pg.K_RIGHT]:
        dinosaurio.mover_der(5)
    elif teclas[pg.K_LEFT]:
        dinosaurio.mover_izq(5)
    # Lógica para disparar fuego con la tecla 'Z'
    elif teclas[pg.K_z]:
        dinosaurio.disparar(sprites, disparos)
    
    # Actualizar la posición del dinosaurio antes de aplicar la gravedad
    dinosaurio.update()

    #Aplicar gravedad
    dinosaurio.aplicar_gravedad()

    #Limites
    if dinosaurio.rect.left <= -3:
        dinosaurio.rect.left = -3
    elif dinosaurio.rect.right >= WIDTH + 5:
        dinosaurio.rect.right = WIDTH + 5
    elif dinosaurio.rect.top <= 0:
        dinosaurio.rect.top = 0
    elif dinosaurio.rect.bottom >= HEIGTH:
        dinosaurio.rect.bottom = HEIGTH

    # Actualizar y dibujar las vidas
    vidas.update()
    vidas.draw(pantalla)

    for disparo in disparos:
        colision_enemigos = pg.sprite.spritecollide(disparo, enemigos, True)
        for enemigo in colision_enemigos:
            puntaje.matar_enemigo(enemigo.puntaje)
            disparo.kill()
            print("Enemigo eliminado.")
        colision_trampas = pg.sprite.spritecollide(disparo, trampas, True)
        for trampa in colision_trampas:
            puntaje.destruir_trampa(trampa.puntaje)
            disparo.kill()
            print("Trampa destruida.")
    
    for trampa in trampas.sprites():
        if trampa.rect.top >= HEIGTH:
            trampa.kill()
        elif pg.sprite.collide_rect(dinosaurio, trampa):
            dinosaurio.colisionar_trampa()
            print("Colision con trampa.")
            trampa.kill()

            if dinosaurio.vidas < len(vidas):
                vida = vidas.sprites()[0]
                vidas.remove(vida)

    generar_trampas(sprites, trampas, pantalla, MAX_ASTEROID)
    dinosaurio.actualizar_defensa()

    for objetivo in objetivos:
        if pg.sprite.collide_rect(dinosaurio, objetivo):
            puntaje.recolectar_objetivo(objetivo.puntaje)
            objetivo.kill()  
            print("Objetivo recolectado")
    for energia in energias:
        if pg.sprite.collide_rect(dinosaurio, energia):
            puntaje.recolectar_energia(energia.puntaje)
            energia.kill()  
            dinosaurio.energias_recolectadas += 1
            print("Energia recolectada")

            if dinosaurio.energias_recolectadas % 5 == 0:
                dinosaurio.vidas += 1

    sprites.update()

    vidas.update()
    vidas.draw(pantalla)
    
    #Dibujar en pantalla
    pantalla.blit(fondo, (0, 0))
    sprites.draw(pantalla)

    # Mostrar el puntaje en la pantalla
    puntaje_texto = fuente.render(f'Puntaje: {puntaje.obtener_puntaje()}', True, NEGRO)
    pantalla.blit(puntaje_texto, (10, 10))
    
    # Actualizar pantalla
    pg.display.flip()

    # Añadir un pequeño retardo para controlar la velocidad de la animación
    clock.tick(20)