"""Module définition pour main.py"""
import pygame
from scripts import classes


class Butom:
    def __init__(self, pos, size):
        """Classe bouton pour les boutons"""
        self.pos = pos
        self.size = size

    def draw(self):
        """Dessine le bouton sur la feunètttreux"""
        pass
    
    def click(self):
        """Permet que le bouton soit clicable"""
        m_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (self.pos[0] <= m_pos[0] <= self.pos[0] + self.size[0] and
                    self.pos[1] <= m_pos[1] <= self.pos[1] + self.size[1]):
                    return True
        return False
