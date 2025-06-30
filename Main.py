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
from BFS_Algorithm import BFSAlgorithm
from Menu import Menu

def main():
    play = True
    while play:
        
        pygame.init()
        window = Window()
        play = start_menu(window.screen)
        if not play:
            pygame.quit()
            break
        map = Map(window.screen)

        index =select_levels(window.screen)

        menu = Menu(window.screen)
        algo_choice = menu.get_algorithm_choice()
        if algo_choice is None:
            return
        
        # handler = EventHandler(map)
        map.vehicles = copy.deepcopy(vehicles_map[index])
        initial_vehicles = copy.deepcopy(vehicles_map[index])
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

