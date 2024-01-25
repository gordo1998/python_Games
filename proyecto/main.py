import pygame
import random
from clases.Prueba import Prueba
from clases.button import Button
pygame.init()
#Configuración de la pantalla principal
ancho_pantalla = 800
alto_pantalla = 400
screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Ovni")
clock = pygame.time.Clock()
hoa = Prueba()
hoa.saludar()





#IMAGENES
#Fondo
fondo = pygame.image.load("imagenes/diseño fondo/disenyo1.jpg").convert_alpha()
fondo = pygame.transform.rotozoom(fondo, 0, 1.5)
fondo_rect = fondo.get_rect(topleft = (-20, 15))
#Nave espacial
nave = pygame.image.load("imagenes/diseños nave/ovni.png").convert_alpha()
nave_rect = nave.get_rect(midbottom = (ancho_pantalla / 2, alto_pantalla / 2))
#Barriles
barril = pygame.image.load("imagenes/diseño barriles/petroleo.png").convert_alpha()

#Barra de estado
# Conformada por dos rectangulos
#El primero es hueco

# 
#
#Variable de estado del juego 
running = True

#Variables de movimiento
estado_movimiento = 0

#Variable velocidad
velocidad_nave = 2

#Variable para el contador
contador_barriles = 0
contenedor_coor_x = ancho_pantalla - 335
contenedor_coor_y = 30
contenedor_ancho = 300
contenedor_alto = 35
game_running = False
alpha = 100

#numero barra estado
font = pygame.font.Font("fuentes/alien.ttf", 30)

#Sonidos
#nave
sonido_nave = pygame.mixer.Sound("sonidos/ovni/ovnilong.mp3")
sonido_nave.set_volume(0.5)
sonido_item_recolect = pygame.mixer.Sound("sonidos/ítems/recolect.item.mp3")
music_game = pygame.mixer.Sound("musica/musicagame.mp3")

# Pantalla start
imagen_start = pygame.image.load("imagenes/diseño fondo/Spaceship.png")
imagen_start = pygame.transform.rotozoom(imagen_start, 0, 0.3)
imagen_start_rec = imagen_start.get_rect(center = (ancho_pantalla / 2, alto_pantalla / 2 - 70))

aumentar_texto = 5
fuente_txt_start = pygame.font.Font("fuentes/PantoufleDEMO-Regular.otf", 20)

botonStart = Button("Start", 200, 50, (ancho_pantalla / 2 - 200 / 2, 250), fuente_txt_start, screen)
botonConf = Button("Configuracion", 200, 50, (ancho_pantalla / 2 - 200 / 2, 320), fuente_txt_start, screen)
# textos_start_rect = [textos_start[0].get_rect(center = (ancho_pantalla / 2, alto_pantalla / 2 + 50)),
#                      textos_start[1].get_rect(center = (ancho_pantalla / 2, alto_pantalla / 2 + 80))]

#Game over
sound_game_over = pygame.mixer.Sound("sonidos/game_over/game_over.mp3")

#Variables de intro del juego
modo_juego = 2

def pintar_limites(screen, ancho_pantalla, alto_pantalla):
    # Dibujando los límites
    # Limite superior
    pygame.draw.rect(screen, "#A1A1A1", (0, 0, ancho_pantalla, 25))
    # Limite inferior
    pygame.draw.rect(screen, "#A1A1A1", (0, alto_pantalla - 25, ancho_pantalla, 25))
    # Limite izquierdo
    pygame.draw.rect(screen,"#A1A1A1", (0, 0, 25, alto_pantalla))
    # Limite derecho
    pygame.draw.rect(screen, "#A1A1A1", (ancho_pantalla - 25, 0, 25, alto_pantalla))

def movimiento_nave(estado_movimiento, nave_rect, velocidad_nave):
    #estado_movimiento = 0
    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_a] or estado_movimiento == 1:
        nave_rect.x -= velocidad_nave 
        estado_movimiento = 1
    if tecla[pygame.K_d] or estado_movimiento == 2:
        nave_rect.x += velocidad_nave
        estado_movimiento = 2
    if tecla[pygame.K_w] or estado_movimiento == 3:
        nave_rect.y -= velocidad_nave
        estado_movimiento = 3
    if tecla[pygame.K_s] or estado_movimiento == 4:
        nave_rect.y += velocidad_nave
        estado_movimiento = 4
    return estado_movimiento

