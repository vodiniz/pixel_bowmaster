import pygame, random
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
        if self.popped:
            if self.rect[1] > 800:
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

        if self.is_off_screen():
            if self.popped:
                self.kill()
            else:
                self.balloon_position[1] = 900
                

        self.rect[1] = self.balloon_position[1]


class Butterfree(pygame.sprite.Sprite):

    def __init__(self,xpos,inverted):
        pygame.sprite.Sprite.__init__(self)
        
        self.butterfree_images = []

        for image in settings.BUTTERFREE:
            convert_image = pygame.image.load(image).convert_alpha()
            convert_image = pygame.transform.scale(convert_image,(50 , 50))
            self.butterfree_images.append(convert_image)


        self.flying_butterfree = []

        for image in settings.FLYING_BUTTERFREE:
            convert_image = pygame.image.load(image).convert_alpha()
            convert_image = pygame.transform.scale(convert_image,(50 , 50))
            self.flying_butterfree.append(convert_image)

        self.current_image = 0
        self.image = self.butterfree_images[self.current_image]

        self.rect = self.image.get_rect()
        self.popped = False

        if inverted:
            self.speed = - settings.BUTTERFREE_SPEED
            self.butterfree_position = [xpos, -random.randint(100, 500)]
        else:
            self.speed =  settings.BUTTERFREE_SPEED
            self.butterfree_position = [xpos, random.randint(900, 1300)]
        
        self.rect[0] = self.butterfree_position[0]
        self.rect[1] = self.butterfree_position[1]


        
        butterfree_mask = pygame.mask.from_surface(self.image)


    def is_off_screen(self):
        if self.rect[1] <= -200 or self.rect[1] >= 1000:
            return True
        if self.popped:
            if self.rect[1] > 800:
                return True
        if self.rect[0] < 0:
            return True
        else:
            return False
                

    def update(self):
        self.current_image += settings.BUTTERFREE_ANIMATION_SPEED

        if self.popped == True:
            if self.current_image >= len(self.flying_butterfree):
                self.current_image = 0
            self.image = self.flying_butterfree[int(self.current_image)]


        else:
            if self.current_image >= len(self.butterfree_images):
                self.current_image = 0
            self.image = self.butterfree_images[int(self.current_image)]

        if self.is_off_screen():
            if self.popped:
                self.kill()
            else:
                if self.rect[1] > 800 and self.speed > 0 :
                    self.speed = -settings.BUTTERFREE_SPEED
                if self.rect[1] < 0 and self.speed < 0:
                    self.speed = settings.BUTTERFREE_SPEED


        if self.popped:
            if self.speed > 0:
                self.butterfree_position[0] += -2*self.speed
                self.butterfree_position[1] += -self.speed
            else:
                self.butterfree_position[0] += 2*self.speed
                self.butterfree_position[1] += self.speed

        else:
            self.butterfree_position[1] += self.speed

        self.rect[0] = self.butterfree_position[0]
        self.rect[1] = self.butterfree_position[1]


