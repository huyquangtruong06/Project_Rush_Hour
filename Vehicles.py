from enum import IntEnum
from define import *
import pygame
import sys

class VehicleTypes(IntEnum):
    car = 2
    truck = 3

class Orientations(IntEnum):
    horizontal = 0
    vertical = 1

class Vehicle:
    def __init__(self, id, position, orientation, vtype, color_idx):
        self.id = id
        self.position = position
        self.orientation = orientation
        self.vType = vtype
        self.color = COLORS[color_idx % len(COLORS)]

    def draw(self, surface, cell_size, offset_x, offset_y):
        x_pos = offset_x + self.position[0] * cell_size
        y_pos = offset_y + self.position[1] * cell_size

        if self.orientation == Orientations.horizontal:
            width = int(self.vType) * cell_size
            height = cell_size
        else:  # vertical
            width = cell_size
            height = int(self.vType) * cell_size

        pygame.draw.rect(surface, self.color, (x_pos, y_pos, width, height))
        pygame.draw.rect(surface, BLACK, (x_pos, y_pos, width, height), 2)  # Viền

        # Display ID if it enough big.
        if cell_size > 50:
            font_size = max(12, int(cell_size * 0.4))
            font = pygame.font.SysFont('Arial', font_size)
            text = font.render(self.id, True, BLACK)
            text_rect = text.get_rect(center=(x_pos + width // 2, y_pos + height // 2))
            surface.blit(text, text_rect)


    def coveredUnits(self):
        """Returns list of all locations covered by this vehicle."""
        dx = int(self.orientation == Orientations.horizontal)
        dy = int(self.orientation == Orientations.vertical)
        return [(self.position[0] + dx * i, self.position[1] + dy * i) for i in range(int(self.vType))]

    def __str__(self):
        orientation_txt = "Horizontal" if self.orientation == Orientations.horizontal else "Vertical"
        type_txt = "Car" if self.vType == VehicleTypes.car else "Truck"
        pos = str(self.coveredUnits())
        return f"{self.id}: {orientation_txt} {type_txt} at ({self.position[0]},{self.position[1]}) covering {pos}"


