from Vehicles import *

class Map:
    def __init__(self, screen):
        self.screen = screen
        self.cell_size = initial_cell_size
        self.offset_x = (WINDOW_WIDTH - GRID_SIZE * self.cell_size) // 2
        self.offset_y = (WINDOW_HEIGHT - GRID_SIZE * self.cell_size) // 2
        
        self.dragging = False
        self.last_mouse_pos = (0, 0)
        
        self.vehicles = []
    
    def draw(self):
        """Draw grid with current size"""
        for row in range(GRID_SIZE + 1):
            pygame.draw.line(
                self.screen, BLACK,
                (self.offset_x, self.offset_y + row * self.cell_size),
                (self.offset_x + GRID_SIZE * self.cell_size, self.offset_y + row * self.cell_size),
                2
            )
        
        for col in range(GRID_SIZE + 1):
            pygame.draw.line(
                self.screen, BLACK,
                (self.offset_x + col * self.cell_size, self.offset_y),
                (self.offset_x + col * self.cell_size, self.offset_y + GRID_SIZE * self.cell_size),
                2
            )
        
        # Draw exit sign
        exit_x = self.offset_x + GRID_SIZE * self.cell_size
        exit_y1 = self.offset_y + 2 * self.cell_size
        exit_y2 = self.offset_y + 3 * self.cell_size
        pygame.draw.line(self.screen, RED, (exit_x, exit_y1), (exit_x + 10, exit_y1), 3)
        pygame.draw.line(self.screen, RED, (exit_x, exit_y2), (exit_x + 10, exit_y2), 3)
        # Display guide.
        font = pygame.font.SysFont('Arial', 16)
        instructions = [
            "Scroll/Pinch to zoom | Drag to pan | R: Reset view",
            f"Zoom: {int((self.cell_size/BASE_CELL_SIZE)*100)}%"
        ]
        
        for i, text in enumerate(instructions):
            text_surface = font.render(text, True, BLACK)
            self.screen.blit(text_surface, (10, 10 + i * 20))
    
    def zoom(self, factor, mouse_pos=None):
        """Zoom in/out with center at mouse position"""
        old_cell_size = self.cell_size
        self.cell_size = min(MAX_CELL_SIZE, max(MIN_CELL_SIZE, int(self.cell_size * factor)))
        
        if mouse_pos:
            # Calculate new offset to keep mouse position on same cell
            mouse_grid_x = (mouse_pos[0] - self.offset_x) / old_cell_size
            mouse_grid_y = (mouse_pos[1] - self.offset_y) / old_cell_size
            
            self.offset_x = mouse_pos[0] - mouse_grid_x * self.cell_size
            self.offset_y = mouse_pos[1] - mouse_grid_y * self.cell_size
    

    def reset_view(self):
       """Reset to default view"""
       self.cell_size = BASE_CELL_SIZE
       self.offset_x = (self.screen.get_width() - GRID_SIZE * self.cell_size) // 2
       self.offset_y = (self.screen.get_height() - GRID_SIZE * self.cell_size) // 2   