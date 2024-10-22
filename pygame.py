import pygame
import random

# inicia el juego
pygame.init()

# tamaño de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# colores de todo
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# nombre del juego
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Atrapa la bolita")


clock = pygame.time.Clock()

# jugador
player_width = 100
player_height = 20
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 10

# propiedades bolita
object_width = 30
object_height = 30
object_x = random.randint(0, SCREEN_WIDTH - object_width)
object_y = -object_height
object_speed = 7

# variables
score = 0
missed = 0
max_missed = 5


font = pygame.font.Font(None, 36)

#loop  juego
running = True
while running:
    screen.fill(WHITE)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed
    
    
    object_y += object_speed
    
    # jugador atrapando bola
    if object_y + object_height > player_y:
        if player_x < object_x + object_width and player_x + player_width > object_x:
            score += 1
            object_x = random.randint(0, SCREEN_WIDTH - object_width)
            object_y = -object_height
    
    # resetea el la bolita si se sale
    if object_y > SCREEN_HEIGHT:
        missed += 1
        object_x = random.randint(0, SCREEN_WIDTH - object_width)
        object_y = -object_height
    
    
    if missed >= max_missed:
        running = False
    
    
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
    

    pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))
    
    # muestra los puntos
    score_text = font.render(f"Score: {score}", True, BLACK)
    missed_text = font.render(f"Missed: {missed}/{max_missed}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(missed_text, (10, 50))
    
    
    pygame.display.flip()
    
    clock.tick(60)

#  mensaje de perder
screen.fill(WHITE)
game_over_text = font.render("Game Over", True, RED)
final_score_text = font.render(f"Final Score: {score}", True, BLACK)
screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 30))
screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 10))
pygame.display.flip()

# etiempo pa salir
pygame.time.wait(3000)

# cierra el juego
pygame.quit()
