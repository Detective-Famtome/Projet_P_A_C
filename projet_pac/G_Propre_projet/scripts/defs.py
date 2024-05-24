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