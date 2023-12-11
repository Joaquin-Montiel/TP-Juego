import pygame as pg

class Button():
    def __init__(self, image, pos, text_input, font, base_color, color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.color = base_color, color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, pantalla):
        if self.image is not None:
            pantalla.blit(self.image, self.rect)
        pantalla.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1]in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def handle_click(self, position):
        if self.checkForInput(position):
            print("Boton clickeado: " + self.text_input)

            if pg.mixer.music.get_busy():
                pg.mixer_music.pause()
            else:
                pg.mixer.music.unpause()