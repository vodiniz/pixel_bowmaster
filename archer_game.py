import pygame
from settings import settings
from pygame.locals import *

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

        self.archer_position = settings.ARCHER_STARTING_POSITION

        self.image = pygame.image.load('Assets/character/character_sprite_idle1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

        self.moving_up = False
        self.moving_down = False
        self.shooting = False
        self.shooting_ready = False
        self.arrows = settings.ARROW_COUNT_LEVEL_1


    def shoot(self):
        self.arrows -= 1
        self.shooting_ready, self.shooting = False, False



    def update(self):
        if self.current_image >= 3:
            self.shooting_ready = True

        else:
            self.shooting_ready = False

        self.current_image += settings.ARCHER_SHOOTING_ANIMATION_SPEED

        if self.shooting:
            if self.current_image >= len(self.shooting_images):
                self.current_image = 3
        else:
            self.current_image -= settings.ARCHER_IDLE_ANIMATION_SPEED
            if self.current_image >= len(self.images):
                self.current_image = 0


        if self.shooting:
            self.image = self.shooting_images[int(self.current_image)]
        else:
            self.image = self.images[int(self.current_image)]


        if self.moving_up == True:
            if self.archer_position[1] <= 0:
                pass
            else:
                self.archer_position[1] -= settings.ARCHER_MOVING_SPEED
        if self.moving_down == True:
            if self.archer_position[1] >= 650:
                pass
            else:
                self.archer_position[1] += settings.ARCHER_MOVING_SPEED


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


        self.balloon_speed = settings.BALLOON_SPEED
        self.current_image = 0
        self.image = pygame.image.load('Assets/balloon/popped_balloon_sprite_1.png').convert()
        self.image = pygame.transform.scale(self.balloon_images[self.current_image], (50 , 50))

        self.balloon_position = [xpos, 900]
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.popped = False
        
        balloon_mask = pygame.mask.from_surface(self.image)


    def is_off_screen(self):
        if self.rect[1] <= -200:
            return True
        else:
            return False
                

    def update(self):
        self.current_image += settings.BALLOON_ANIMATION_SPEED

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

        self.speed = settings.ARROW_SPEED 
        self.waiting = True
        self.shot = True
        self.image = pygame.image.load('Assets/arrow/arrow.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect()
        self.arrow_position = [xpos,ypos]
        self.rect[0], self.rect[1] = xpos, ypos

        arrow_mask = pygame.mask.from_surface(self.image)

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


class MouseArrow(pygame.sprite.Sprite):

    def __init__(self,xpos,ypos):
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load('Assets/arrow/arrow.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect()
        self.arrow_position = [xpos,ypos]
        self.rect[0], self.rect[1] = xpos, ypos

        self.arrow_mask = pygame.mask.from_surface(self.image)
        print(pygame.mask.Mask.get_rect(self.arrow_mask))

    def is_arrow_off_screen(self):
        if self.arrow_position[0] > 1600:
            return True
        else:
            return False
        
    def update(self):
        self.arrow_position = pygame.mouse.get_pos()[0]-self.rect[2]/2,\
            pygame.mouse.get_pos()[1]-self.rect[3]/2
        self.rect[0],self.rect[1] = self.arrow_position


def create_arrow_shooting(xpos, ypos):
    new_arrow = Arrow(xpos, ypos)
    arrow_group.add(new_arrow) 


def check_balloon_hit(arrow_group, balloon_group):

    result = pygame.sprite.groupcollide(arrow_group, balloon_group, False, False, \
        pygame.sprite.collide_mask)
    if len(result) > 0:
        for arrow,balloon_list in result.items():
            for balloon in balloon_list:
                balloon_middle = balloon.rect[0] + balloon.rect[2]/2
                arrow_tip = arrow.rect[0] + (3/4)*arrow.rect[2]
                if arrow_tip < balloon_middle:
                    balloon.popped = True

def create_balloons(balloon_number):
    for i in range(balloon_number):
        new_balloon = Balloon(settings.FIRST_BALLOON_DISTANCE+i*50)
        balloon_group.add(new_balloon)

def mouse_arrow_testing(boolean):
    if boolean:
        mouse_arrow = MouseArrow(pygame.mouse.get_pos()[1],pygame.mouse.get_pos()[1])
        arrow_group.add(mouse_arrow)

def blit_game_static_elements(screen):

    screen.blit(BACKGROUND, (0,0))
    screen.blit(FLOOR, (0,0))
    screen.blit(ARROW_COUNT_MENU, ( settings.SCREEN_WIDTH - ARROW_COUNT_MENU.get_width(), 0))
    

def update_sprites():
    archer_group.update()
    balloon_group.update()
    arrow_group.update()
    

def draw_sprites(screen):
    archer_group.draw(screen)
    balloon_group.draw(screen)
    arrow_group.draw(screen)

def check_game_over():
    if archer.arrows == 0 and len(arrow_group) == 0:
        return True
    else:
        return False


def main_menu():
    clock.tick(settings.CLOCK)

    play_collision = False
    click = False

    play_rect = PLAY_BUTTON.get_rect()
    play_rect[0] = (settings.SCREEN_WIDTH/2 - PLAY_BUTTON.get_width()/2)
    play_rect[1] = 400
    while True:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        screen.blit(BACKGROUND, (0,0))
        screen.blit(GAME_NAME,\
            ((settings.SCREEN_WIDTH/2 - GAME_NAME.get_width()/2),50))

        if play_collision:
            screen.blit(PLAY_BUTTON_RED,\
            ((settings.SCREEN_WIDTH/2 - PLAY_BUTTON.get_width()/2),400))
            if click:
                game()

        else:
            screen.blit(PLAY_BUTTON,\
            ((settings.SCREEN_WIDTH/2 - PLAY_BUTTON.get_width()/2),400))
        
        
        play_collision = False
        if play_rect.collidepoint(mouse_x,mouse_y):
            play_collision = True


        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                   click = True 


        pygame.display.update()

def game():
    running = True

    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()

    archer = Archer()
    archer_group.add(archer)
    create_balloons(15)
    while running:
        clock.tick(settings.CLOCK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:

                if event.key == settings.MOVE_UP_KEY:
                    archer.moving_up = True
                if event.key == settings.MOVE_DOWN_KEY:
                    archer.moving_down = True
                if event.key == settings.SHOOT_KEY:
                    if archer.shooting == False:
                        if(archer.arrows == 0):
                            pass
                        else:
                            archer.shooting = True
                    if archer.shooting == True:
                        if archer.shooting_ready:
                            archer.shoot()
                            create_arrow_shooting(archer.archer_position[0], archer.archer_position[1])

                if event.key == K_ESCAPE:
                    running = False

                    
            if event.type == KEYUP:
                if event.key == settings.MOVE_UP_KEY:
                    archer.moving_up = False
                if event.key == settings.MOVE_DOWN_KEY:
                    archer.moving_down = False

        
        blit_game_static_elements(screen)
        update_sprites()

        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))
        screen.blit(arrow_count_label,(1305, 27))
        
        check_balloon_hit(arrow_group,balloon_group)
        draw_sprites(screen)

        if check_game_over():
            game_over()

        pygame.display.update()

def game_over():
    running = True
    current_image = 0

    opaque_surface = pygame.Surface((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
    opaque_surface.set_alpha(180)
    opaque_surface.fill((0, 0, 0))
    while running:
        clock.tick(settings.CLOCK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    current_image = 0

        blit_game_static_elements(screen)
        screen.blit(opaque_surface,(0, 0))
        if current_image <=32:
            screen.blit(GAME_OVER[int(current_image)],\
                (settings.SCREEN_WIDTH/2 - GAME_OVER[int(current_image)].get_width()/2, -700))

        else:
            screen.blit(STATIC_GAME_OVER,\
                (settings.SCREEN_WIDTH/2 - STATIC_GAME_OVER.get_width()/2,\
                398))

        current_image += settings.GAME_OVER_ANIMATION_SPEED
        pygame.display.update()


pygame.init()
pygame.display.set_caption(settings.WINDOW_NAME)


myfont = pygame.font.Font(settings.PIXEL_FONT, 50)

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
icon = pygame.image.load(settings.ICON).convert_alpha()
pygame.display.set_icon(icon)


BACKGROUND = pygame.image.load('Assets/background/background.png').convert()
BACKGROUND = pygame.transform.scale(BACKGROUND, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

FLOOR = (pygame.image.load('Assets/textures/wooden_floor.png')).convert()
FLOOR_CROP = FLOOR.subsurface(0, 0, 40, 200)
FLOOR = pygame.transform.scale(FLOOR_CROP, (150,800))

ARROW_COUNT_MENU = pygame.image.load('Assets/menu/arrow_count.png').convert_alpha()
ARROW_COUNT_MENU = pygame.transform.scale(ARROW_COUNT_MENU, (150,100))

GAME_NAME = pygame.image.load(settings.MENU_TITLE).convert_alpha()
GAME_NAME = pygame.transform.scale(GAME_NAME,settings.MENU_SIZE)

PLAY_BUTTON = pygame.image.load(settings.PLAY_BUTTON).convert()
PLAY_BUTTON = pygame.transform.scale(PLAY_BUTTON,settings.PLAY_BUTTON_SIZE)
PLAY_BUTTON_RED = pygame.image.load(settings.PLAY_BUTTON_RED).convert()
PLAY_BUTTON_RED = pygame.transform.scale(PLAY_BUTTON_RED,settings.PLAY_BUTTON_SIZE)

GAME_OVER_FILE = settings.GAME_OVER
GAME_OVER = []
for image in GAME_OVER_FILE:
    image = pygame.image.load(image).convert_alpha()
    image = pygame.transform.scale(image,(int(settings.GAME_OVER_SCALE*54),\
                int(settings.GAME_OVER_SCALE*154)))
    GAME_OVER.append(image)

STATIC_GAME_OVER = pygame.image.load(settings.STATIC_GAME_OVER).convert_alpha()
STATIC_GAME_OVER = pygame.transform.scale(STATIC_GAME_OVER,\
    ((int(settings.GAME_OVER_SCALE*STATIC_GAME_OVER.get_width()),\
        int(settings.GAME_OVER_SCALE*STATIC_GAME_OVER.get_height()))))


archer_group = pygame.sprite.Group()
archer = Archer()
archer_group.add(archer)

balloon_group = pygame.sprite.Group()
create_balloons(15)


arrow_group = pygame.sprite.Group()
mouse_arrow_testing(False)

clock = pygame.time.Clock()

main_menu()


