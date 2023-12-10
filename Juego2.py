import pygame as pg, sys, random
from Jugador import Jugador
from Puntaje import Puntaje
from Vida import Vida
from Nivel import Nivel
from config import *


class Juego(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pg.init()
        pg.mixer.init()

        #Configuracion de la pantalla
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("A jugar con Dino")

        # Crear una instancia de la clase Nivel
        self.nivel = Nivel(self.pantalla, ANCHO, ALTO, "nivel_1")

    def ejecutar_juego(self):
        self.nivel.inicializar_nivel()
        #Cargo la fuente
        self.fuente = pg.font.Font('./Fonts\BebasNeue-Regular.ttf', 36)
        #Cargo sonido
        self.sonido_recoleccion = pg.mixer.Sound(r'./Sounds\objetivo.mp3')
        self.sonido_salto = pg.mixer.Sound(r'./Sounds\jump.mp3')
        pg.mixer.music.set_volume(0.10)
        pg.mixer.music.play(-1)

        self.puntaje = Puntaje()
        self.grupo_disparos = pg.sprite.Group()
        self.grupo_sprites = pg.sprite.Group()

        #Variables del juego
        self.reloj = pg.time.Clock()
        self.en_ejecucion = True
        self.nivel_actual = 1
        self.objetivos_recolectados = 0

        self.tiempo_inicial = pg.time.get_ticks() // 1000 #Tiempo en segundos
        self.duracion_juego = 30 # duración del juego en segundos

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

            colision_plataformas = pg.sprite.spritecollide(self.nivel.jugador, self.nivel.grupo_plataformas, False)
            for plataforma in colision_plataformas:
                    if self.nivel.jugador.rect.bottom > plataforma.rect.top:
                        self.nivel.jugador.rect.bottom = plataforma.rect.top
                        self.nivel.jugador.en_el_aire = False
                        self.nivel.jugador.velocidad_y = 0
            
            colision_enemigos = pg.sprite.spritecollide(self.nivel.jugador, self.nivel.grupo_enemigos, False)
            for enemigo in colision_enemigos:
                self.nivel.grupo_vidas.remove(self.nivel.jugador.vidas)
                print("Colisión con enemigo.")
            if self.nivel.jugador.vidas < 1:
                self.en_ejecucion = False
                self.pantalla.fill(BLANCO)
                self.pantalla.blit(texto_derrota, (ANCHO // 2, ALTO // 2))
                pg.display.flip()
                tiempo_espera = 2000  # en milisegundos
                pg.time.delay(tiempo_espera)


            for disparo in self.grupo_disparos:
                colision_enemigos = pg.sprite.spritecollide(disparo, self.nivel.grupo_enemigos, True)
                for enemigo in colision_enemigos:
                    self.puntaje.matar_enemigo(enemigo.puntaje)
                    disparo.kill()
                    print("Enemigo eliminado.")

                colision_trampas = pg.sprite.spritecollide(disparo, self.nivel.grupo_trampas, True)
                for trampa in colision_trampas:
                    self.puntaje.destruir_trampa(trampa.puntaje)
                    disparo.kill()
                    print("Trampa destruida.")

                colision_disparo_plataforma = pg.sprite.spritecollide(disparo, self.nivel.grupo_plataformas, False)
                for plataforma in colision_disparo_plataforma:
                    disparo.kill()

            colision_trampa_jugador = pg.sprite.spritecollide(self.nivel.jugador, self.nivel.grupo_trampas, True)
            for trampa in colision_trampa_jugador:
                self.nivel.jugador.colision_con_trampa += 1
                if self.nivel.jugador.colision_con_trampa == 3:
                    self.nivel.jugador.vidas -= 1
                    self.nivel.grupo_vidas.remove(self.nivel.vidas)
                    print("Vida menos")
                    print("Colision con trampa.")

        
            colision_objetivos = pg.sprite.spritecollide(self.nivel.jugador, self.nivel.grupo_objetivos, True)
            for objetivo in colision_objetivos:
                    self.sonido_recoleccion.set_volume(0.05)
                    self.sonido_recoleccion.play()  
                    self.puntaje.recolectar_objetivo(objetivo.puntaje)
                    self.objetivos_recolectados += 1
                    print("Objetivo recolectado")
            # Verifico si se recolectaron todos los objetivos para cambiar de nivel
            if self.objetivos_recolectados >= self.nivel.configuracion_nivel.get("cantidad_objetivos"):
                self.cambiar_nivel()
            
            colision_energia = pg.sprite.spritecollide(self.nivel.jugador, self.nivel.grupo_energias, True)
            for energia in colision_energia:
                    self.puntaje.recolectar_energia(energia.puntaje)
                    self.sonido_recoleccion.set_volume(0.05)
                    self.sonido_recoleccion.play() 
                    self.nivel.jugador.energias_recolectadas += 1
                    if self.nivel.jugador.energias_recolectadas == 3:
                        print("Energia recolectada")
                        nueva_vida = Vida(x = random.randint(200, 400), y = 25)
                        self.nivel.grupo_vidas.add(nueva_vida)
                    

            #Actualizo los sprites
            # self.nivel.grupo_sprites.update()
            self.nivel.grupo_objetivos.update() 
            self.nivel.grupo_enemigos.update()
            self.nivel.grupo_plataformas.update()
            self.nivel.grupo_objetivos.update()
            self.nivel.grupo_energias.update()
            self.nivel.grupo_trampas.update()
            self.nivel.grupo_vidas.update()

            #Dibujo en la pantalla
            self.pantalla.blit(self.nivel.imagen_fondo, (0, 0))
            self.pantalla.blit(self.nivel.jugador.image, self.nivel.jugador.rect)
            texto_temporizador = self.fuente.render(f"Tiempo: {tiempo_restante}", True, (NEGRO))
            self.pantalla.blit(texto_temporizador, (ANCHO - 150, 10))
            texto_puntaje = self.fuente.render(f'Puntaje: {self.puntaje.obtener_puntaje()}', True, NEGRO)
            self.pantalla.blit(texto_puntaje, (10, 10))

            #Renderizo todos los sprites 
            self.nivel.grupo_sprites.draw(self.pantalla)
            self.nivel.grupo_vidas.draw(self.pantalla)
            self.nivel.grupo_objetivos.draw(self.pantalla)
            self.grupo_sprites.draw(self.pantalla)
            self.grupo_disparos.draw(self.pantalla)

            # Actualizar el jugador
            self.mover_con_teclas()
            self.delimitar_jugador()
            self.grupo_sprites.update()
            self.grupo_disparos.update()
            self.nivel.grupo_vidas.update()
            self.nivel.jugador.update()

            pg.display.flip()
            self.reloj.tick(20)

    def mover_con_teclas(self):
        #Manejo del jugador
        teclas = pg.key.get_pressed()
        if teclas[pg.K_SPACE]:
            self.nivel.jugador.saltar()
            self.sonido_salto.set_volume(0.01)
            self.sonido_salto.play()
        elif teclas[pg.K_RIGHT]:
            self.nivel.jugador.mover_der(5)
        elif teclas[pg.K_LEFT]:
            self.nivel.jugador.mover_izq(5)
        elif teclas[pg.K_z]:
            self.nivel.jugador.disparar(self.grupo_sprites, self.grupo_disparos)

        #Aplico gravedad
        self.nivel.jugador.aplicar_gravedad()

    def delimitar_jugador(self):
        #Limites
        if self.nivel.jugador.rect.left <= -1:
            self.nivel.jugador.rect.left = -1
        elif self.nivel.jugador.rect.right >= ANCHO + 1:
            self.nivel.jugador.rect.right = ANCHO + 1
        elif self.nivel.jugador.rect.top <= 0:
            self.nivel.jugador.rect.top = 0
        elif self.nivel.jugador.rect.bottom >= ALTO + 1:
            self.nivel.jugador.rect.bottom = ALTO + 1


    def cambiar_nivel(self):
        #Incremento el número del nivel
        self.nivel_actual += 1

        #Genero el nombre del próximo nivel
        nombre_nuevo_nivel = f"nivel_{self.nivel_actual}"

        #Reinicio la cuenta de objetivos recolectados
        self.objetivos_recolectados = 0

        #Reinicio el tiempo para el nuevo nivel si es necesario
        self.tiempo_inicial = pg.time.get_ticks() // 1000

        #Reinicio el juego con el nuevo nivel
        self.nivel = Nivel(self.pantalla, ANCHO, ALTO, nombre_nuevo_nivel)
        self.nivel.inicializar_nivel()






        


