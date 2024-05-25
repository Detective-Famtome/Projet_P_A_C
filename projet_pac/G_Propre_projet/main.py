import pygame
import scripts

# main program of our own first game ''

# Define some colors
BLACK, WHITE, GREEN, RED = scripts.defs.get_color()

pygame.init()

screen, clock = scripts.defs.setup_pygame()

# Loop until the user clicks the close button.
done = False

bg_img, esc_img, to_quit_img = scripts.def.imgs()
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
    screen.blit(bg_img, (0, 0)
    screen.blit(bg_img, (0, 0))  # Draw the background image
    screen.blit(esc_img, (10, 10))  # Draw the esc image at position (100, 100)
    screen.blit(to_quit_img, (50, 10))

    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    pygame.time.Clock().tick(60)
 
# Close the window and quit.
pygame.quit()
