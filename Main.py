import pygame
import copy
from Map import Map
from Vehicles import Vehicle, Orientations, VehicleTypes
from Window import *
from Event import EventHandler
from DFS_Algorithm import DFSAlgorithm
from UCS_Algorithm import UCSAlgorithm
from State import State
def main():
    run = True
    Clock = pygame.time.Clock()
    pygame.init()
    window = Window()
    map = Map(window.screen)
    handler = EventHandler(map)
    vehicles = [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (2, 2), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (3, 0), Orientations.vertical, VehicleTypes.car, 2),
        Vehicle("D", (3, 2), Orientations.vertical, VehicleTypes.car, 3),
        Vehicle("E", (3, 4), Orientations.horizontal, VehicleTypes.car, 4),
        Vehicle("F", (5, 4), Orientations.vertical, VehicleTypes.car, 5),
        Vehicle("G", (4, 3), Orientations.horizontal, VehicleTypes.car, 6),

    ]
    # map.vehicles = copy.deepcopy(vehicles)
    # map.get_domain_cars()
    # goal = map.get_goal_cars()
    # print(f"Goal car: {goal.id} at position {goal.position} with orientation {goal.orientation} and type {goal.vtype}\n")
    # DFS = DFSAlgorithm(map)
    # result = DFS.search(DFS.map)
    # if result is not None:
    #     print("Solution found:")
    #     result.get_domain_cars()
    #     result.draw()
    # else:
    #     print("No solution found.")

    map.vehicles = copy.deepcopy(vehicles)
    initial_state = State(map.vehicles)
    cost, result_path = UCSAlgorithm(initial_state).search()
    if result_path is not None:
        print("Solution found:")
    else:
        print("No solution found.")

    isShow = False
    while run:
        
        window.fill(WHITE)
        map.draw()
        run = handler.handle_events()
        if result_path and not isShow:
            isShow = True
            for state in result_path:
                map.vehicles = copy.deepcopy(state.vehicles)
                window.fill(WHITE)
                map.draw()
                pygame.display.update()
                pygame.time.delay(1000)
                Clock.tick(60)

        pygame.display.update()
 
    pygame.quit()


if __name__ == "__main__":
    main()
