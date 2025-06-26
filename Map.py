from Vehicles import *

class Map:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Rush Hour Puzzle - Zoom/Pan")
        
        self.cell_size = initial_cell_size
        self.offset_x = (WINDOW_WIDTH - GRID_SIZE * self.cell_size) // 2
        self.offset_y = (WINDOW_HEIGHT - GRID_SIZE * self.cell_size) // 2
        
        self.dragging = False
        self.last_mouse_pos = (0, 0)
        
        self.vehicles = []
    
    def draw_grid(self):
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
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.VIDEORESIZE:
                # Process when change size window.
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse - move map
                    self.dragging = True
                    self.last_mouse_pos = event.pos
                
                #Zoom in/out with middle mouse
                elif event.button == 4:  #Scroll up - zoom in
                    self.zoom(1.1, pygame.mouse.get_pos())
                elif event.button == 5:  # Scroll down - zoom out
                    self.zoom(0.9, pygame.mouse.get_pos())
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging = False
            
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging:
                    dx = event.pos[0] - self.last_mouse_pos[0]
                    dy = event.pos[1] - self.last_mouse_pos[1]
                    self.offset_x += dx
                    self.offset_y += dy
                    self.last_mouse_pos = event.pos
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    self.zoom(1.1, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
                elif event.key == pygame.K_MINUS:
                    self.zoom(0.9, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
                elif event.key == pygame.K_r:  # Reset zoom and position
                    self.reset_view()
        
        return True
    
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
           
    def draw(self):
        programIcon = pygame.image.load("RUSHHOUR.png")
        pygame.display.set_icon(programIcon)
        self.screen.fill(WHITE)
        
        # Draw grid
        self.draw_grid()
        
        # Draw vehicles
        for vehicle in self.vehicles:
            vehicle.draw(self.screen, self.cell_size, self.offset_x, self.offset_y)
        
        # Display guide.
        font = pygame.font.SysFont('Arial', 16)
        instructions = [
            "Scroll/Pinch to zoom | Drag to pan | R: Reset view",
            f"Zoom: {int((self.cell_size/BASE_CELL_SIZE)*100)}%"
        ]
        
        for i, text in enumerate(instructions):
            text_surface = font.render(text, True, BLACK)
            self.screen.blit(text_surface, (10, 10 + i * 20))
    
    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            running = self.handle_events()
            
            self.draw()
            pygame.display.flip()
            clock.tick(60)
        
        pygame.quit()
        sys.exit()