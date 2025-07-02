from Map import *
import pygame
from define import *

class KeyboardOperation:
    def __init__(self, Algorithm, Solution_Path):
        self.current_step = 0
        self.auto_play = False
        self.step_delay = 500  # milliseconds between steps in autoplay
        self.last_step_time = 0
        self.Solution_Path = Solution_Path  # Make a copy of the solution path
        self.Algorithm = Algorithm

    # forward
    def get_next_step(self):
        if self.current_step < len(self.Solution_Path) - 1:
            self.current_step += 1
            move_sound.play()
            return self.Solution_Path[self.current_step]
        return None

    # backward
    def get_previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            move_sound.play()
            return self.Solution_Path[self.current_step]
        
        return self.Solution_Path[0]

    # auto
    def toggle_auto_play(self):
        self.auto_play = not self.auto_play
        space_sound.play()
        self.last_step_time = pygame.time.get_ticks()



    
    