class Target(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.target_images = []

        for image in settings.TARGET:
            convert_image = pygame.image.load(image).convert_alpha()
            convert_image = pygame.transform.scale(convert_image,(58 , 140))
            self.target_images.append(convert_image)
    
        self.current_image = 0
        self.image = self.target_images[self.current_image]
        self.speed = settings.TARGET_SPEED
        self.target_position = [1300,100]

        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = self.target_position
        target_mask = pygame.mask.from_surface(self.image)


    def update(self):
        self.current_image += settings.BUTTERFREE_ANIMATION_SPEED
        
        if self.current_image >= len(self.target_images):
            self.current_image = 0
        self.image = self.target_images[int(self.current_image)]

        if self.rect[1] < 100 or self.rect[1]>650:
            self.speed = -self.speed

        self.target_position[1] -= self.speed
        self.rect[1] = self.target_position[1]
        

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

    def is_arrow_off_screen(self):
        if self.arrow_position[0] > 1600:
            return True
        else:
            return False
        
    def update(self):
        self.arrow_position = pygame.mouse.get_pos()[0]-self.rect[2]/2,\
            pygame.mouse.get_pos()[1]-self.rect[3]/2
        self.rect[0],self.rect[1] = self.arrow_position



class Button(pygame.sprite.Sprite):
    def __init__(self, blue_image, red_image, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)

        self.blue_image = pygame.image.load(blue_image).convert()
        self.blue_image = pygame.transform.scale(self.blue_image,\
         (int(settings.BUTTON_SCALE*self.blue_image.get_width()), int(settings.BUTTON_SCALE*self.blue_image.get_height())))

        self.red_image = pygame.image.load(red_image).convert()
        self.red_image = pygame.transform.scale(self.red_image,\
         (int(settings.BUTTON_SCALE*self.red_image.get_width()), int(settings.BUTTON_SCALE*self.red_image.get_height())))

        self.image = self.blue_image
        self.position = [xpos - self.image.get_width()/2,ypos]
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = self.position[0], self.position[1]
        self.clicked = False

    def update(self, mouse_x, mouse_y, click):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            self.image = self.red_image
            if click:
                self.clicked = True
        else:
            self.image = self.blue_image
            self.clicked = False

 
class State:
    def __init__(self):
        self.menu = False
        self.game = False
        self.level2 = False
        self.level3 = False
        self.game_over = False


def create_arrow_shooting(xpos, ypos):
    new_arrow = Arrow(xpos, ypos)
    arrow_group.add(new_arrow) 


def check_enemy_hit(arrow_group, balloon_group):

    result = pygame.sprite.groupcollide(arrow_group, balloon_group, False, False, \
        pygame.sprite.collide_mask)
    if len(result) > 0:
        for arrow,balloon_list in result.items():
            for balloon in balloon_list:
                balloon_middle = balloon.rect[0] + balloon.rect[2]/2
                arrow_tip = arrow.rect[0] + (3/4)*arrow.rect[2]
                if arrow_tip < balloon_middle:
                    balloon.popped = True

def check_target_center_hit(arrow_group, target_group):
    result = pygame.sprite.groupcollide(arrow_group, target_group, False, False, \
        pygame.sprite.collide_mask)

    # DE 11 A 18 NO ASEPRITE, TENHO 140 DE ALTURA NORMALMENTE. DE BAIXO PARA CIMA 32 E 53
    if len(result) > 0:
        for arrow,target_list in result.items():
            for target in target_list:
                low_middle_point = target.rect[1] + target.rect[3] + 32
                high_middle_point = target.rect[1] + target.rect[3] + 56
                offset = 2
                arrow_tip_x = arrow.rect[0] + (3/4)*arrow.rect[2]
                arrow_tip_y = arrow.rect[1] + arrow.rect[3] + 15
                #print(low_middle_point,'>', arrow_tip_y,'>',high_middle_point)
                if arrow_tip_y > low_middle_point - 5 and arrow_tip_y < high_middle_point + offset:
                    #print (arrow_tip_x)
                    if arrow_tip_x + 20 > target.rect[0] + (1/3)*target.rect[2] and arrow_tip_x< 1330 :
                        return True
        


def create_balloons(balloon_number):
    for i in range(balloon_number):
        new_balloon = Balloon(settings.FIRST_BALLOON_DISTANCE+i*50)
        balloon_group.add(new_balloon)

def create_random_balloons(balloon_number):
    for i in range(balloon_number):
        new_balloon = Balloon(settings.FIRST_BALLOON_DISTANCE+i*50)
        new_balloon.balloon_speed = round(random.uniform(1.5,2), 1)
        new_balloon.balloon_position[1] = random.randint(900,1200)
        balloon_group.add(new_balloon)

def create_butterfree(number):
    for i in range(number):
        new_enemy = Butterfree(settings.FIRST_BUTTERFREE_DISTANCE+i*50, random.randint(0,1))
        butterfree_group.add(new_enemy)

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


def check_game_over(player, arrow_group, enemy_group):
    if player.arrows == 0 and len(arrow_group) == 0:
            return True
    else:
        return False

def go_next_next_level(enemy_group):
    if len(enemy_group) == 0:
        return True



def main_menu():
    clock.tick(settings.CLOCK)

    play_collision = False
    click = False

    play_rect = PLAY_BUTTON.get_rect()
    play_rect[0] = (settings.SCREEN_WIDTH/2 - PLAY_BUTTON.get_width()/2)
    play_rect[1] = 400
    while True:
        if state.game:
            state.game = False
            game()
            state.game = False
        if state.level2 == True:
            game_level_2()
            state.level2 = False
        if state.level3 == True:
            game_level_3()
            state.level3 = False


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

    mouse_arrow_testing(True)
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
        
        check_enemy_hit(arrow_group,balloon_group)
        draw_sprites(screen)
  
        if check_game_over(archer, arrow_group, balloon_group):
            game_over()
            running = False

        if go_next_next_level(balloon_group):
            state.level2 = True
            running = False

        

        pygame.display.update()


def game_level_2():
    running = True
    print('level 2')

    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()

    mouse_arrow_testing(True)
    archer = Archer()
    archer_group.add(archer)
    create_random_balloons(15)

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

        check_enemy_hit(arrow_group,balloon_group)
        draw_sprites(screen)
  
        if check_game_over(archer, arrow_group, balloon_group):
            game_over()
            running = False

        if go_next_next_level(balloon_group):
            state.level3 = True
            running = False
        pygame.display.update()


def game_level_3():
    running = True
    print('level 3')

    
    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()

    mouse_arrow_testing(True)
    archer = Archer()
    archer_group.add(archer)
    create_butterfree(3)

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

        archer_group.update()
        butterfree_group.update()
        arrow_group.update()
        
        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))
        screen.blit(arrow_count_label,(1305, 27))

        check_enemy_hit(arrow_group,butterfree_group)
        
        archer_group.draw(screen)
        butterfree_group.draw(screen)
        arrow_group.draw(screen)
  
        if check_game_over(archer, arrow_group, butterfree_group):
            game_over()
            running = False

        if go_next_next_level(butterfree_group):
            state.level3 = True
            running = False
        pygame.display.update()



