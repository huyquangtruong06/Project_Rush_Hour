import pygame
import copy
from define import *
from Map import Map
from Vehicles import Vehicle, Orientations, VehicleTypes
from Window import *
from Event import EventHandler
from DFS_Algorithm import DFSAlgorithm
from UCS_Algorithm import UCSAlgorithm
from A_Algorithm import A_Algorithm
from KeyboardOperation import KeyboardOperation
from Button import Button
from Support import *
from Levels import *
def main():
    run = True
    pygame.init()
    window = Window()
    map = Map(window.screen)
    index =select_levels(window.screen)
    # handler = EventHandler(map)
    map.vehicles = copy.deepcopy(vehicles_map[index])
    initial_vehicles = copy.deepcopy(vehicles_map[index])
    map.get_domain_cars()
    goal = map.get_goal_cars()


    print(f"Goal car: {goal.id} at position {goal.position} with orientation {goal.orientation} and type {goal.vtype}\n")

    DFS = DFSAlgorithm(map)
    DFS.current_step = 0
    result = DFS.search(map.copy())
    A = A_Algorithm(map.copy())
    a_result = A.search()
    UCS = UCSAlgorithm(map.copy())
    ucs_result = UCS.search()
    controller = KeyboardOperation(A, A.solution_path)
    handler = EventHandler(map, controller, initial_vehicles)

    if result is not None:
        print(f"Solution found with {len(DFS.solution_path)} steps")
        # Set initial state
        map.vehicles = DFS.solution_path[0].vehicles
        DFS.current_step = 0
    else:
        print("No solution found.")

    #handler = EventHandler(map, DFS)
    

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
            step_text = f"Step: {controller.current_step + 1}/{len(DFS.solution_path)}"
            text_surface = font.render(step_text, True, BLACK)
            window.screen.blit(text_surface, (10, 50))
            
            if controller.auto_play:
                auto_text = font.render("Auto-play: ON", True, GREEN)
            else:
                auto_text = font.render("Auto-play: OFF", True, RED)
            window.screen.blit(auto_text, (10, 70))
        
        pygame.display.update()
        clock.tick(60)
        
if __name__ == "__main__":
    main()