def muerte_nave(nave_rect, game_running):
    if nave_rect.x <= 25:
        game_running = False
    if nave_rect.x >= (ancho_pantalla - nave_rect.width) - 25:
        game_running = False
    if nave_rect.y <= 25:
        game_running = False
    if nave_rect.y >= (alto_pantalla - nave_rect.height):
        game_running = False
    
    return game_running

def coordenadas_barril_x():
    return random.randint(30, ancho_pantalla - 30)

def coordenadas_barril_y():
    return random.randint(50, alto_pantalla - 30)

def imprimir_naveYfondo(fondo, fondo_rect, nave, nave_rect):
    #Imprimiendo el fondo
    screen.blit(fondo, fondo_rect)
    #Imprimir la nave
    screen.blit(nave, nave_rect)

def empezarSonidoNave():
    sound_active = False
    key = pygame.key.get_pressed()
    if key[pygame.K_a] or key[pygame.K_d] or key[pygame.K_w] or key[pygame.K_s]:
        sound_active = True
    return sound_active


        
barril_rect = barril.get_rect(midbottom = (coordenadas_barril_x(), coordenadas_barril_y()))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_running = True
    
    if game_running:
        if empezarSonidoNave():
            if pygame.mixer.get_busy() == False:
                sonido_nave.play()
        
        #NO FUNCIONA BIEN
        # if pygame.mixer.get_busy() == True:
        #     music_game.play()
        
        imprimir_naveYfondo(fondo, fondo_rect, nave, nave_rect)
    
        if nave_rect.colliderect(barril_rect):
            sonido_item_recolect.play()

            barril_rect = barril.get_rect(midbottom = (coordenadas_barril_x(), coordenadas_barril_y()))
            velocidad_nave += 0.5
            contador_barriles += 30
            if contador_barriles >= 300:
                game_running = False

            numero = contador_barriles /contenedor_ancho * 100
            letras = font.render(f"{numero}%", False, "white")
            barra = pygame.transform.scale(barra, (contador_barriles, contenedor_alto))
        else:
            screen.blit(barril, barril_rect)
        pintar_limites(screen, ancho_pantalla, alto_pantalla)

        #imprimir_contador(alpha, probando)
        
        estado_movimiento =  movimiento_nave(estado_movimiento, nave_rect, velocidad_nave)
        game_running = muerte_nave(nave_rect, game_running)
        screen.blit(barra, barra_rect)
        screen.blit(letras, texto_rect)
        barra.set_alpha(alpha)
        pygame.draw.rect(screen, "white", (contenedor_coor_x, contenedor_coor_y, contenedor_ancho, contenedor_alto), 1)
    else:
        #Tiene que haber aquí la historia. Aquí empezará todo, por lo que debe haber una variable 
        sonido_nave.stop()
        screen.blit(fondo, fondo_rect)
        
        screen.blit(imagen_start, imagen_start_rec)
        pygame.draw.rect(screen, "#218B13", (200, 230, 400, 150), 0, 10)
        botonStart.draw()
        botonConf.draw()
        game_running = botonStart.check_click()
        botonConf.check_click()
        # key_txt = pygame.key.get_pressed()
        # if key_txt[pygame.K_w]:
        #     textos_start[1]

        nave_rect.x = ancho_pantalla / 2
        nave_rect.y = alto_pantalla / 2
        velocidad_nave = 2
        estado_movimiento = 0
        contador_barriles = 0
        numero = contador_barriles
        letras = font.render(f"{numero}%", False, "white")
        
        texto_rect = letras.get_rect(center = (contenedor_coor_x + contenedor_ancho / 2, contenedor_coor_y + contenedor_alto / 2))
        barra = pygame.image.load("imagenes/barraestadotres.png").convert_alpha()
        barra_rect = barra.get_rect(topleft = (contenedor_coor_x, contenedor_coor_y))
        
        

    

    pygame.display.flip()

    clock.tick(60)


print(contador_barriles / 30)
pygame.quit()

