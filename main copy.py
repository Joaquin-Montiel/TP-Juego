# import pygame
# import sys

# #Inicializo pygame
# pygame.init()

# #Configuro la ventana del juego
# WIDTH = 800
# HEIGHT  = 600
# RUTA_FONDO = r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\fondo.jpg'
# RUTA_DER = r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Still.png'
# RUTA_IZ = r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Still(iz).png'

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Juego con Dinosaurios")

# #Cargar imagen de fondo
# fondo = pygame.image.load(RUTA_FONDO)
# fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))

# #Cargar sprite del dinosaurio
# dinosaurio_der = pygame.image.load(RUTA_DER)
# dinosaurio_iz = pygame.image.load(RUTA_IZ)

# dinosaurio_camina_derecha = [
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(1).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(2).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(3).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(4).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(5).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(6).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(7).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(8).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(9).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(10).png')
# ]

# dinosaurio_camina_izquierda = [
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(1)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(2)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(3)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(4)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(5)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(6)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(7)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(8)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(9)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Walk\Walk(10)iz.png')
# ]

# dinosaurio_salta_derecha = [
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(1).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(2).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(3).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(4).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(5).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(6).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(7).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(8).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(9).png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(10).png')
# ]
# dinosaurio_salta_izquierda = [
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(1)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(2)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(3)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(4)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(5)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(6)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(7)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(8)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(9)iz.png'),
#     pygame.image.load(r'C:\Users\joaqu\OneDrive\Desktop\Joaquin Montiel-TP Juego\sprites_juego\Jump\Jump(10)iz.png')
# ]

# # Cargar sprite del dinosaurio
# dinosaurio_rect = dinosaurio_camina_derecha[0].get_rect()

# # Inicializar la posición en el centro de la pantalla
# dinosaurio_rect.midbottom = (WIDTH // 2, HEIGHT  - 10)

# # Elegir dirección inicial
# direccion_actual = "derecha"
# sprite_actuales = dinosaurio_camina_derecha

# #Indice del sprite
# indice_sprite = 0

# #Velocidad del dinosaurio
# velocidad = 2

# #Variables de salto
# en_el_aire = False
# velocidad_salto = -10
# gravedad = 1

# #Bucle principal
# clock = pygame.time.Clock()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     teclas = pygame.key.get_pressed()
#     if teclas[pygame.K_LEFT] and dinosaurio_rect.left >= 0:
#         dinosaurio_rect.x -= velocidad
#         # Cambiar dirección a la izquierda
#         sprite_actuales = dinosaurio_salta_izquierda if en_el_aire else dinosaurio_camina_izquierda  
#         direccion_actual = "izquierda"
#     elif teclas[pygame.K_RIGHT] and dinosaurio_rect.right <= WIDTH:
#         dinosaurio_rect.x += velocidad
#         # Cambiar dirección a la derecha
#         sprite_actuales = dinosaurio_salta_derecha if en_el_aire else dinosaurio_camina_derecha  
#         direccion_actual = "derecha"
#     elif teclas[pygame.K_SPACE] and not en_el_aire:
#         en_el_aire = True
#     else:
#         # Si no se están presionando teclas, el dinosaurio se queda quieto
#         if direccion_actual == "derecha":
#             sprite_actuales = [dinosaurio_der]
#         else:
#             sprite_actuales = [dinosaurio_iz]

#     # Aplicar gravedad si está en el aire
#     if en_el_aire:
#         dinosaurio_rect.y += velocidad_salto
#         velocidad_salto += gravedad
#         # Verificar si ha vuelto al suelo
#         if dinosaurio_rect.bottom >= HEIGHT - 10:
#             print("Hola dino")
#             en_el_aire = False
#             velocidad_salto = 0
#             dinosaurio_rect.bottom = HEIGHT - 10
#             # Cambiar a sprite caminando dependiendo de la dirección
#             sprite_actuales = [dinosaurio_der] if direccion_actual == "derecha" else [dinosaurio_iz]
#     else:
#         en_el_aire = False


#     #Dibujar en pantalla
#     screen.blit(fondo, (0, 0))

#     # Alternar entre sprites para animar el movimiento
#     if 0 <= indice_sprite < len(sprite_actuales):
#         sprite_actual = sprite_actuales[indice_sprite]
#         screen.blit(sprite_actual, dinosaurio_rect)
#     else:
#         # Si el índice está fuera de rango, se reinicia
#         indice_sprite = 0   


#     # Actualizar el índice del sprite para la siguiente iteración
#     indice_sprite = (indice_sprite + 1) % len(sprite_actuales)

#     # Actualizar pantalla
#     pygame.display.flip()

#     # Añadir un pequeño retardo para controlar la velocidad de la animación
#     clock.tick(20)