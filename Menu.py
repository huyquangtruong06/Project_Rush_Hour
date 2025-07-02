import pygame
from define import *

class Menu:
    def __init__(self, screen, levels=None):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 30)
        self.levels = levels 

        '''
        self.buttons = [
            ("DFS", pygame.Rect(100, 150, 200, 50)),
            ("BFS", pygame.Rect(100, 220, 200, 50)),
            ("UCS", pygame.Rect(100, 290, 200, 50)),
            ("A*", pygame.Rect(100, 360, 200, 50))
        ]'''
        self.button_width = 200
        self.button_height = 50
        self.spacing = 20
        self.labels = ["DFS", "BFS", "UCS", "A*"]
        self.buttons = []

    def update_buttons(self):
        screen_width, screen_height = self.screen.get_size()
        total_height = len(self.labels) * self.button_height + (len(self.labels) - 1) * self.spacing
        start_y = (screen_height - total_height) // 2
        start_x = (screen_width - self.button_width) // 2

        self.buttons = []
        for i, label in enumerate(self.labels):
            rect = pygame.Rect(start_x, start_y + i * (self.button_height + self.spacing), self.button_width, self.button_height)
            self.buttons.append((label, rect))

    def draw(self):
        self.screen.fill(WHITE)
        '''
        title_surface = self.font.render("Your Option :", True, BLACK)
        self.screen.blit(title_surface, (100, 80))'''
        self.update_buttons()

        title_surface = self.font.render(f"Your Option for Level {self.levels + 1} :", True, BLACK)
        title_rect = title_surface.get_rect(center=(self.screen.get_width() // 2, 80))
        self.screen.blit(title_surface, title_rect)

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

        instructions = [
            "Level 5 and above should be not used with UCS algorithm (it will take a lot of time).",
        ]

        font = pygame.font.SysFont('Arial', 16)
        for i, text in enumerate(instructions):
            text_surface = font.render(text, True, RED)
            self.screen.blit(text_surface, (10, 10 + i * 20))
        pygame.display.flip()


    def get_algorithm_choice(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for label, rect in self.buttons:
                        if rect.collidepoint(event.pos):
                            return label
     