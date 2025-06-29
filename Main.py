import pygame
import copy
from Map import Map
from Vehicles import Vehicle, Orientations, VehicleTypes
from Window import *
from Event import EventHandler
from DFS_Algorithm import DFSAlgorithm

def main():
    run = True
    pygame.init()
    window = Window()
    map = Map(window.screen)
    # handler = EventHandler(map)
    vehicles = [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (2, 3), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (3, 0), Orientations.vertical, VehicleTypes.car, 2),
        Vehicle("D", (3, 2), Orientations.vertical, VehicleTypes.car, 3),
        Vehicle("E", (3, 4), Orientations.horizontal, VehicleTypes.car, 4),
        Vehicle("F", (5, 4), Orientations.vertical, VehicleTypes.car, 5),
        Vehicle("G", (4, 3), Orientations.horizontal, VehicleTypes.car, 6),
    ]

    map.vehicles = copy.deepcopy(vehicles)
    map.get_domain_cars()
    goal = map.get_goal_cars()
    print(f"Goal car: {goal.id} at position {goal.position} with orientation {goal.orientation} and type {goal.vtype}\n")
    DFS = DFSAlgorithm(map)
    result = DFS.search(DFS.map)

    '''if result is not None:
        print("Solution found:")
        result.get_domain_cars()
        result.draw()
    else:
        print("No solution found.")'''
    if result is not None:
        print(f"Solution found with {len(DFS.solution_path)} steps")
        map.vehicles = DFS.solution_path[0].vehicles
    else:
        print("No solution found.")

    handler = EventHandler(map, DFS)
    clock = pygame.time.Clock()

    while run:
        if not handler.handle_events():
            break
        window.fill(WHITE)
        map.draw()
        run = handler.handle_events()

        # Display step information
        font = pygame.font.SysFont('Arial', 16)
        if DFS.solution_path:
            step_text = f"Step: {DFS.current_step + 1}/{len(DFS.solution_path)}"
            text_surface = font.render(step_text, True, BLACK)
            window.screen.blit(text_surface, (10, 50))
            
            if DFS.auto_play:
                auto_text = font.render("Auto-play: ON", True, GREEN)
            else:
                auto_text = font.render("Auto-play: OFF", True, RED)
            window.screen.blit(auto_text, (10, 70))
        
        pygame.display.update()
        clock.tick(60)
        
if __name__ == "__main__":
    main()

