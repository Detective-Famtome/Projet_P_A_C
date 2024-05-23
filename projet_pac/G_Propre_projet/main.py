import pygame
import os

# main program of our own first game ''

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1920, 1080)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Not any point and click")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Paths to images
bg_img_path = "projet_pac\\G_Propre_projet\\images\\fonds\\menu.jpg"
esc_img_path = "images\\boutons\\keyboard_escape_outline.png"
to_quit_img_path = "images\\boutons\\to_quit.png"
# Load images

if not os.path.exists(bg_img_path):
    print(f"Error: The file '{bg_img_path}' does not exist.")
    pygame.quit()
    exit()

if not os.path.exists(esc_img_path):
    print(f"Error: The file '{esc_img_path}' does not exist.")
    pygame.quit()
    exit()

if not os.path.exists(to_quit_img_path):
    print(f"Error: The file '{to_quit_img_path}' does not exist.")
    pygame.quit()
    exit()

bg_img = pygame.image.load(bg_img_path)
esc_img = pygame.image.load(esc_img_path)
to_quit_img = pygame.image.load(to_quit_img_path)

# ------------------------------------------------------------------------------------------------------- Main Program Loop ----------------------------------------------------------------------------------------------

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    screen.blit(bg_img, (0, 0))  # Draw the background image
    screen.blit(esc_img, (10, 10))  # Draw the esc image at position (100, 100)
    screen.blit(to_quit_img, (50, 10))

    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()