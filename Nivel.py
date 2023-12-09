import pygame as pg, random
from config import *
from Jugador import Jugador
from Plataforma import Plataforma
from Enemigo import Enemigo
from Objetivo import Huevo
from Energia  import Energia
from Trampa import Asteroide
from Vida import Vida


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

        #Iniciar los grupos de sprites
        self.grupo_sprites = pg.sprite.Group()
        self.grupo_trampas = pg.sprite.Group()
        self.grupo_disparos = pg.sprite.Group()
        self.grupo_plataformas = pg.sprite.Group()
        self.grupo_objetivos = pg.sprite.Group()
        self.grupo_energias = pg.sprite.Group()
        self.grupo_enemigos = pg.sprite.Group()
        self.grupo_vidas = pg.sprite.Group()

        #Configuro el nivel con los datos del json
        self.imagen_nivel = self.configuracion_nivel("fondo_pantalla")
        self.imagen_fondo = pg.transform.scale(pg.image.load(self.imagen_nivel), (ANCHO, ALTO))
        self.musica_fondo = pg.mixer.music.load(self.configuracion_nivel.get("musica_fondo"))
        self.sonido_game_over = pg.mixer.Sound(self.configuracion_nivel.get("sonido_game_over"))
        self.sonido_victoria = pg.mixer.Sound(self.configuracion_nivel.get("sonido_victoria"))
        #Pantalla principal
        self.pantalla_principal = pantalla
        self.tiempo_trasncurrido = 0

        #Juego ganado
        self.juego_ganado_sonido = False
        #Juego perdido
        self.juego_perdido = False

        #Cargo plataformas
        self.plataformas = self.configuracion_plataformas
        self.crear_plataformas()
        self.mostrar_plataformas()

        #Cargo enemigos
        self.enemigo = self.configuracion_enemigo
        self.crear_enemigos()
        self.mostrar_enemigos()

        #Cargar objetivos
        self.objetivos = self.configuracion_objetivo
        self.crear_objetivos()
        self.mostrar_objetivos()

        #Cargar energias
        self.energia = self.configuracion_energia
        self.crear_energias()
        self.mostrar_energias()

        #Cargar trampas
        self.trampas = self.configuracion_trampa()
        self.crear_trampas()
        self.mostrar_trampas()

        #Cargar Vidas
        self.vidas = self.configuracion_vida
        self.crear_vidas()
        self.mostrar_vidas()


    def crear_plataformas(self):
        for nombre, datos in self.plataformas.items():
            imagen = datos["imagen"]
            x = datos["x"]
            y = datos["y"]
            ancho = datos["ancho"]
            alto = datos["alto"]

            plataforma = Plataforma(imagen, x, y, ancho, alto)
            self.grupo_plataformas.add(plataforma)
    
    def mostrar_plataformas(self):
        for plataforma in self.grupo_plataformas:
            plataforma.draw(self.pantalla_principal)

    def crear_enemigos(self):
        for _ in range(self.configuracion.get("cantidad_enemigos")):
            x = random.randint(self.enemigo.get("valor_x_1"), self.enemigo.get("valor_x_2"))
            y = self.enemigo.get("valor_y_1") - self.enemigo.get("valor_y_2")
            self.aliens = Enemigo(self.enemigo.get("enemigo_der"), self.enemigo.get("enemigo_izq"), x, y)
            self.grupo_enemigos(self.aliens)

    def mostrar_enemigos(self):
        for enemigo in self.grupo_enemigos:
            enemigo.draw(self.pantalla_principal)

    def crear_objetivos(self):
        cantidad_objetivos = self.configuracion_nivel.get("cantidad_objetivos")
        for nombre, datos in self.objetivos.items():
            imagen = datos["imagen"]
            ancho = datos["ancho"]
            alto = datos["alto"]
            for i in range(1, cantidad_objetivos + 1):
                x = datos[f"objetivo_{i}"]["x"]
                y = datos[f"objetivo_{i}"]["y"]
                objetivo = Huevo(imagen, x, y, ancho, alto)
                self.grupo_objetivos.add(objetivo)

    def mostrar_objetivos(self):
        for objetivo in self.grupo_objetivos:
            objetivo.draw(self.pantalla_principal)

    def crear_energias(self):
        cantidad_energias = self.configuracion_nivel.get("cantidad_energia")
        for nombre, datos in self.energia.items():
            imagen = datos["imagen"]
            ancho = datos["ancho"]
            alto = datos["alto"]
            for i in range(1, cantidad_energias + 1):
                x = datos[f"objetivo_{i}"]["x"]
                y = datos[f"objetivo_{i}"]["y"]
                energia = Energia(imagen, x, y, ancho, alto)
                self.grupo_energias.add(energia)

    def mostrar_energias(self):
        for energia in self.grupo_energias:
            energia.draw(self.pantalla_principal)

    def crear_trampas(self):
        if len(self.grupo_trampas) == 0:
            cantidad_trampas = self.configuracion_nivel.get("cantidad_trampas")
            datos_trampa = self.configuracion_nivel.get("trampa")
            imagen = datos_trampa["imagen"]

            for i in range(cantidad_trampas):
                x = random.randint(datos_trampa["x"]["valor_x_1"], datos_trampa["x"]["valor_x_2"])
                y = random.randint(datos_trampa["y"]["valor_y_1"], datos_trampa["y"]["valor_y_2"])
                trampa = Asteroide(imagen, (x, y), VELOCIDAD_ASTEROIDE)
                self.grupo_trampas.add(trampa)

    def mostrar_trampas(self):
        for trampa in self.grupo_trampas:
            trampa.draw(self.pantalla_principal)

    def crear_vidas(self):
        cantidad_vidas = self.vidas.get("cantidad_vidas")
        for i in range(cantidad_vidas):
            x = (ANCHO -(20 * self.jugador.vidas)) // 2 + i * 30
            y = 25
            vida = Vida(x, y)
            self.grupo_vidas.add(vida) 




    


