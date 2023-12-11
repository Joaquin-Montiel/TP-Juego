# import pygame as pg, sys, random
# from config import *
# from Jugador import Jugador
# from Trampa import Asteroide, generar_trampas
# from Plataforma import Plataforma
# from Objetivo import Huevo
# from Energia import Energia
# from Disparo import Defensa
# from Enemigo import Enemigo
# from Puntaje import Puntaje
# from Vida import Vida

# puntuacion = 0
# derrota = 0
# victoria = 0


# #Inicializo pygame
# pg.init()
# pg.mixer.init()

# sonido_recoleccion = pg.mixer.Sound(r'./Sounds\objetivo.mp3')
# sonido_salto = pg.mixer.Sound(r'./Sounds\jump.mp3')
# sonido_fondo = pg.mixer.music.load(r'./Sounds\videojuegos.mp3')
# # pg.mixer.music.set_volume(0.10)
# # pg.mixer.music.play(-1)

# reloj = pg.time.Clock()
# # Configuración del cronómetro
# tiempo_inicial = 60  # Tiempo en segundos
# tiempo_actual = tiempo_inicial
# tiempo_cronometro = pg.time.get_ticks() // 1000 + tiempo_inicial  # Convierte a segundos

# #Creo la ventana
# pantalla = pg.display.set_mode((ANCHO, ALTO))
# pg.display.set_caption("Juego con Dinosaurios")

# #Cargar imagen de fondo
# fondo = pg.transform.scale(pg.image.load(RUTA_FONDO), (ANCHO, ALTO))
# fuente = pg.font.Font('./Fonts\BebasNeue-Regular.ttf', 36)
# puntaje = Puntaje()

# #Inicializo los grupos:
# sprites = pg.sprite.Group()
# trampas = pg.sprite.Group()
# plataformas = pg.sprite.Group()
# disparos = pg.sprite.Group()
# objetivos = pg.sprite.Group()
# energias = pg.sprite.Group()
# enemigos = pg.sprite.Group()
# vidas = pg.sprite.Group()


# #Inicializo las instancias:
# dinosaurio = Jugador((0, ALTO), RUTA_DER, RUTA_IZQ, dinosaurio_camina_der, dinosaurio_camina_izq)

# for i in range(dinosaurio.vidas):
#             x = (ANCHO -(20 * dinosaurio.vidas)) // 2 + i * 30
#             y = 25
#             vida = Vida(x, y)
#             vidas.add(vida) 

# plataforma_1 = Plataforma(RUTA_PLATAFORMA_1, 500, 310, 150, 150)
# plataforma_2 = Plataforma(RUTA_PLATAFORMA_1, 210, 320, 150, 150)
# plataforma_3 = Plataforma(RUTA_PLATAFORMA_2, 550, 470, 150, 150)
# plataforma_4 = Plataforma(RUTA_PLATAFORMA_2, 100, 470, 150, 150)
# plataformas.add(plataforma_1, plataforma_2, plataforma_3, plataforma_4)

# for i in range(NUM_ENEMIGOS):
#     x = random.randint(200, 500)
#     y =  ALTO - 1
#     aliens = Enemigo((x, y))
#     enemigos.add(aliens)

# objetivo_1 = Huevo(530, 330, 40, 40)
# objetivo_2 = Huevo(240, 340, 40, 40)
# objetivo_3 = Huevo(400, 558, 40, 40)
# objetivo_4 = Huevo(290, 340, 40, 40)
# objetivos.add(objetivo_1, objetivo_2, objetivo_3, objetivo_4)

# energia_1 = Energia(380, 415, 40, 40)
# energia_2 = Energia(150, 515, 40, 40)
# energia_3 = Energia(410, 415, 40, 40)
# energia_4 = Energia(580, 330, 40, 40)
# energia_5 = Energia(390, 450, 40, 40)
# energias.add(energia_1, energia_2, energia_3, energia_4, energia_5)

# sprites.add(dinosaurio, plataformas, objetivos, energias, enemigos, vidas)


# #Bucle principal
# clock = pg.time.Clock()
# while True:
#     tiempo_transcurrido = pg.time.get_ticks() // 1000  # Convierte a segundos
#     tiempo_restante = max(0, tiempo_cronometro - tiempo_transcurrido)
#     reloj.tick(FPS)
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             sys.exit()

