import pygame
import os

def get_color():
    """Donne les couleurs sous format de tuple (r, g, b)"""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    return BLACK, WHITE, GREEN, RED

def setup_pygame():
    """Lignes de commandes pour setup pygame"""
    # Set the width and height of the
    screen [width, height]
    size = (1920, 1080)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Not any point and click")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    return screen, clock

def imgs():
    # Paths to images
    bg_img_path = "projet_pac/G_Propre_projet/images/fonds/menu.jpg"
    esc_img_path = "projet_pac/G_Propre_projet/images/boutons/keyboard_escape_outline.png"
    to_quit_img_path = "projet_pac/G_Propre_projet/images/boutons/to_quit.png"
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
    return bg_img, esc_img, to_quit_img