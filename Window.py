import pygame
from define import *

class Window():
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Rush Hour Puzzle - Zoom/Pan")
        programIcon = pygame.image.load("RUSHHOUR.png")
        pygame.display.set_icon(programIcon)
        
    def fill(self, color):
        """Fill the screen with a color."""
        self.screen.fill(color)
