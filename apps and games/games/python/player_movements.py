import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player Movement Test")

# Colors
WHITE = (200, 200, 200)
BLUE = (20, 20, 100)
GREEN = (20, 100, 20)
RED = (200, 20, 20)

# Player properties
player_radius = 25
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 2 * player_radius
player_dx = 0
player_dy = 0
gravity = 0.8
jump_force = -15
on_ground = False

# Main game loop
running = True
while running:
    screen.fill(BLUE)  # Set background color

    # Draw green platform
    pygame.draw.rect(screen, GREEN, (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))

    # Draw player
    pygame.draw.circle(screen, RED, (player_x, player_y), player_radius)

    # Display controls
    font = pygame.font.Font(None, 36)
    text = font.render("Use arrow keys to move and jump", True, WHITE)
    screen.blit(text, (10, 10))

    # Update player position
    player_dy += gravity
    player_y += player_dy
    if player_y >= SCREEN_HEIGHT - 50 - player_radius:  # Check collision with ground
        player_y = SCREEN_HEIGHT - 50 - player_radius
        player_dy = 0
        on_ground = True
    else:
        on_ground = False

    player_x += player_dx

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_dx = -5
            elif event.key == pygame.K_RIGHT:
                player_dx = 5
            elif event.key == pygame.K_UP and on_ground:
                player_dy = jump_force

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_dx = 0

    # Bound player within the screen
    if player_x <= player_radius:
        player_x = player_radius
    elif player_x >= SCREEN_WIDTH - player_radius:
        player_x = SCREEN_WIDTH - player_radius

    # Refresh screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limit frame rate to 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()
