import pygame
from pygame.locals import *

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

class Archer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [(pygame.image.load('Assets/character/character_sprite_idle1.png')).convert_alpha(),
                    pygame.image.load('Assets/character/character_sprite_idle2.png').convert_alpha()
        ]
        
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (150, 150))

        self.shooting_images = [(pygame.image.load('Assets/character/character_sprite_shooting1.png')).convert_alpha(),
                    pygame.image.load('Assets/character/character_sprite_shooting2.png').convert_alpha(),
                    pygame.image.load('Assets/character/character_sprite_shooting3.png').convert_alpha(),
                    pygame.image.load('Assets/character/character_sprite_shooting4.png').convert_alpha()
        ]
        
        for i in range(len(self.shooting_images)):
            self.shooting_images[i] = pygame.transform.scale(self.shooting_images[i], (150, 150))

        self.current_image = 0

        self.archer_position = [20,20]

        self.image = pygame.image.load('Assets/character/character_sprite_idle1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

        self.moving_up = False
        self.moving_down = False
        self.shooting = False
        self.shooting_ready = False
        self.arrows = 15


    def shoot(self):
        print('SHOOOOT')
        self.arrows -= 1
        self.shooting_ready, self.shooting = False, False



    def update(self):
        if self.current_image >= 3:
            self.shooting_ready = True

        else:
            self.shooting_ready = False

        self.current_image += 0.15

        if self.shooting:
            if self.current_image >= len(self.shooting_images):
                self.current_image = 3
        else:
            self.current_image -= 0.07
            if self.current_image >= len(self.images):
                self.current_image = 0


        if self.shooting:
            self.image = self.shooting_images[int(self.current_image)]
        else:
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


        self.balloon_speed = 1.7
        self.current_image = 0
        self.image = pygame.image.load('Assets/balloon/popped_balloon_sprite_1.png').convert()
        self.image = pygame.transform.scale(self.balloon_images[self.current_image], (50 , 50))

        self.balloon_position = [xpos, 900]
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.popped = False
        
        

    def is_off_screen(self):
        if self.rect[1] <= -200:
            return True
        else:
            return False
                

    def update(self):
        self.current_image += 0.15

        if self.popped == True:
            if self.current_image >= len(self.popped_images):
                self.current_image = 0
            self.image = self.popped_images[int(self.current_image)]
            if len(self.popped_images) == 5:
                del self.popped_images[0]

            self.balloon_position[1] += self.balloon_speed

        else:
            if self.current_image >= len(self.balloon_images):
                self.current_image = 0
            self.image = self.balloon_images[int(self.current_image)]
            self.balloon_position[1] -= self.balloon_speed

        if self.is_off_screen() and self.popped == False:
            self.balloon_position[1] = 900

        self.rect[1] = self.balloon_position[1]


class Arrow(pygame.sprite.Sprite):

    def __init__(self,xpos,ypos):
        pygame.sprite.Sprite.__init__(self)

        self.speed = 6.8 
        self.waiting = True
        self.shot = True
        self.image = pygame.image.load('Assets/arrow/arrow.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect()
        self.arrow_position = [xpos,ypos]
        self.rect[0], self.rect[1] = xpos, ypos

    def is_arrow_off_screen(self):
        if self.arrow_position[0] > 1600:
            return True
        else:
            return False

        
    def update(self):
        self.arrow_position[0] += self.speed
        self.rect[0] = self.arrow_position[0]
        if self.arrow_position[0] > 1600:
            self.kill()



def create_arrow_shooting(xpos, ypos):
    new_arrow = Arrow(xpos, ypos)
    arrow_group.add(new_arrow) 

def check_balloon_hit(arrow_group, balloon_group):

    result = pygame.sprite.groupcollide(arrow_group, balloon_group, False, False)
    if len(result) > 0:
        for key,value in result.items():
            for balloon in value:
                balloon.popped = True
                if balloon.popped == True:
                    print('POPPED')



pygame.init()
myfont = pygame.font.Font('Assets/font/pixel_font.ttf', 50)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('Assets/background/background.png').convert()
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

FLOOR = (pygame.image.load('Assets/textures/wooden_floor.png')).convert()
FLOOR_CROP = FLOOR.subsurface(0, 0, 40, 200)
FLOOR = pygame.transform.scale(FLOOR_CROP, (150,800))

FIRST_BALLOON_DISTANCE = 600

ARROW_COUNT_MENU = pygame.image.load('Assets/menu/arrow_count.png').convert_alpha()
ARROW_COUNT_MENU = pygame.transform.scale(ARROW_COUNT_MENU, (150,100))

archer_group = pygame.sprite.Group()
archer = Archer()
archer_group.add(archer)

balloon_group = pygame.sprite.Group()
for i in range(15):
    new_balloon = Balloon(FIRST_BALLOON_DISTANCE+i*50)
    balloon_group.add(new_balloon)

arrow_group = pygame.sprite.Group()


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
            if event.key == K_SPACE:
                if archer.shooting == False:
                    if(archer.arrows == 0):
                        pass
                    else:
                        archer.shooting = True
                if archer.shooting == True:
                    if archer.shooting_ready:
                        archer.shoot()
                        create_arrow_shooting(archer.archer_position[0], archer.archer_position[1])

                
        if event.type == KEYUP:
            if event.key == K_UP:
                archer.moving_up = False
            if event.key == K_DOWN:
                archer.moving_down = False

    


    screen.blit(BACKGROUND, (0, 0))
    screen.blit(FLOOR, (0, 0))

    screen.blit(ARROW_COUNT_MENU, ( SCREEN_WIDTH - ARROW_COUNT_MENU.get_width(), 0))
    arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))
    screen.blit(arrow_count_label,(1305, 27))

    archer_group.update()
    balloon_group.update()
    arrow_group.update()
    
    check_balloon_hit(arrow_group,balloon_group)

    archer_group.draw(screen)
    balloon_group.draw(screen)
    arrow_group.draw(screen)


    if archer.arrows == 0 and len(arrow_group) == 0:
        input()
        break
    
    pygame.display.update()


