from define import *
from Button import Button
import pygame
from KeyboardOperation import menu_sound, level_sound

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
    level_sound.play(-1)

    while not selected_level:
        scaled_bg = scale_background(bg_level_menu, screen)
        screen.blit(scaled_bg, (0, 0))
        for button in buttons:
            button.draw()

        mouse_pos = pygame.mouse.get_pos()
        hand_cursor_needed = any(button.is_hovered(mouse_pos) for button in buttons)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(buttons)):
                    if buttons[i].is_clicked(event.pos):
                        print(f"Level {i + 1} selected")
                        level_sound.stop()
                        return i
        if hand_cursor_needed:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        pygame.display.update()

def start_menu(screen):
    Start_button = Button(screen, 0.5, 0.3, start_button.convert_alpha(), 0.25)
    Quit_button = Button(screen, 0.5, 0.7, quit_button.convert_alpha(), 0.25)

    while True:
        menu_sound.play()
        scaled_bg = scale_background(bg_start_menu, screen)
        screen.blit(scaled_bg, (0, 0))
        Start_button.draw()
        Quit_button.draw()
        mouse_pos = pygame.mouse.get_pos()
        hand_cursor_needed = (
            Start_button.is_hovered(mouse_pos) or Quit_button.is_hovered(mouse_pos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_sound.stop()
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_sound.stop()
                if Start_button.is_clicked(event.pos):
                    print("Start button clicked")
                    return True
                elif Quit_button.is_clicked(event.pos):
                    print("Quit button clicked")
                    pygame.quit()
                    return False
        if hand_cursor_needed:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.display.update()

    return True

def scale_background(bg_image, screen):
    screen_width, screen_height = screen.get_size()
    return pygame.transform.scale(bg_image, (screen_width, screen_height))