def game_level_4():
    running = True
    print('level 4')

    
    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()

    mouse_arrow_testing(True)
    archer = Archer()
    archer_group.add(archer)
    target = Target()
    target_group.add(target)


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

        archer_group.update()
        target_group.update()
        arrow_group.update()
        
        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))
        screen.blit(arrow_count_label,(1305, 27))

        if check_target_center_hit(arrow_group, target_group):
            print('bullseye')
        
        archer_group.draw(screen)
        target_group.draw(screen)
        arrow_group.draw(screen)
  
        if check_game_over(archer, arrow_group, target_group):
            game_over()
            running = False

        if go_next_next_level(target_group):
            state.level3 = True
            running = False
        pygame.display.update()

def game_over():
    running = True
    current_image = 0
    
    opaque_surface = pygame.Surface((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
    opaque_surface.set_alpha(180)
    opaque_surface.fill((0, 0, 0))

    button_group = pygame.sprite.Group()
    try_button = Button(settings.TRY_AGAIN_BUTTON, settings.TRY_AGAIN_BUTTON_RED,\
        settings.SCREEN_WIDTH/2 , 500)

    menu_button = Button(settings.MENU_BUTTON, settings.MENU_BUTTON_RED,\
        settings.SCREEN_WIDTH/2 , 650)
    button_group.add(try_button)
    button_group.add(menu_button)

    while running:
        clock.tick(settings.CLOCK)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        blit_game_static_elements(screen)
        screen.blit(opaque_surface,(0, 0))
        if current_image <=32:
            screen.blit(GAME_OVER[int(current_image)],\
                (settings.SCREEN_WIDTH/2 - GAME_OVER[int(current_image)].get_width()/2, -900))

        else:
            screen.blit(STATIC_GAME_OVER,\
                (settings.SCREEN_WIDTH/2 - STATIC_GAME_OVER.get_width()/2,\
                198))
        


        current_image += settings.GAME_OVER_ANIMATION_SPEED
        
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                   click = True 
        
        button_group.update(mouse_x, mouse_y, click)
        button_group.draw(screen)

        if try_button.clicked:
            running = False
            state.game = True
        if menu_button.clicked:
            running = False
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

state = State()

archer_group = pygame.sprite.Group()
archer = Archer()
archer_group.add(archer)

balloon_group = pygame.sprite.Group()

butterfree_group = pygame.sprite.Group()

target_group = pygame.sprite.Group()

arrow_group = pygame.sprite.Group()

clock = pygame.time.Clock()

gaming = True

while True:
    game_level_4()
    main_menu()


