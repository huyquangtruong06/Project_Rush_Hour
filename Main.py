import pygame
from Map import Map
from Vehicles import Vehicle, Orientations, VehicleTypes

def main():
    pygame.init()

    # List car.
    vehicles = [
        Vehicle("A", (0, 2), Orientations.horizontal, VehicleTypes.car, 0),
        Vehicle("B", (2, 0), Orientations.vertical, VehicleTypes.truck, 1),
        Vehicle("C", (3, 3), Orientations.horizontal, VehicleTypes.truck, 2),
        Vehicle("D", (5, 0), Orientations.vertical, VehicleTypes.car, 3),
        Vehicle("E", (0, 0), Orientations.vertical, VehicleTypes.car, 4),
        Vehicle("X", (2, 2), Orientations.horizontal, VehicleTypes.car, 5)  # Goal.
    ]

    game_map = Map()
    game_map.vehicles = vehicles  # Assign list car into map.
    game_map.run()  #Run.

if __name__ == "__main__":
    main()
