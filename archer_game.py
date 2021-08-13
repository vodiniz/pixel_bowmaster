from email.mime import image
import pygame
from pygame.locals import *

SCREEN_WIDTH = 1200
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

    def __init__(self):

        self.images = [(pygame.image.load('Assets/baloon/balloon_sprite_1.png')).convert_alpha(),
                    (pygame.image.load('Assets/baloon/balloon_sprite_2.png')).convert_alpha(),
                    (pygame.image.load('Assets/baloon/balloon_sprite_3.png')).convert_alpha(),
                    (pygame.image.load('Assets/baloon/balloon_sprite_4.png')).convert_alpha()
        ]

        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (50 , 50))

        self.popped_images = [image(pygame.image.load('Assets/baloon/popped_balloon_sprite_1.png')).convert_alpha(),
                            image(pygame.image.load('Assets/baloon/popped_balloon_sprite_2.png')).convert_alpha(),
                            image(pygame.image.load('Assets/baloon/popped_balloon_sprite_3.png')).convert_alpha(),
                            image(pygame.image.load('Assets/baloon/popped_balloon_sprite_4.png')).convert_alpha(),
                            image(pygame.image.load('Assets/baloon/popped_balloon_sprite_5.png')).convert_alpha()
                            ]
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (50 , 50))

        self.current_image = 0

    def is_out_of_screen(self):
        if ballon
        
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('Assets/background/background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

archer_group = pygame.sprite.Group()
archer = Archer()
archer_group.add(archer)

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
                print('deveria ser falso')
                print(archer.moving_up)
            if event.key == K_DOWN:
                archer.moving_down = False



    screen.blit(BACKGROUND, (0, 0))

    archer_group.update()
    archer_group.draw(screen)
    
    pygame.display.update()


