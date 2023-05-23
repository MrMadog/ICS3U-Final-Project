
import pygame, sys


def outro_screen(screen, clock):
    done = False
    # -------- Main 87Program Loop -----------
    while not done:
            # --- Main event loop

            # --- All events are detected here
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            terminate()

            # --- Game logic should go here


            # --- Screen-clearing code goes here
             #  Here, we clear the screen to white. 


        
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        
            # --- Limit to 60 frames per second
            clock.tick(60)
        