import pygame
import copy
from Map import Map
from Vehicles import Vehicle, Orientations, VehicleTypes
from Window import *
from Event import EventHandler
from DFS_Algorithm import DFSAlgorithm
from UCS_Algorithm import UCSAlgorithm
from A_Algorithm import A_Algorithm
from KeyboardOperation import KeyboardOperation
from BFS_Algorithm import BFSAlgorithm
from Menu import Menu

def main():
    run = True
    pygame.init()
    window = Window()
    map = Map(window.screen)

    menu = Menu(window.screen)
    algo_choice = menu.get_algorithm_choice()
    if algo_choice is None:
        return
    
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
    initial_vehicles = copy.deepcopy(vehicles)
    map.get_domain_cars()
    goal = map.get_goal_cars()
    print(f"Goal car: {goal.id} at position {goal.position} with orientation {goal.orientation} and type {goal.vtype}\n")
    
    if algo_choice == "DFS":
        algo = DFSAlgorithm(map)
        result = algo.search(map.copy())
    elif algo_choice == "BFS":
        algo = BFSAlgorithm(map)
        result = algo.search(map.copy())
    elif algo_choice == "UCS":
        algo = UCSAlgorithm(map.copy())
        result = algo.search()
    elif algo_choice == "A*":
        algo = A_Algorithm(map.copy())
        result = algo.search()
    else:
        print("Invaid Algorithm")
        return
    
    '''
    # DFS.
    DFS = DFSAlgorithm(map)
    DFS.current_step = 0
    result = DFS.search(map.copy())

    # A star
    A = A_Algorithm(map.copy())
    a_result = A.search()

    # UCS
    UCS = UCSAlgorithm(map.copy())
    ucs_result = UCS.search()

    # BFS 
    BFS = BFSAlgorithm(map)
    BFS.current_step = 0
    result = BFS.search(map.copy())'''

    if result is not None:
            print(f"Solution found with {len(algo.solution_path)} steps")
            map.vehicles = algo.solution_path[0].vehicles
    else:
            print("No solution found.")

    
    controller = KeyboardOperation(algo, algo.solution_path)
    handler = EventHandler(map, controller, initial_vehicles)

    clock = pygame.time.Clock()
    run = True

    #handler = EventHandler(map, DFS)

    while run:
        if not handler.handle_events():
            break
        window.fill(WHITE)
        map.draw()
        run = handler.handle_events()

        # Display step information
        font = pygame.font.SysFont('Arial', 16)
        if controller.Solution_Path:
            step_text = f"Step: {controller.current_step + 1}/{len(controller.Solution_Path)}"
            text_surface = font.render(step_text, True, BLACK)
            window.screen.blit(text_surface, (10, 50))
            
            if controller.auto_play:
                auto_text = font.render("Auto-play: ON", True, GREEN)
            else:
                auto_text = font.render("Auto-play: OFF", True, RED)
            window.screen.blit(auto_text, (10, 70))
        
        pygame.display.update()
        clock.tick(60)
        
if __name__ == "__main__" :
    main()

