
import pygame, sys, math
from Intro_Screen import intro_screen
import Objective
#from Outro_Screen import outro_screen

def draw_plane_shadow(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)



custom_cursor = pygame.image.load("tile_0027.png")
custom_cursor = pygame.transform.scale(custom_cursor, [32, 32])


# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (120, 120, 120)


pygame.init()
# Set the width and height of the screen [width, height]
size = (1008, 912)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("To The Clouds")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

object = Objective.objective(100, 100)


intro_screen(screen, clock)

final_map = pygame.image.load("Final Project Map.png").convert()
final_map.set_colorkey(BLACK)

grass = pygame.image.load("tile_0050.png")

plane = pygame.image.load("ship_0007.png")
plane = pygame.transform.scale(plane, (64,64))

plane_shadow = pygame.image.load("ship_0007_shadow.png")
plane_shadow = pygame.transform.scale(plane_shadow, (64, 64))

player_pos = [500, 950]

x = 100
y = 100


pygame.mouse.set_visible(False)

# -------- Main Program Loop -----------
while not done:
        # --- Main event loop

        # --- All events are detected here
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                
        # --- Game logic should go here
        
        # --- Screen-clearing code goes here
         #  Here, we clear the screen to white. 
        mx, my = pygame.mouse.get_pos() # mouseState.X & mouseState.Y

        for x in range(0,1008,16):
            for y in range(0,912,16):
                screen.blit(grass, (0+x, 0+y))
        screen.blit(final_map, [0, 0])

        dx = mx - player_pos[0]
        dy = my - player_pos[1]
        
        angle = math.atan2(dx, dy)
        movex = math.sin(angle)
        movey = math.cos(angle)

        player_pos[0] += movex * 1.10
        player_pos[1] += movey * 1.10

        



        mouse_pos = pygame.mouse.get_pos()
        angle1 = math.atan2(mouse_pos[1] - (player_pos[1]+32), mouse_pos[0] - (player_pos[0]+26))
        planerot = pygame.transform.rotate(plane, 260-angle1*57.29)
        planerot_shadow = pygame.transform.rotate(plane_shadow, 260-angle1*57.29)
        player_pos1 = (player_pos[0] - planerot.get_rect().width/2, player_pos[1]-planerot.get_rect().height/2)
        player_pos_shadow = (player_pos[0] - planerot_shadow.get_rect().width/2 - 40, player_pos[1]-planerot_shadow.get_rect().height/2 + 30)

        draw_plane_shadow(screen, planerot_shadow, player_pos_shadow, 100)
        screen.blit(planerot, player_pos1)

        screen.blit(custom_cursor, [mx-16, my-16])



        plane_collision = pygame.Rect(player_pos[0]- 15, player_pos[1]-15, 30, 30)

        
        if plane_collision.colliderect(object.rect):
            object.spawning()


        object.draw(screen)

        #pygame.draw.rect(screen, RED, [player_pos[0]-15, player_pos[1]-15, 30, 30])
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
        
# Close the window and quit.
pygame.quit()
