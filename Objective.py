import pygame, random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (120, 120, 120)


class objective():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        
        self.spawn_x = 0
        self.spawn_y = 0
        self.coin_list = []
        
        coin = pygame.image.load("towerDefense_tile272.png").convert()
        coin = pygame.transform.scale(coin, (64, 64))
        coin.set_colorkey(BLACK)
        self.coin_list.append(coin)
    def spawning(self):
        self.spawn_x = random.randrange (0, 976)
        self.spawn_y = random.randrange (0, 880)
        self.rect.x = self.spawn_x
        self.rect.y = self.spawn_y
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, [self.rect.x, self.rect.y, 64, 64])       
        screen.blit(self.coin_list[0], [self.rect.x, self.rect.y])