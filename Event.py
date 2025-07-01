import pygame
from define import *
import copy
from pygame.locals import *
from KeyboardOperation import move_sound, space_sound, i_sound
class EventHandler:
    def __init__(self, map, KeyboardOperation):
        self.map = map.copy()
        self.KeyboardOperation = KeyboardOperation

    def handle_events(self):
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.VIDEORESIZE:
                self.map.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse
                    self.map.dragging = True
                    self.map.last_mouse_pos = event.pos
                elif event.button == 4:  # Scroll up
                    self.map.zoom(1.1, pygame.mouse.get_pos())
                elif event.button == 5:  # Scroll down
                    self.map.zoom(0.9, pygame.mouse.get_pos())

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.map.dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if self.map.dragging:
                    dx = event.pos[0] - self.map.last_mouse_pos[0]
                    dy = event.pos[1] - self.map.last_mouse_pos[1]
                    self.map.offset_x += dx
                    self.map.offset_y += dy
                    self.map.last_mouse_pos = event.pos

            elif event.type == pygame.KEYDOWN:
                if self._handle_control_keys(event) == False:
                    return False

        # auto-play
        self.AutoPlay(current_time)

        return True

    def _handle_control_keys(self, event):
        if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
            self.map.zoom(1.1, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        elif event.key == pygame.K_MINUS:
            self.map.zoom(0.9, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        elif event.key == pygame.K_r:
            self.map.reset_view()
        elif event.key == pygame.K_RIGHT:
            self.NextStep()
            
        elif event.key == pygame.K_LEFT:
            self.LastStep()
        elif event.key == pygame.K_SPACE:
            self.KeyboardOperation.toggle_auto_play()
        elif event.key == pygame.K_i:
            self.ResetInitial()
            i_sound.play()
        elif event.key == pygame.K_ESCAPE:
            return False
        return True

    def NextStep(self):
        next_state = self.KeyboardOperation.get_next_step()
        if next_state:
            self.map = next_state.copy()

    def LastStep(self):
        prev_state = self.KeyboardOperation.get_previous_step()
        if prev_state:
            self.map = prev_state.copy()

    def AutoPlay(self, current_time):
        if self.KeyboardOperation.auto_play and current_time - self.KeyboardOperation.last_step_time > self.KeyboardOperation.step_delay:
            next_state = self.KeyboardOperation.get_next_step()
            if next_state:
                self.map = next_state.copy()
                self.KeyboardOperation.last_step_time = current_time
            else:
                self.KeyboardOperation.auto_play = False

    def ResetInitial(self):
        # Reset vehicles on map
        # Reset algorithm
        self.KeyboardOperation.visited = set()
        # self.KeyboardOperation.Solution_Path = []
        self.KeyboardOperation.current_step = 0
        self.KeyboardOperation.auto_play = False
        self.map = self.KeyboardOperation.Solution_Path[0].copy()



