#pgzero
import random

WIDTH = 750
HEIGHT = 450

TITLE = "Flappy Seal"
FPS = 30

# Objetos del juego
def character():
    global background, Seal_neutron, Seal_up, Seal_down
    background = Actor('background', (WIDTH / 2, HEIGHT / 2))
    Seal_neutron = Actor('Seal_neutron', (105, HEIGHT / 2))
    Seal_up = Actor('Seal_up', (105, HEIGHT / 2))
    Seal_down = Actor('Seal_down', (105, HEIGHT / 2))

# Controlador de animación (empieza con la neutra)
character()
seal = Seal_neutron

# Variables del juego
gravity = 0.4
seal_velocity = 0
game_over = False
score = 0

# Lista de tuberías
pipes = []


def draw():
    screen.clear()
    background.draw()

    # Dibujar tuberías
    for pipe in pipes:
        pipe.draw()

    # Dibujar la foca animada
    seal.draw()

    # Mostrar puntaje
    screen.draw.text("Puntaje: " + str(score // 2), (10, 10), fontsize=35, color="black", background = 'orange')

    if game_over:
        screen.draw.text("Game Over", center=(WIDTH / 2, HEIGHT / 2), fontsize=50, color="red")
        screen.draw.text("Presiona ESPACIO para reiniciar", center=(WIDTH / 2, HEIGHT / 2 + 40), fontsize=25, color="white")


def update(dt):
    global seal_velocity, game_over, score, seal

    if not game_over:
        # Aplicar gravedad
        seal_velocity += gravity
        seal.y += seal_velocity

        # Actualizar animación según movimiento
        if seal_velocity < -1:
            seal.image = 'Seal_up'
        elif seal_velocity > 2:
            seal.image = 'Seal_down'
        else:
            seal.image = 'Seal_neutron'

        # Generar tuberías nuevas
        if len(pipes) == 0 or pipes[-1].x < WIDTH - 200:
            crear_tuberia()

        # Mover tuberías
        for pipe in pipes:
            pipe.x -= 3

        # Eliminar tuberías fuera de la pantalla
        if len(pipes) > 0 and pipes[0].x < -50:
            pipes.pop(0)
            score += 1

        # Colisiones
        #for pipe in pipes:
            #if seal.colliderect(pipe):
                #game_over = True
        
        coll = seal.collidelist(pipes)
        if coll != -1:
            game_over = True

        # Revisar si la foca toca el suelo o el techo
        if seal.y > HEIGHT or seal.y < 0:
            game_over = True


def on_key_down(key):
    global seal_velocity, game_over, score, pipes

    if key == keys.SPACE:
        if game_over:
            # Reiniciar juego
            seal.y = HEIGHT / 2
            seal_velocity = 0
            pipes = []
            score = 0
            game_over = False
        else:
            # Salto
            seal_velocity = -6


def crear_tuberia():
    """Crea un par de tuberías (superior e inferior)"""
    if score < 20:
        altura = random.randint(40, 200)
        altura2 = random.randint(250, 410)
    elif score > 19:
        altura = random.randint(40, 210)
        altura2 = random.randint(240, 410)
    #elif score > 
    # Tubería superior
    pipe_top = Actor('Pipe', (WIDTH, 20), size = (50, altura))
    pipe_top.angle = 180

    # Tubería inferior
    pipe_bottom = Actor('Pipe', (WIDTH, 430), size = (50, altura2))

    pipes.append(pipe_top)
    pipes.append(pipe_bottom)


