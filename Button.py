import pygame

class Button:
    def __init__(self, screen, rel_x, rel_y, image, scale):
        self.screen = screen
        self.image_original = image
        self.scale = scale
        self.rel_x = rel_x  
        self.rel_y = rel_y

        self.update_position()

    def update_position(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        width = self.image_original.get_width()
        height = self.image_original.get_height()
        self.image = pygame.transform.scale(self.image_original, (int(width * self.scale), int(height * self.scale)))

        button_width = self.image.get_width()
        button_height = self.image.get_height()

        abs_x = int(self.rel_x * screen_width - button_width // 2)
        abs_y = int(self.rel_y * screen_height - button_height // 2)

        self.rect = self.image.get_rect(topleft=(abs_x, abs_y))

    def draw(self):
        self.update_position()
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
