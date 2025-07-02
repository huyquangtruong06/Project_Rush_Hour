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
        pygame.font.init()
        window = Window()
        play = start_menu(window.screen)
        if not play:
            pygame.quit()
            break
        map = Map(window.screen)

        index =select_levels(window.screen)
        if index is None :
            return
        
        while True:
            menu = Menu(window.screen, index)
            algo_choice = menu.get_algorithm_choice()
            if algo_choice == "BACK":
                index = select_levels(window.screen)
                if index is None:
                    return  # Người dùng thoát
                continue
            elif algo_choice is None:
                return  # Người dùng tắt cửa sổ
            else:
                break  
        
        menu = Menu(window.screen, index)
        
        map.vehicles = copy.deepcopy(vehicles_map[index])
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
                map = algo.solution_path[0].copy()
        else:
                print("No solution found.")
        
        controller = KeyboardOperation(algo, algo.solution_path)
        handler = EventHandler(map.copy(), controller)

        clock = pygame.time.Clock()
        run = True

        while run:
            if not handler.handle_events() or not result:
                break
            scaled_bg = scale_background(bg_game, window.screen)
            window.screen.blit(scaled_bg, (0, 0))
            handler.map.draw()
            run = handler.handle_events()

            # Display step information
            font = pygame.font.SysFont('Arial', 16)
            if controller.Solution_Path:
                step_text = f"Step: {controller.current_step + 1}/{len(controller.Solution_Path)}"
                text_surface = font.render(step_text, True, CYAN)
                window.screen.blit(text_surface, (10, 110))
                
                if controller.auto_play:
                    auto_text = font.render("Pause game: ON", True, GREEN)
                else:
                    auto_text = font.render("Pause game: OFF", True, RED)
                window.screen.blit(auto_text, (10, 130))
            
            pygame.display.update()
            clock.tick(60)
        
if __name__ == "__main__" :
    main()

