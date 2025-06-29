'''import pygame
from define import *
from Map import Map
class EventHandler():
    def __init__(self, map):
        self.map = map


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.VIDEORESIZE:
                # Process when change size window.
                self.map.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse - move map
                    self.map.dragging = True
                    self.map.last_mouse_pos = event.pos
                
                #Zoom in/out with middle mouse
                elif event.button == 4:  #Scroll up - zoom in
                    self.map.zoom(1.1, pygame.mouse.get_pos())
                elif event.button == 5:  # Scroll down - zoom out
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
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    self.map.zoom(1.1, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
                elif event.key == pygame.K_MINUS:
                    self.map.zoom(0.9, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
                elif event.key == pygame.K_r:  # Reset zoom and position
                    self.map.reset_view()

        return True
'''
# BY HUY
import pygame
from define import *
from Map import Map
import copy

class EventHandler:
    def __init__(self, map, dfs_algorithm):
        self.map = map
        self.dfs = dfs_algorithm

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
                self._handle_control_keys(event)

        # Handle auto-play
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
            self.dfs.toggle_auto_play() 

    def NextStep(self):
        next_state = self.dfs.get_next_step()
        if next_state:
            self.map.vehicles = next_state.vehicles

    def LastStep(self):
        prev_state = self.dfs.get_previous_step()
        if prev_state:
            self.map.vehicles = prev_state.vehicles

    def AutoPlay(self, current_time):
        if self.dfs.auto_play and current_time - self.dfs.last_step_time > self.dfs.step_delay:
            next_state = self.dfs.get_next_step()
            if next_state:
                self.map.vehicles = next_state.vehicles
                self.dfs.last_step_time = current_time
            else:
                self.dfs.auto_play = False
