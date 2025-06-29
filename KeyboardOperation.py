from Map import *
import pygame

class KeyboardOperation:
    def __init__(self, Algorithm, Solution_Path):
        self.current_step = 0
        self.auto_play = False
        self.step_delay = 500  # milliseconds between steps in autoplay
        self.last_step_time = 0
        self.Solution_Path = Solution_Path
        self.Algorithm = Algorithm

    # forward
    def get_next_step(self):
        if self.current_step < len(self.Solution_Path) - 1:
            self.current_step += 1
            return self.Solution_Path[self.current_step]
        return None

    # backward
    def get_previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            return self.Solution_Path[self.current_step]
        
        # Nếu đang ở bước 0, vẫn trả lại bước 0 để đảm bảo giao diện cập nhật
        return self.Solution_Path[0]

    # auto
    def toggle_auto_play(self):
        self.auto_play = not self.auto_play
        self.last_step_time = pygame.time.get_ticks()

    def reset(self, initial_map):
        """Reset internal state and resolve the puzzle again."""
        self.current_step = 0
        self.auto_play = False
        self.last_step_time = 0
        self.Algorithm.visited = set()
        self.Algorithm.Solution_Path = []

        result = self.Algorithm.search(initial_map.copy())
        if result is not None:
            self.Solution_Path = self.Algorithm.Solution_Path

    



    
    

