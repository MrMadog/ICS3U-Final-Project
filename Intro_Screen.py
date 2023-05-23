
import pygame, sys

BLACK = (30, 30, 30)
START_TEXT = (0, 0, 0)
COLLIDE_START_TEXT = (235, 235, 235)
START_BUTTON = (141, 212, 224)
START_BUTTON_COLLIDE = (114, 176, 186)
BUTTON_OUTLINE = (120, 120, 120)



def intro_screen(screen, clock):
    start_text_colour = START_TEXT
    mouse_collision = pygame.Rect(504, 456, 1, 1)
    start_button = pygame.Rect(449, 742, 110, 50)
    title_font = pygame.font.SysFont('Kanit-ExtraLight.ttf', 75, True, False)
    title_text = title_font.render("To The Clouds", True, BLACK)
    instruction_font = pygame.font.SysFont('Calibri', 40, True, False)
    instruction_text = instruction_font.render("Play", True, start_text_colour)
    intro_screen_bg = pygame.image.load("intro_screen_bg.png").convert()
    intro_screen_bg = pygame.transform.scale(intro_screen_bg, [1008, 912])
    pygame.mouse.set_visible(False)
    custom_cursor = pygame.image.load("tile_0027.png")
    custom_cursor = pygame.transform.scale(custom_cursor, [32, 32])
    start_button_colour = START_BUTTON
    done = False
    # -------- Main Program Loop -----------
    while not done:
            # --- Main event loop

            # --- All events are detected here
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True

                    elif event.type == pygame.MOUSEMOTION:
                        mouse_pos = pygame.mouse.get_pos()
                        mouse_collision.x = mouse_pos[0]
                        mouse_collision.y = mouse_pos[1]
                    if start_button.contains(mouse_collision):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            done = True

                    if start_button.contains(mouse_collision):
                        start_button_colour = START_BUTTON_COLLIDE
                        start_text_colour = COLLIDE_START_TEXT
                    else:
                        start_button_colour = START_BUTTON
                        start_text_colour = START_TEXT
            # --- Game logic should go here


            # --- Screen-clearing code goes here
            #  Here, we clear the screen to white. 
            mx, my = pygame.mouse.get_pos()

            screen.blit(intro_screen_bg, [0, 0])
            pygame.draw.rect(screen, BUTTON_OUTLINE, [447, 740, 114, 54])
            pygame.draw.rect(screen, start_button_colour, start_button)
            # --- Go ahead and update the screen with what we've drawn.


            # - TEXT - #
            screen.blit(title_text, [135, 190])
            screen.blit(instruction_text, [468, 750])

            screen.blit(custom_cursor, [mx-16, my-16])

            pygame.display.flip()
        
            # --- Limit to 60 frames per second
            clock.tick(60)
        