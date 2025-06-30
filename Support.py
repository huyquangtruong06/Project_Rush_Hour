from define import *
from Button import Button
import pygame
def select_levels(screen):

    buttons = [
        Button(screen, 0.3, 0.1, LEVELS[0].convert_alpha(), 0.5),
        Button(screen, 0.7, 0.1, LEVELS[1].convert_alpha(), 0.5),
        Button(screen, 0.3, 0.3, LEVELS[2].convert_alpha(), 0.5),
        Button(screen, 0.7, 0.3, LEVELS[3].convert_alpha(), 0.5),
        Button(screen, 0.3, 0.5, LEVELS[4].convert_alpha(), 0.5),
        Button(screen, 0.7, 0.5, LEVELS[5].convert_alpha(), 0.5),
        Button(screen, 0.3, 0.7, LEVELS[6].convert_alpha(), 0.5),
        Button(screen, 0.7, 0.7, LEVELS[7].convert_alpha(), 0.5),
        Button(screen, 0.3, 0.9, LEVELS[8].convert_alpha(), 0.5),
        Button(screen, 0.7, 0.9, LEVELS[9].convert_alpha(), 0.5),
    ]
    selected_level = False
    while not selected_level:
        screen.fill(WHITE)
        for button in buttons:
            button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(buttons)):
                    if buttons[i].is_clicked(event.pos):
                        print(f"Level {i + 1} selected")
                        return i 
        pygame.display.update()

def start_menu(screen):
    Start_button = Button(screen, 0.5, 0.3, start_button.convert_alpha(), 0.25)
    Quit_button = Button(screen, 0.5, 0.7, quit_button.convert_alpha(), 0.25)

    while True:
        screen.fill(WHITE)
        Start_button.draw()
        Quit_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Start_button.is_clicked(event.pos):
                    print("Start button clicked")
                    return True
                elif Quit_button.is_clicked(event.pos):
                    print("Quit button clicked")
                    pygame.quit()
                    return False

        pygame.display.update()

    return True