import pygame
from sys import exit

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Runner')

# set up clock
clock = pygame.time.Clock()

# Set up the background ----------------------------------------------------------------------------------------------------------
background = pygame.image.load('backgrounds/marioBackground.jpg').convert()
# Change the size of the background
scaling_factor = 1.5  # Adjust this value to scale the sprite up (e.g., 1.5 for 150% size) or down (e.g., 0.8 for 80% size)
# Get the current dimensions of the sprite
original_width, original_height = background.get_size()
# Calculate the new dimensions based on the scaling factor
new_width = int(original_width * scaling_factor)
new_height = int(original_height * scaling_factor)
# Resize the sprite image
background = pygame.transform.scale(background, (new_width, new_height))
# --------------------------------------------------------------------------------------------------------------------------------

# Set up mario ----------------------------------------------------------------------------------------------------------
mario = pygame.image.load('sprites/mario1.png').convert_alpha()
# Change the size of the mario
scaling_factor = 0.1  # Adjust this value to scale the sprite up (e.g., 1.5 for 150% size) or down (e.g., 0.8 for 80% size)
# Get the current dimensions of the sprite
original_width, original_height = mario.get_size()
# Calculate the new dimensions based on the scaling factor
new_width = int(original_width * scaling_factor)
new_height = int(original_height * scaling_factor)
# Resize the sprite image
mario = pygame.transform.scale(mario, (new_width, new_height))

mario_rect = mario.get_rect(bottomleft=(0, 435))

gravity = 1
on_ground = False  # Variable to track if Mario is on the ground

# create text
test_font = pygame.font.Font(None, 50)
text_surface = test_font.render('My Game', False, 'Black')

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYUP:
            if on_ground:
                gravity = -20  # Only allow jumping when on the ground

    screen.blit(background, (0, 0))
    screen.blit(text_surface, (350, 250))
    screen.blit(mario, mario_rect.topleft)

    mario_rect.x += 4
    if mario_rect.right > 1000:
        mario_rect.left = -new_width

    gravity += 1
    mario_rect.y += gravity

    if mario_rect.bottom >= 435:
        mario_rect.bottom = 435
        on_ground = True  # Mario is on the ground
    else:
        on_ground = False  # Mario is not on the ground

    # Update game state
    pygame.display.update()
    clock.tick(60)
