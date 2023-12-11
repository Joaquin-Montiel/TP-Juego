import pygame as pg, sys
from Button import Button
from InputBox import InputBox
pg.init()

ANCHO = 800
ALTO = 600
pantalla = pg.display.set_mode((ANCHO, ALTO))
pg.display.set_caption("Menu")

fondo_menu = pg.transform.scale(pg.image.load(r"./sprites_juego\Fondo\fondo_menu.jpg"), (ANCHO, ALTO))

def get_font(tamanio):
    font_path = "./Fonts\ConcertOne-Regular.ttf"
    try:
        font = pg.font.Font(font_path, tamanio)
        return font
    except pg.error:
        print("Error al cargar la fuente.")
        return None

def cambio_nivel(jugador_nombre):
    nivel_seleccionado = None
    title_font = get_font(60)
    level_font = get_font(30)
    level_buttons = [
        Button(image=None, pos=(400, 300), text_input="Nivel 1", font=level_font, base_color="Black",
                color="White"),
        Button(image=None, pos=(400, 345), text_input="Nivel 2", font=level_font, base_color="Black",
                color="White"),
        Button(image=None, pos=(400, 390), text_input="Nivel 3", font=level_font, base_color="Black",
                color="White")
    ]

    while True:
        pantalla.blit(fondo_menu, (0, 0))

        title_text = title_font.render(f"Selecciona un nivel, {jugador_nombre}:", True, "Black")
        title_rect = title_text.get_rect(center=(400, 200))
        pantalla.blit(title_text, title_rect)

        for button in level_buttons:
            button.changeColor(pg.mouse.get_pos())
            button.update(pantalla)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in level_buttons:
                    if button.checkForInput(pg.mouse.get_pos()):
                        nivel_seleccionado = button.text_input
                        print(f"Jugador: {jugador_nombre}, Nivel seleccionado: {nivel_seleccionado}")
                    
                        return  

        pg.display.update()


def play():
    pg.display.set_caption("Play")
    nombre_jugador = ""
    entrada_activa = False
    input_box = InputBox(300, 300, 200, 40, get_font(30))

    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos()

        pantalla.blit(fondo_menu, (0, 0))

        PLAY_TEXT = get_font(60).render("Iniciar Juego", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 200))
        pantalla.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(700, 500), text_input="<- Atras", font=get_font(45),
                            base_color="Black", color="Blue")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(pantalla)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pg.KEYDOWN:
                if entrada_activa:
                    if event.key == pg.K_RETURN:
                        entrada_activa = False
                        jugador_nombre = nombre_jugador
                        nivel_seleccionado = cambio_nivel(jugador_nombre)
                        if nivel_seleccionado is not None:
                            print(f"Jugador: {jugador_nombre}, Nivel seleccionado: {nivel_seleccionado}")
                            return  # Salgo del bucle 
                    elif event.key == pg.K_BACKSPACE:
                        nombre_jugador = nombre_jugador[:-1]
                    else:
                        nombre_jugador += event.unicode
                elif event.key == pg.K_RETURN:
                    entrada_activa = True

            # Verifico si se ha presionado "Enter"
            if input_box.is_enter_pressed(event):
                entrada_activa = False
                jugador_nombre = input_box.text
                nivel_seleccionado = cambio_nivel(jugador_nombre)
                if nivel_seleccionado is not None:
                    print(f"Jugador: {jugador_nombre}, Nivel seleccionado: {nivel_seleccionado}")
                    return  
                
            input_box.handle_event(event)

        pantalla.blit(fondo_menu, (0, 0))

        PLAY_TEXT = get_font(60).render("Iniciar Juego", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 200))
        pantalla.blit(PLAY_TEXT, PLAY_RECT)

        input_box.update()
        input_box.draw(pantalla)

        PLAY_BACK.changeColor(pg.mouse.get_pos())
        PLAY_BACK.update(pantalla)


        pg.display.update()


def options():
    pg.display.set_caption("Options")

    while True:
        OPTIONS_MOUSE_POS = pg.mouse.get_pos()

        pantalla.blit(fondo_menu, (0, 0))

        OPTIONS_TEXT = get_font(45).render("Configuracion", True, "black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 200))
        pantalla.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(700, 500), text_input="<- Atras", font=get_font(45), base_color="Black", 
                            color="Blue")
        

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(pantalla)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pg.display.update()


def main_menu():
    while True:

        pantalla.blit(fondo_menu, (0, 0))
        posicion_mouse = pg.mouse.get_pos()

        menu_texto = get_font(75).render("Menu Principal", True, "Black")
        menu_rect = menu_texto.get_rect(center=(400, 200))

        PLAY_BUTTON = Button(image=pg.image.load(r"./sprites_juego\Fondo\play.png"), pos=(400, 350),
                            text_input="PLAY", font=get_font(25), base_color="Black",color="White")
        OPTIONS_BUTTON = Button(image=pg.image.load(r"./sprites_juego\Fondo\play.png"), pos=(400, 400),
                            text_input="OPTIONS", font=get_font(25), base_color="Black",color="White")
        QUIT_BUTTON = Button(image=pg.image.load(r"./sprites_juego\Fondo\play.png"), pos=(400, 450),
                            text_input="QUIT", font=get_font(25), base_color="Black",color="White")
        
        pantalla.blit(menu_texto, menu_rect)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(posicion_mouse)
            button.update(pantalla)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(posicion_mouse):
                    play()
                if OPTIONS_BUTTON.checkForInput(posicion_mouse):
                    options()
                if QUIT_BUTTON.checkForInput(posicion_mouse):
                    pg.quit()
                    sys.exit()

        pg.display.update()

main_menu()