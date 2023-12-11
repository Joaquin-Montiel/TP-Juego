import pygame as pg

class InputBox:
    def __init__(self, x, y, width, height, font):
        self.rect = pg.Rect(x, y, width, height)
        self.text_color = (0, 0, 0)  # Color del texto (negro)
        self.bg_color = (255, 255, 255, 128)  # Color de fondo con transparencia (blanco, 128 de opacidad)
        self.text = ''
        self.font = font
        self.txt_surface = self.font.render(self.text, True, self.text_color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.active = False
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.text_color)

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, pantalla):
        pg.draw.rect(pantalla, self.bg_color, self.rect, 0)
        pg.draw.rect(pantalla, (0, 0, 0), self.rect, 2)
        pantalla.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def is_enter_pressed(self, event):
        return event.type == pg.KEYDOWN and event.key == pg.K_RETURN