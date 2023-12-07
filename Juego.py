import pygame as pg, sys, random
from Jugador import Jugador
from Puntaje import Puntaje
from Trampa import Asteroide, generar_trampas
from Disparo import Defensa 
from Enemigo import Enemigo
from Energia import Energia
from Objetivo import Huevo
from Plataforma import Plataforma
from config import *


class Juego(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def iniciar_nivel(self):
        pg.init()
        pg.mixer.init()

        #Configuracion de la pantalla
        self.ancho_pantalla = ANCHO
        self.alto_pantalla = ALTO
        self.pantalla = pg.display.set_mode((self.ancho_pantalla, self.alto_pantalla))
        pg.display.set_caption("A jugar con Dino")

        #Cargo el fondo
        self.imagen_fondo = pg.transform.scale(pg.image.load(r'./sprites_juego\Fondo\fondo.jpg'), (ANCHO, ALTO))

        #Cargo la fuente
        self.fuente = pg.font.Font('./Fonts\BebasNeue-Regular.ttf', 36)
        
        #Cargo sonido
        self.sonido_recoleccion = pg.mixer.Sound(r'./Sounds\objetivo.mp3')
        self.sonido_salto = pg.mixer.Sound(r'./Sounds\jump.mp3')
        self.sonido_fondo = pg.mixer.music.load(r'./Sounds\videojuegos.mp3')
        # pg.mixer.music.set_volume(0.10)
        # pg.mixer.music.play(-1)

        #Iniciar los grupos de sprites
        self.grupo_sprites = pg.sprite.Group()
        self.grupo_trampas = pg.sprite.Group()
        self.grupo_disparos = pg.sprite.Group()
        self.grupo_plataformas = pg.sprite.Group()
        self.grupo_objetivos = pg.sprite.Group()
        self.grupo_energias = pg.sprite.Group()
        self.grupo_enemigos = pg.sprite.Group()

        #Instancio las clases
        self.jugador = Jugador((0, ALTO), RUTA_DER, RUTA_IZQ, dinosaurio_camina_der, dinosaurio_camina_izq)
        
        for i in range(NUM_ENEMIGOS):
            x = random.randint(200, 500)
            y =  ALTO - 1
            self.aliens = Enemigo(RUTA_ENEMIGO_DER, RUTA_ENEMIGO_IZQ, x, y)
            self.grupo_enemigos.add(self.aliens)

        self.puntaje = Puntaje()

        self.plataforma_1 = Plataforma(RUTA_PLATAFORMA_1, 510, 335, 120, 120)
        self.plataforma_2 = Plataforma(RUTA_PLATAFORMA_1, 225, 345, 120, 120)
        self.plataforma_3 = Plataforma(RUTA_PLATAFORMA_2, 560, 510, 100, 100)
        self.plataforma_4 = Plataforma(RUTA_PLATAFORMA_2, 100, 510, 100, 100)
        self.grupo_plataformas.add(self.plataforma_1, self.plataforma_2, self.plataforma_3, self.plataforma_4)
        for plataforma in self.grupo_plataformas:
                plataforma.mask = pg.mask.from_surface(plataforma.image)

        self.objetivo_1 = Huevo(RUTA_OBJETIVO, 530, 330, 40, 40)
        self.objetivo_2 = Huevo(RUTA_OBJETIVO, 240, 340, 40, 40)
        self.objetivo_3 = Huevo(RUTA_OBJETIVO, 400, 558, 40, 40)
        self.objetivo_4 = Huevo(RUTA_OBJETIVO, 290, 340, 40, 40)
        self.grupo_objetivos.add(self.objetivo_1, self.objetivo_2, self.objetivo_3, self.objetivo_4)
        
        self.energia_1 = Energia(RUTA_ENERGIA, 380, 415, 40, 40)
        self.energia_2 = Energia(RUTA_ENERGIA, 150, 515, 40, 40)
        self.energia_3 = Energia(RUTA_ENERGIA, 410, 415, 40, 40)
        self.energia_4 = Energia(RUTA_ENERGIA, 580, 330, 40, 40)
        self.energia_5 = Energia(RUTA_ENERGIA, 390, 450, 40, 40)
        self.grupo_energias.add(self.energia_1, self.energia_2, self.energia_3, self.energia_4, self.energia_5)

        self.grupo_sprites.add(self.jugador, self.grupo_plataformas, self.grupo_disparos, self.grupo_objetivos, self.grupo_energias, 
                            self.grupo_enemigos)

        #Variables del juego
        self.reloj = pg.time.Clock()
        self.en_ejecucion = True
        self.nivel_actual = 1
        self.objetivos_recolectados = 0

        self.tiempo_inicial = pg.time.get_ticks() // 1000 #Tiempo en segundos
        self.duracion_juego = 60  # duración del juego en segundos

        # #Bucle principal
        while self.en_ejecucion:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    self.en_ejecucion = False

                    pg.mixer.quit()
                    pg.quit()
                    sys.exit()

            # Verifico el tiempo transcurrido
            tiempo_actual = pg.time.get_ticks() // 1000  # tiempo en segundos
            tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
            #Tiempo restante lo utilizo para mostrar tiempo en pantalla
            tiempo_restante = max(0, self.duracion_juego - tiempo_transcurrido)

            # Verifico si se alcanzó la duración del juego
            if tiempo_transcurrido >= self.duracion_juego:
                self.en_ejecucion = False
                self.pantalla.fill(BLANCO)
                texto_derrota = self.fuente.render(f"GAME OVER", True, NEGRO)
                self.pantalla.blit(texto_derrota, (ANCHO // 2, ALTO // 2))
                pg.display.flip()
                tiempo_espera = 2000  # en milisegundos
                pg.time.delay(tiempo_espera)
                print("GAME OVER")

            #Manejo del jugador
            teclas = pg.key.get_pressed()
            if teclas[pg.K_SPACE]:
                self.jugador.saltar()
                self.sonido_salto.set_volume(0.01)
                self.sonido_salto.play()
            elif teclas[pg.K_RIGHT]:
                self.jugador.mover_der(5)
            elif teclas[pg.K_LEFT]:
                self.jugador.mover_izq(5)
            elif teclas[pg.K_z]:
                self.jugador.disparar(self.grupo_sprites, self.grupo_disparos)
            
            #Aplico gravedad
            self.jugador.aplicar_gravedad()

            #Limites
            if self.jugador.rect.left <= -1:
                self.jugador.rect.left = -1
            elif self.jugador.rect.right >= ANCHO + 1:
                self.jugador.rect.right = ANCHO + 1
            elif self.jugador.rect.top <= 0:
                self.jugador.rect.top = 0
            elif self.jugador.rect.bottom >= ALTO + 1:
                self.jugador.rect.bottom = ALTO + 1

            generar_trampas(self.grupo_sprites, self.grupo_trampas, self.pantalla, MAX_ASTEROID)

            # self.jugador.aplicar_gravedad()


            for plataforma in self.grupo_plataformas:
                if self.jugador.rect.colliderect(plataforma.rect):
                    self.jugador.rect.y = plataforma.rect.y - self.jugador.rect.height
                    self.jugador.velocidad_y = 0

            # colision_plataformas = pg.sprite.spritecollide(self.jugador, self.grupo_plataformas, False)
            # for plataforma in colision_plataformas:
            #     if pg.sprite.collide_mask(self.jugador, plataforma):
            #         if self.jugador.bottom > plataforma.rect.top:
            #             self.jugador.bottom = plataforma.rect.top
            #             self.jugador.en_el_aire = False
            #             self.jugador.velocidad_y = 0

            # Actualizo el jugador usando el hitbox
            # self.jugador.rect.x = self.jugador.x
            # self.jugador.rect.y = self.jugador.y


            colision_enemigos = pg.sprite.spritecollide(self.jugador, self.grupo_enemigos, False)
            for enemigo in colision_enemigos:
                self.jugador.colisionar_enemigo() 
                print("Colisión con enemigo.")
                self.jugador.perder_vida()

            for disparo in self.grupo_disparos:
                colision_enemigos = pg.sprite.spritecollide(disparo, self.grupo_enemigos, True)
                for enemigo in colision_enemigos:
                    self.puntaje.matar_enemigo(enemigo.puntaje)
                    disparo.kill()
                    print("Enemigo eliminado.")

                colision_trampas = pg.sprite.spritecollide(disparo, self.grupo_trampas, True)
                for trampa in colision_trampas:
                    self.puntaje.destruir_trampa(trampa.puntaje)
                    disparo.kill()
                    print("Trampa destruida.")

            for trampa in self.grupo_trampas:
                if trampa.rect.top >= ALTO:
                    trampa.kill()
                elif pg.sprite.collide_rect(self.jugador, trampa):
                    self.jugador.colisionar_trampa()
                    print("Colision con trampa.")
                    trampa.kill()
                    if self.jugador.colisionar_trampa == self.jugador.max_colisiones_trampa:
                        self.jugador.perder_vida()

            colision_objetivos = pg.sprite.spritecollide(self.jugador, self.grupo_objetivos, True)
            for objetivo in colision_objetivos:
                    # self.sonido_recoleccion.set_volume(0.05)
                    # self.sonido_recoleccion.play()  
                    self.puntaje.recolectar_objetivo(objetivo.puntaje)
                    self.objetivos_recolectados += 1
                    print("Objetivo recolectado")
            # Verificar si se recolectaron todos los objetivos para cambiar de nivel
            if self.objetivos_recolectados >= 4 and tiempo_restante > 0:
                self.cambiar_nivel()

            for energia in self.grupo_energias:
                if pg.sprite.collide_rect(self.jugador, energia):
                    self.puntaje.recolectar_energia(energia.puntaje)
                    # self.sonido_recoleccion.set_volume(0.05)
                    # self.sonido_recoleccion.play()
                    energia.kill()  
                    self.jugador.energias_recolectadas += 1
                    print("Energia recolectada")

            #Actualizo los sprites
            self.jugador.update()
            self.grupo_sprites.update()

            #Dibujo al fondo en pantalla
            self.pantalla.blit(self.imagen_fondo, (0, 0))

            # Dibujo al jugador en la pantalla
            self.pantalla.blit(self.jugador.image, self.jugador.rect)

            #Dibujo texto en pantalla
            texto_temporizador = self.fuente.render(f"Tiempo: {tiempo_restante}", True, (NEGRO))
            self.pantalla.blit(texto_temporizador, (ANCHO - 150, 10))
            texto_puntaje = self.fuente.render(f'Puntaje: {self.puntaje.obtener_puntaje()}', True, NEGRO)
            self.pantalla.blit(texto_puntaje, (10, 10))

            #Renderizo todos los sprites 
            self.grupo_sprites.draw(self.pantalla)
            self.jugador.debugger(self.pantalla)
            for enemigo in self.grupo_enemigos:
                enemigo.debugger_enemigo(self.pantalla)
            for plataforma in self.grupo_plataformas:
                plataforma.debugger_plataformas(self.pantalla)

            # Actualizar el jugador
            self.jugador.update()

            pg.display.flip()
            self.reloj.tick(20)

        # def cambiar_nivel(self):
        #     self.objetivos_recolectados = 0






        


