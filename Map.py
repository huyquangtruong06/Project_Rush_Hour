from Vehicles import *
import copy

class Map:
    def __init__(self, screen, parent = None, cost = 0):
        self.screen = screen
        self.cell_size = initial_cell_size
        self.offset_x = (WINDOW_WIDTH - GRID_SIZE * self.cell_size) // 2
        self.offset_y = (WINDOW_HEIGHT - GRID_SIZE * self.cell_size) // 2
        
        self.dragging = False
        self.last_mouse_pos = (0, 0)
        
        self.vehicles = []
        self.vehicles_goal = None

        self.parent = parent
        self.cost = cost

    def copy(self):
        """Create a copy of the current map"""
        new_map = Map(self.screen)
        new_map.cell_size = self.cell_size
        new_map.offset_x = self.offset_x
        new_map.offset_y = self.offset_y
        new_map.dragging = self.dragging
        new_map.last_mouse_pos = self.last_mouse_pos
        new_map.vehicles = [vehicle.copy() for vehicle in self.vehicles]
        
        return new_map

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
        for vehicle in self.vehicles:
            vehicle.draw(self.screen, self.cell_size, self.offset_x, self.offset_y)
        
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

    def check_exit(self, target, array):
        for i in array:
            if i == target:
                return True
        return False
    
    def get_domain_cars(self):
        tmp = [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]
        ]
        
        for vehicle in self.vehicles:
            if vehicle.orientation == Orientations.horizontal:
                for i in range(int(vehicle.vtype)):
                    tmp[vehicle.position[1]][vehicle.position[0] + i] = 1
            else:  # vertical
                for i in range(int(vehicle.vtype)):
                    tmp[vehicle.position[1] + i][vehicle.position[0]] = 1
        # print(tmp)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                print(tmp[i][j], end=' ')
            print("\n")
        print("\n")
        
        for vehicle in self.vehicles:
            vehicle.domain = []
            #horizontal
            if vehicle.orientation == Orientations.horizontal:
                for i in range(vehicle.position[0]):
                    if tmp[vehicle.position[1]][i] == 0:
                        vehicle.domain.append((i, vehicle.position[1], (vehicle.position[0] - i) * vehicle.vtype))
                    else:
                        vehicle.domain.clear()
                i = vehicle.position[0] + int(vehicle.vtype)
                while i < GRID_SIZE:
                    if tmp[vehicle.position[1]][i] == 0:
                        vehicle.domain.append((i - vehicle.vtype + 1, vehicle.position[1], (i - vehicle.vtype + 1 - vehicle.position[0]) * vehicle.vtype))
                    else:
                        break
                    i += 1
            else:  # vertical
                for i in range(vehicle.position[1]):
                    if tmp[i][vehicle.position[0]] == 0:
                        vehicle.domain.append((vehicle.position[0], i, (vehicle.position[1] - i) * vehicle.vtype))
                    else:
                        vehicle.domain.clear()
                i = vehicle.position[1] + int(vehicle.vtype)
                while i < GRID_SIZE:   
                    if tmp[i][vehicle.position[0]] == 0:
                        vehicle.domain.append((vehicle.position[0], i - vehicle.vtype + 1, (i - vehicle.vtype + 1 -vehicle.position[1]) * vehicle.vtype))
                    else:
                        break
                    i += 1

    def setup_goal_cars(self):
        for vehicle in self.vehicles:
            if vehicle.orientation == Orientations.horizontal and vehicle.position[1] == 2:
                self.vehicles_goal = vehicle

    def get_goal_cars(self):
        if self.vehicles_goal is None:
            self.setup_goal_cars()
        return self.vehicles_goal
    
    def get_map_signature(self):
        return tuple( v.position for v in self.vehicles)

    def sort_vehicles(self):
        """Sort vehicles by their position in the grid"""
        tmp = []
        for vehicle in self.vehicles:
            if vehicle.id != self.get_goal_cars().id:
                tmp.append(vehicle)

    def reset_to_state(self, state):
        self.vehicles = [v.copy() for v in state.vehicles]
        self.vehicles_goal = None
        self.setup_goal_cars()  