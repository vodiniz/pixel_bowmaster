from email.mime import image
from lib2to3.pytree import convert
import pygame
from pygame.locals import *

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

class Archer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [(pygame.image.load('Assets/character/character_sprite_pos1.png')).convert_alpha(),
                    pygame.image.load('Assets/character/character_sprite_pos2.png').convert_alpha(),
                    pygame.image.load('Assets/character/character_sprite_pos3.png').convert_alpha(),
                    pygame.image.load('Assets/character/character_sprite_pos4.png').convert_alpha()
        ]
        
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (150, 150))

        self.current_image = 0

        self.archer_position = [20,20]

        self.image = pygame.image.load('Assets/character/character_sprite_pos1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        self.current_image += 0.15
        if self.current_image >= len(self.images):
            self.current_image = 0

        self.image = self.images[int(self.current_image)]

        if self.moving_up == True:
            self.archer_position[1] -= 8
    
        if self.moving_down == True:
            self.archer_position[1] += 8

        self.rect[0] = self.archer_position[0]
        self.rect[1] = self.archer_position[1]


class Balloon(pygame.sprite.Sprite):

    def __init__(self,xpos):
        pygame.sprite.Sprite.__init__(self)
        
        self.balloon_images = [(pygame.image.load('Assets/balloon/balloon_sprite_1.png')).convert_alpha(),
                    (pygame.image.load('Assets/balloon/balloon_sprite_2.png')).convert_alpha(),
                    (pygame.image.load('Assets/balloon/balloon_sprite_3.png')).convert_alpha(),
                    (pygame.image.load('Assets/balloon/balloon_sprite_4.png')).convert_alpha()
        ]
        for i in range(len(self.balloon_images)):
            self.balloon_images[i] = pygame.transform.scale(self.balloon_images[i], (50 , 50))

        self.popped_images = [(pygame.image.load('Assets/balloon/popped_balloon_sprite_1.png')).convert_alpha(),
                            (pygame.image.load('Assets/balloon/popped_balloon_sprite_2.png')).convert_alpha(),
                            (pygame.image.load('Assets/balloon/popped_balloon_sprite_3.png')).convert_alpha(),
                            (pygame.image.load('Assets/balloon/popped_balloon_sprite_4.png')).convert_alpha(),
                            (pygame.image.load('Assets/balloon/popped_balloon_sprite_5.png')).convert_alpha()
                            ]
        for i in range(len(self.popped_images)):
            self.popped_images[i] = pygame.transform.scale(self.popped_images[i], (50 , 50))

        self.current_image = 0
        self.image = pygame.image.load('Assets/balloon/popped_balloon_sprite_1.png').convert()
        self.image = pygame.transform.scale(self.balloon_images[self.current_image], (50 , 50))

        self.balloon_position = [xpos, 900]
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.popped = False

    def update(self):
        if self.popped == True:
            pass
        

        self.current_image += 0.15
        if self.current_image >= len(self.balloon_images):
            self.current_image = 0
        self.image = self.balloon_images[int(self.current_image)]


        self.balloon_position[1] -= 1.3
        self.rect[1] = self.balloon_position[1]



        
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('Assets/background/background.png').convert()
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
FLOOR = (pygame.image.load('Assets/textures/wooden_floor.png')).convert()
FLOOR_CROP = FLOOR.subsurface(0, 0, 40, 200)
FLOOR = pygame.transform.scale(FLOOR_CROP, (150,800))


archer_group = pygame.sprite.Group()
archer = Archer()
archer_group.add(archer)

balloon_group = pygame.sprite.Group()
balloon1 = Balloon(400)
balloon_group.add(balloon1)


clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == KEYDOWN:

            if event.key == K_UP:
                archer.moving_up = True
            if event.key == K_DOWN:
                archer.moving_down = True

        if event.type == KEYUP:
            if event.key == K_UP:
                archer.moving_up = False
            if event.key == K_DOWN:
                archer.moving_down = False



    screen.blit(BACKGROUND, (0, 0))
    screen.blit(FLOOR, (0, 0))

    archer_group.update()
    balloon_group.update()

    archer_group.draw(screen)
    balloon_group.draw(screen)
    
    pygame.display.update()


