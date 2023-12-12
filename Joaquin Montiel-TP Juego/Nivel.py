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
        self.configuracion_tiempo = self.configuracion.get("tiempo_de_juego")
        if self.configuracion:
            self.configuracion_nivel = self.configuracion.get("nivel", {})
        else:
            # Puedes manejar la falta de configuración según tus necesidades
            print(f"No hay configuración para el nivel {nombre_del_nivel}")
            self.configuracion_nivel = {}
        # #Configuro el nivel
        # self.configuracion_nivel = self.configuracion.get("nivel")
        #Configuro el jugador
        self.configuracion_jugador = self.configuracion.get("jugador", {})
        self.jugador = Jugador((0, alto_pantalla), 
                                    self.configuracion_jugador.get("jugador_parado_der"),
                                    self.configuracion_jugador.get("jugador_parado_izq"),
                                    dinosaurio_camina_der,
                                    dinosaurio_camina_izq)
        self.jugador.vidas = self.configuracion_nivel.get("cantidad_vidas")
        
        #Configuro los enemigos
        self.configuracion_enemigo = self.configuracion.get("enemigo")
        self.enemigo = self.configuracion_enemigo

        #Configuro los objetivos
        self.configuracion_objetivo = self.configuracion.get("objetivos")
        self.objetivos = self.configuracion_objetivo

        #Configuro la energia
        self.configuracion_energia = self.configuracion.get("energia")
        self.energia = self.configuracion_energia

        #configuro la trampa 
        self.configuracion_trampa = self.configuracion.get("trampa")
        self.trampas = self.configuracion_trampa

        #Configuro la vida
        self.configuracion_vida = self.configuracion.get("vidas")
        self.vidas = self.configuracion_vida

        #Configuro las plataformas
        self.configuracion_plataformas = self.configuracion.get("plataformas")
        self.plataformas = self.configuracion_plataformas

        #Iniciar los grupos de sprites
        self.grupo_sprites = pg.sprite.Group()
        self.grupo_trampas = pg.sprite.Group()
        self.grupo_disparos = pg.sprite.Group()
        self.grupo_plataformas = pg.sprite.Group()
        self.grupo_objetivos = pg.sprite.Group()
        self.grupo_energias = pg.sprite.Group()
        self.grupo_enemigos = pg.sprite.Group()
        self.grupo_vidas = pg.sprite.Group()

        self.pantalla_principal = pantalla

        #Llamo al método de inicialización al crear una instancia de Nivel
        self.inicializar_nivel()

    def crear_plataformas(self):
        imagen = self.plataformas["imagen"]
        ancho = self.plataformas["ancho"]
        alto = self.plataformas["alto"]

        for nombre, datos in self.plataformas.items():
            if nombre.startswith("plataforma"):
                x = datos["x"]
                y = datos["y"]
                plataforma = Plataforma(imagen, x, y, ancho, alto)
                self.grupo_plataformas.add(plataforma)
        self.grupo_sprites.add(self.grupo_plataformas)


    def mostrar_plataformas(self):
        for plataforma in self.grupo_plataformas:
            plataforma.draw(self.pantalla_principal)

    def crear_enemigos(self):
        cantidad_enemigos = self.configuracion_nivel.get("cantidad_enemigos")
        for _ in range(1, cantidad_enemigos + 1):
            valor_x = self.enemigo.get("x")
            vaolr_y = self.enemigo.get("y")
            x = random.randint(valor_x["valor_x_1"], valor_x["valor_x_2"])
            y = vaolr_y["valor_y_1"] - vaolr_y["valor_y_2"]
            self.aliens = Enemigo(self.enemigo.get("enemigo_der"), self.enemigo.get("enemigo_izq"), x, y)
            self.grupo_enemigos.add(self.aliens)
        self.grupo_sprites.add(self.grupo_enemigos)

    def mostrar_enemigos(self):
        for enemigo in self.grupo_enemigos:
            enemigo.draw(self.pantalla_principal)

    def crear_objetivos(self):
        cantidad_objetivos = self.configuracion_nivel.get("cantidad_objetivos")
        if self.objetivos:
            imagen = self.objetivos.get("imagen")
            ancho = self.objetivos.get("ancho")
            alto = self.objetivos.get("alto")
            for i in range(1, cantidad_objetivos + 1):
                x = self.objetivos[f"objetivo_{i}"]["x"]
                y = self.objetivos[f"objetivo_{i}"]["y"]
                objetivo = Huevo(imagen, x, y, ancho, alto)
                self.grupo_objetivos.add(objetivo)
        self.grupo_sprites.add(self.grupo_objetivos)

    def mostrar_objetivos(self):
        for objetivo in self.grupo_objetivos:
            objetivo.draw(self.pantalla_principal)

    def crear_energias(self):
        cantidad_energias = self.configuracion_nivel.get("cantidad_energia")
        if self.energia:
            imagen = self.energia.get("imagen")
            ancho = self.energia.get("ancho")
            alto = self.energia.get("alto")
            for i in range(1, cantidad_energias + 1):
                x = self.energia[f"energia_{i}"]["x"]
                y = self.energia[f"energia_{i}"]["y"]
                energia = Energia(imagen, x, y, ancho, alto)
                self.grupo_energias.add(energia)
        self.grupo_sprites.add(self.grupo_energias)

    def mostrar_energias(self):
        for energia in self.grupo_energias:
            energia.draw(self.pantalla_principal)

    def crear_trampas(self):
        cantidad_trampas = self.configuracion_nivel.get("cantidad_trampas")
        imagen = self.trampas.get("imagen")
        if len(self.grupo_trampas) == 0:
            for i in range(1, cantidad_trampas + 1):
                valor_x = self.trampas.get("x")
                valor_y = self.trampas.get("y")
                x = random.randint(valor_x["valor_x_1"], valor_x["valor_x_2"])
                y = random.randint(valor_y["valor_y_1"], valor_y["valor_y_2"])
                trampa = Asteroide(imagen, (x, y), VELOCIDAD_ASTEROIDE)
                self.grupo_trampas.add(trampa)
        self.grupo_sprites.add(self.grupo_trampas)

    def mostrar_trampas(self):
        for trampa in self.grupo_trampas:
            trampa.draw(self.pantalla_principal)

    def crear_vidas(self):
        for vida in self.grupo_vidas:
            vida.kill()
        if isinstance(self.jugador.vidas, int):
            for i in range(1, self.jugador.vidas + 1):
                x = (ANCHO -(20 * self.jugador.vidas)) // 2 + i * 30
                y = 25
                vida = Vida(x, y)
                self.grupo_vidas.add(vida) 


    def mostrar_vidas(self):
        for vida in self.grupo_vidas:
            vida.draw(self.pantalla_principal)

    def cargar_recursos(self):
        #Configuro el nivel con los datos del json
        self.imagen_nivel = self.configuracion_nivel.get("fondo_pantalla")
        self.imagen_fondo = pg.transform.scale(pg.image.load(self.imagen_nivel), (ANCHO, ALTO))
        self.musica_fondo = pg.mixer.music.load(self.configuracion_nivel.get("musica_fondo"))

    
    def update(self):
        self.mostrar_enemigos()
        self.mostrar_plataformas()
        self.mostrar_objetivos()
        self.mostrar_energias()
        self.crear_vidas()
        self.crear_trampas()
        self.mostrar_vidas()
        self.grupo_trampas.update()
        self.mostrar_trampas()
        self.grupo_sprites.draw(self.pantalla)

    def inicializar_nivel(self):
        
        self.cargar_recursos()

        #Cargo plataformas
        self.crear_plataformas()
        self.mostrar_plataformas()

        #Cargo enemigos
        self.crear_enemigos()
        self.mostrar_enemigos()

        #Cargar objetivos
        self.crear_objetivos()
        self.mostrar_objetivos()

        #Cargar energias
        self.crear_energias()
        self.mostrar_energias()

        #Cargar trampas
        self.crear_trampas()
        self.mostrar_trampas()

        #Cargar Vidas
        self.crear_vidas()
        self.mostrar_vidas()



