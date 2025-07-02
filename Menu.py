import pygame
from define import *
from KeyboardOperation import traffic_sound

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
        #self.labels = ["DFS", "BFS", "UCS", "A*"]
        self.labels = ["DFS", "BFS", "UCS", "A*", "Back"]
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
        self.draw_decorations() # Draw

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

    def draw_decorations(self):
        # List of cars with positions and colors
        cars = [
            {"x": 50, "y": self.screen.get_height() - 100, "color": RED},
            {"x": 150, "y": self.screen.get_height() - 100, "color": BLUE},
            {"x": 250, "y": self.screen.get_height() - 100, "color": YELLOW},
            {"x": 350, "y": self.screen.get_height() - 100, "color": GREEN}
        ]

        # Draw each car
        for car in cars:
            pygame.draw.rect(self.screen, car["color"], (car["x"], car["y"], 80, 40))  # Car body
            pygame.draw.circle(self.screen, BLACK, (car["x"] + 20, car["y"] + 40), 10)  # Left wheel
            pygame.draw.circle(self.screen, BLACK, (car["x"] + 60, car["y"] + 40), 10)  # Right wheel
            pygame.draw.rect(self.screen, YELLOW, (car["x"] + 10, car["y"] + 5, 20, 15))  # Car window

        # List of houses with positions, styles, and colors
        house_spacing = 40  # Space between houses vertically
        houses = [
            # Left side houses
            {
                "x": 20,
                "y": 150,
                "body_color": GRAY,
                "roof_color": RED,
                "roof_type": "triangle",
                "width": 100,
                "height": 80,
                "windows": [{"x_offset": 20, "y_offset": 20, "size": 20}],
                "door": {"x_offset": 70, "y_offset": 50, "width": 20, "height": 30}
            },
            {
                "x": 20,
                "y": 150 + 80 + house_spacing + 40,  # Account for house height + roof height + spacing
                "body_color": YELLOW,
                "roof_color": BLUE,
                "roof_type": "flat",
                "width": 80,
                "height": 100,
                "windows": [{"x_offset": 15, "y_offset": 20, "size": 15}, {"x_offset": 50, "y_offset": 20, "size": 15}],
                "door": {"x_offset": 30, "y_offset": 70, "width": 20, "height": 30}
            },
            {
                "x": 20,
                "y": 150 + 80 + house_spacing + 40 + 100 + house_spacing + 20,  # Account for previous houses + roofs
                "body_color": GREEN,
                "roof_color": RED,
                "roof_type": "triangle",
                "width": 120,
                "height": 70,
                "windows": [{"x_offset": 30, "y_offset": 15, "size": 30}],
                "door": {"x_offset": 80, "y_offset": 40, "width": 20, "height": 30},
                "chimney": {"x_offset": 90, "y_offset": -20, "width": 10, "height": 20}
            },
            # Right side houses
            {
                "x": self.screen.get_width() - 120,
                "y": 150,
                "body_color": GRAY,
                "roof_color": RED,
                "roof_type": "triangle",
                "width": 100,
                "height": 80,
                "windows": [{"x_offset": 20, "y_offset": 20, "size": 20}],
                "door": {"x_offset": 70, "y_offset": 50, "width": 20, "height": 30}
            },
            {
                "x": self.screen.get_width() - 100,
                "y": 150 + 80 + house_spacing + 40,  # Account for house height + roof height + spacing
                "body_color": YELLOW,
                "roof_color": BLUE,
                "roof_type": "flat",
                "width": 80,
                "height": 100,
                "windows": [{"x_offset": 15, "y_offset": 20, "size": 15}, {"x_offset": 50, "y_offset": 20, "size": 15}],
                "door": {"x_offset": 30, "y_offset": 70, "width": 20, "height": 30}
            },
            {
                "x": self.screen.get_width() - 140,
                "y": 150 + 80 + house_spacing + 40 + 100 + house_spacing + 20,  # Account for previous houses + roofs
                "body_color": GREEN,
                "roof_color": RED,
                "roof_type": "triangle",
                "width": 120,
                "height": 70,
                "windows": [{"x_offset": 30, "y_offset": 15, "size": 30}],
                "door": {"x_offset": 80, "y_offset": 40, "width": 20, "height": 30},
                "chimney": {"x_offset": 90, "y_offset": -20, "width": 10, "height": 20}
            }
        ]

        # Draw each house
        for house in houses:
            # Draw house body
            pygame.draw.rect(self.screen, house["body_color"], (house["x"], house["y"], house["width"], house["height"]))
            # Draw roof
            if house["roof_type"] == "triangle":
                pygame.draw.polygon(self.screen, house["roof_color"], 
                    [(house["x"], house["y"]), 
                     (house["x"] + house["width"] // 2, house["y"] - 40), 
                     (house["x"] + house["width"], house["y"])])
            else:  # Flat roof
                pygame.draw.rect(self.screen, house["roof_color"], (house["x"], house["y"] - 20, house["width"], 20))
            # Draw windows
            for window in house["windows"]:
                pygame.draw.rect(self.screen, YELLOW, 
                    (house["x"] + window["x_offset"], house["y"] + window["y_offset"], window["size"], window["size"]))
            # Draw door
            pygame.draw.rect(self.screen, BLUE, 
                (house["x"] + house["door"]["x_offset"], house["y"] + house["door"]["y_offset"], 
                 house["door"]["width"], house["door"]["height"]))
            # Draw chimney if present
            if "chimney" in house:
                pygame.draw.rect(self.screen, BLACK, 
                    (house["x"] + house["chimney"]["x_offset"], house["y"] + house["chimney"]["y_offset"], 
                     house["chimney"]["width"], house["chimney"]["height"]))

        # Draw a traffic light
        traffic_light_x, traffic_light_y = self.screen.get_width() - 100, self.screen.get_height() - 150
        pygame.draw.rect(self.screen, BLACK, (traffic_light_x, traffic_light_y, 30, 90))  # Traffic light body
        pygame.draw.circle(self.screen, RED, (traffic_light_x + 15, traffic_light_y + 15), 10)  # Red light
        pygame.draw.circle(self.screen, YELLOW, (traffic_light_x + 15, traffic_light_y + 45), 10)  # Yellow light
        pygame.draw.circle(self.screen, GREEN, (traffic_light_x + 15, traffic_light_y + 75), 10)  # Green light
        pygame.draw.rect(self.screen, GRAY, (traffic_light_x + 10, traffic_light_y + 90, 10, 30))  # Pole

        # Draw road lines
        road_y = self.screen.get_height() - 60
        for x in range(0, self.screen.get_width(), 40):
            pygame.draw.rect(self.screen, YELLOW, (x, road_y, 20, 5))  # Dashed road lines
            
    def get_algorithm_choice(self):
        while True:
            self.draw()
            traffic_sound.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    traffic_sound.stop()
                    return None
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    traffic_sound.stop()
                    for label, rect in self.buttons:
                        if rect.collidepoint(event.pos):
                            if label == "Back":
                                return "BACK"
                            return label
     