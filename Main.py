import pygame
from Map import Map
from Vehicles import Vehicle, Orientations, VehicleTypes
from Window import *
from Event import EventHandler

def main():
    run = True
    pygame.init()
    window = Window()
    map = Map(window.screen)
    handler = EventHandler(map)
    while run:
        
        window.fill(WHITE)
        map.draw()
        run = handler.handle_events()

        pygame.display.update()
 


if __name__ == "__main__":
    main()
