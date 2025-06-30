import pygame
from define import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 30)
        self.buttons = [
            ("DFS", pygame.Rect(400, 150, 200, 50)),
            ("BFS", pygame.Rect(400, 220, 200, 50)),
            ("UCS", pygame.Rect(400, 290, 200, 50)),
            ("A*", pygame.Rect(400, 360, 200, 50))
        ]

    def draw(self):
        self.screen.fill(WHITE)
        title_surface = self.font.render("Your Option :", True, BLACK)
        self.screen.blit(title_surface, (400, 80))

        mouse_pos = pygame.mouse.get_pos()
        hand_cursor_needed = False

        for label, rect in self.buttons:
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, forest_green, rect)
                hand_cursor_needed = True
            else:
                pygame.draw.rect(self.screen, BLUE, rect)
            text = self.font.render(label, True, WHITE)
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)

        if hand_cursor_needed:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

    def get_algorithm_choice(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for label, rect in self.buttons:
                        if rect.collidepoint(event.pos):
                            return label