#     #Manejo del jugador
#     teclas = pg.key.get_pressed()
#     if teclas[pg.K_SPACE]:
#         dinosaurio.saltar()
#         # sonido_salto.set_volume(0.01)
#         # sonido_salto.play()
#     elif teclas[pg.K_RIGHT]:
#         dinosaurio.mover_der(5)
#     elif teclas[pg.K_LEFT]:
#         dinosaurio.mover_izq(5)
#     elif teclas[pg.K_z]:
#         dinosaurio.disparar(sprites, disparos)
    
#     # Actualizar la posición del dinosaurio antes de aplicar la gravedad
#     dinosaurio.update()

#     #Aplicar gravedad
#     dinosaurio.aplicar_gravedad()

#     generar_trampas(sprites, trampas, pantalla, MAX_ASTEROID)

#     #Limites
#     if dinosaurio.rect.left <= -3:
#         dinosaurio.rect.left = -3
#     elif dinosaurio.rect.right >= ANCHO + 5:
#         dinosaurio.rect.right = ANCHO + 5
#     elif dinosaurio.rect.top <= 0:
#         dinosaurio.rect.top = 0
#     elif dinosaurio.rect.bottom >= ALTO:
#         dinosaurio.rect.bottom = ALTO

#     # colision_plataformas = pg.sprite.spritecollide(dinosaurio, plataformas, False)
#     # for plataforma in colision_plataformas:
#     #         if dinosaurio.rect.bottom > plataforma.rect.top:
#     #             dinosaurio.rect.bottom = plataforma.rect.top
#     #             dinosaurio.en_el_aire = False
#     #             dinosaurio.velocidad_y = 0


#     colision_enemigos = pg.sprite.spritecollide(dinosaurio, enemigos, False)
#     for enemigo in colision_enemigos:
#         dinosaurio.colisionar_enemigo()  # Llamar al método al colisionar con un enemigo
#         print("Colisión con enemigo.")
#         dinosaurio.perder_vida()
#         vidas.remove(1)

#     for disparo in disparos:
#         colision_enemigos = pg.sprite.spritecollide(disparo, enemigos, True)
#         for enemigo in colision_enemigos:
#             puntaje.matar_enemigo(enemigo.puntaje)
#             disparo.kill()
#             print("Enemigo eliminado.")

#         colision_trampas = pg.sprite.spritecollide(disparo, trampas, True)
#         for trampa in colision_trampas:
#             puntaje.destruir_trampa(trampa.puntaje)
#             disparo.kill()
#             print("Trampa destruida.")
    
#     for trampa in trampas.sprites():
#         if trampa.rect.top >= ALTO:
#             trampa.kill()
#         elif pg.sprite.collide_rect(dinosaurio, trampa):
#             dinosaurio.colisionar_trampa()
#             print("Colision con trampa.")
#             trampa.kill()
#             if dinosaurio.colisionar_trampa == dinosaurio.max_colisiones_trampa:
#                 dinosaurio.perder_vida()
#                 vidas.remove(1)


#     for objetivo in objetivos:
#         if pg.sprite.collide_rect(dinosaurio, objetivo):
#             puntaje.recolectar_objetivo(objetivo.puntaje)
#             # sonido_recoleccion.set_volume(0.05)
#             # sonido_recoleccion.play()
#             objetivo.kill()  
#             print("Objetivo recolectado")
#     for energia in energias:
#         if pg.sprite.collide_rect(dinosaurio, energia):
#             puntaje.recolectar_energia(energia.puntaje)
#             # sonido_recoleccion.play()
#             energia.kill()  
#             dinosaurio.energias_recolectadas += 1
#             print("Energia recolectada")

#     vidas.update()

#     sprites.update()

#     #Dibujar en pantalla
#     pantalla.blit(fondo, (0, 0))
#     sprites.draw(pantalla)
    
#     # Mostrar el puntaje en la pantalla
#     puntaje_texto = fuente.render(f'Puntaje: {puntaje.obtener_puntaje()}', True, NEGRO)
#     pantalla.blit(puntaje_texto, (10, 10))
#     tiempo_texto = fuente.render(f'Tiempo: {tiempo_restante}', True, NEGRO)
#     pantalla.blit(tiempo_texto, (ANCHO - 150, 10))
    
#     # Actualizar pantalla
#     pg.display.flip()

#     # Añadir un pequeño retardo para controlar la velocidad de la animación
#     clock.tick(20)