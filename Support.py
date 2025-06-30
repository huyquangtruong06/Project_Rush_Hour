from define import *
from Button import Button
import pygame
def select_levels(screen):

    lv1 = Button(screen, 175, 50, LEVELS[0].convert_alpha(), 0.5)
    lv2 = Button(screen, 425, 50, LEVELS[1].convert_alpha(), 0.5)
    lv3 = Button(screen, 175, 125, LEVELS[2].convert_alpha(), 0.5)
    lv4 = Button(screen, 425, 125, LEVELS[3].convert_alpha(), 0.5)
    lv5 = Button(screen, 175, 200, LEVELS[4].convert_alpha(), 0.5)
    lv6 = Button(screen, 425, 200, LEVELS[5].convert_alpha(), 0.5)
    lv7 = Button(screen, 175, 275, LEVELS[6].convert_alpha(), 0.5)
    lv8 = Button(screen, 425, 275, LEVELS[7].convert_alpha(), 0.5)
    lv9 = Button(screen, 175, 350, LEVELS[8].convert_alpha(), 0.5)
    lv10 = Button(screen, 425, 350, LEVELS[9].convert_alpha(), 0.5)

    selected_level = False
    while not selected_level:
        screen.fill(WHITE)
        lv1.draw()
        lv2.draw()
        lv3.draw()
        lv4.draw()
        lv5.draw()
        lv6.draw()
        lv7.draw()
        lv8.draw()
        lv9.draw()
        lv10.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lv1.is_clicked(event.pos):
                    print("Level 1 selected")
                    selected_level = True
                    return 0

                elif lv2.is_clicked(event.pos):
                    print("Level 2 selected")
                    selected_level = True
                    return 1
                elif lv3.is_clicked(event.pos):
                    print("Level 3 selected")
                    selected_level = True
                    return 2
                    break
                elif lv4.is_clicked(event.pos):
                    print("Level 4 selected")
                    selected_level = True
                    return 3
                    break
                elif lv5.is_clicked(event.pos):
                    print("Level 5 selected")
                    selected_level = True
                    return 4
                    break
                elif lv6.is_clicked(event.pos):
                    print("Level 6 selected")
                    selected_level = True
                    return 5
                    break
                elif lv7.is_clicked(event.pos):
                    print("Level 7 selected")
                    selected_level = True
                    return 6
                    break
                elif lv8.is_clicked(event.pos):
                    print("Level 8 selected")
                    selected_level = True
                    return 7
                    break
                elif lv9.is_clicked(event.pos):
                    print("Level 9 selected")
                    selected_level = True
                    return 8
                    break
                elif lv10.is_clicked(event.pos):
                    print("Level 10 selected")
                    selected_level = True
                    return 9
                    break
        pygame.display.update()
