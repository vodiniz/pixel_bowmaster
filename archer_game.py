import pygame, random

from pygame import mixer
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

        self.popped_images = [(pygame.image.load('Assets/balloon/popped_balloon_sprite_2.png')).convert_alpha(),
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
        self.popped_animation = pygame.image.load('Assets/balloon/popped_balloon_sprite_1.png').convert_alpha()
        self.popped_animation = pygame.transform.scale(self.popped_animation, (50 , 50))
        self.popped_animation_count = 0
        
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
            if self.popped_animation_count < 15:
                self.image = self.popped_animation
                self.popped_animation_count += 1
                pass
            else:
                if self.current_image >= len(self.popped_images):
                    self.current_image = 0
                self.image = self.popped_images[int(self.current_image)]

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

        self.inverted = inverted
        self.current_image = 0
        self.image = self.butterfree_images[self.current_image]

        self.rect = self.image.get_rect()
        self.popped = False

        if inverted:
            self.speed = - settings.BUTTERFREE_SPEED
            self.butterfree_position = [xpos, -random.randint(100, 700)]
        else:
            self.speed =  settings.BUTTERFREE_SPEED
            self.butterfree_position = [xpos, random.randint(900, 1500)]
        
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
        


class Slime(pygame.sprite.Sprite):

    def __init__(self,xpos, bridge):
        pygame.sprite.Sprite.__init__(self)
        self.slime_images = []

        for image in settings.SLIME:
            convert_image = pygame.image.load(image).convert_alpha()
            convert_image = pygame.transform.scale(convert_image,(120 , 120))
            self.slime_images.append(convert_image)

        self.dead_images = []

        for image in settings.SLIME_DEATH:
            convert_image = pygame.image.load(image).convert_alpha()
            convert_image = pygame.transform.scale(convert_image,(120 , 120))
            self.dead_images.append(convert_image)

        
        self.speed = -settings.SLIME_SPEED
        self.current_image = 0
        self.image = self.slime_images[self.current_image]
        self.rect = self.image.get_rect()
        self.dead = False

        self.slime_position = [xpos, bridge*200 + 140 -self.rect[3]]
        self.rect[0] = self.slime_position[0]
        self.rect[1] = self.slime_position[1]
        slime_mask = pygame.mask.from_surface(self.image)

    def kill_off_screen(self):
        if self.rect[0] <= -200:
            self.kill()


    def update(self):
        if self.dead:
            self.current_image += settings.SLIME_DEATH_ANIMATION_SPEED
        else:
            self.current_image += settings.SLIME_ANIMATION_SPEED

        if self.dead:
            if self.current_image >= len(self.dead_images):
                self.current_image = len(self.dead_images)-1
                self.kill()
            self.image = self.dead_images[int(self.current_image)]
        
        else:
            if self.current_image >= len(self.slime_images):
                self.current_image = 0
            self.image = self.slime_images[int(self.current_image)]
        
        self.kill_off_screen()
        if self.dead:
            pass
        else:
            self.slime_position[0] += self.speed
        self.rect[0] = self.slime_position[0]

    
class Roman(pygame.sprite.Sprite):

    def __init__(self,xpos, bridge):
        pygame.sprite.Sprite.__init__(self)
        self.roman_images = []

        for image in settings.ROMAN:
            convert_image = pygame.image.load(image).convert_alpha()
            convert_image = pygame.transform.scale(convert_image,(200 , 200))
            self.roman_images.append(convert_image)

        self.dead_images = []

        for image in settings.ROMAN_DEATH:
            convert_image = pygame.image.load(image).convert_alpha()
            convert_image = pygame.transform.scale(convert_image,(200 , 200))
            self.dead_images.append(convert_image)

        
        self.speed = -settings.ROMAN_SPEED
        self.current_image = 0
        self.image = self.roman_images[self.current_image]
        self.rect = self.image.get_rect()
        self.dead = False

        self.roman_position = [xpos, bridge*200 + 180 -self.rect[3]]
        self.rect[0] = self.roman_position[0]
        self.rect[1] = self.roman_position[1]
        self.health = 2
        roman_mask = pygame.mask.from_surface(self.image)

    def kill_off_screen(self):
        if self.rect[0] <= -200:
            self.kill()


    def update(self):
        if self.dead:
            self.current_image += settings.ROMAN_DEATH_ANIMATION_SPEED
        else:
            self.current_image += settings.ROMAN_ANIMATION_SPEED

        if self.dead:
            if self.current_image >= len(self.dead_images):
                self.current_image = len(self.dead_images)-1
                self.kill()
            self.image = self.dead_images[int(self.current_image)]
        
        else:
            if self.current_image >= len(self.roman_images):
                self.current_image = 0
            self.image = self.roman_images[int(self.current_image)]
        
        self.kill_off_screen()
        if self.dead:
            pass
        else:
            self.roman_position[0] += self.speed
        self.rect[0] = self.roman_position[0]


class Clouds(pygame.sprite.Sprite):

    def __init__(self,ypos,positive_speed):
        pygame.sprite.Sprite.__init__(self)
        
        self.cloud_images = []

        for image in settings.CLOUD:
            convert_image = pygame.image.load(image).convert_alpha()
            convert_image = pygame.transform.scale(convert_image,(50, 130))
            self.cloud_images.append(convert_image)
    
        self.current_image = 0
        self.image = self.cloud_images[self.current_image]
 
        if positive_speed:  
            self.speed = settings.CLOUD_SPEED
        else:
            self.speed = -settings.CLOUD_SPEED

        self.cloud_position = [500,ypos]

        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = self.cloud_position
        cloud_mask = pygame.mask.from_surface(self.image)


    def update(self):
        self.current_image += 0
        
        if self.current_image >= len(self.cloud_images):
            self.current_image = 0
        self.image = self.cloud_images[int(self.current_image)]

        if self.rect[1] <= 0 or self.rect[1] >= 800 - self.rect[3]:
            self.speed = -self.speed
        self.cloud_position[1] -= self.speed
        self.rect[1] = self.cloud_position[1]
        

        
class Bridge(pygame.sprite.Sprite):

    def __init__(self, pos_y, final_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(settings.BRIDGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (1250,190))
        self.rect = self.image.get_rect()
        self.position = [150,pos_y]
        self.done = False
        self.speed = -settings.BRIDGE_SPEED
        self.final_pos = final_pos
        self.rect[0], self.rect[1] = self.position[0], self.position[1]

    def update(self):
        if self.final_pos >= self.position[1]:
            self.done = True
        
        if self.done:
            pass
        else:
            self.position[1] += self.speed
            self.rect[1] = int(self.position[1])


class Wizard(pygame.sprite.Sprite):
    def __init__(self,xpos,bridge):
        pygame.sprite.Sprite.__init__(self)

        self.wizard_images = []
        
        for image in settings.WIZARD:
            convert_image = pygame.image.load(image).convert_alpha()
            convert_image = pygame.transform.scale(convert_image,(150, 150))
            self.wizard_images.append(convert_image)

        self.dead_images = []

        for image in settings.WIZARD_DEATH:
            convert_image = pygame.image.load(image).convert_alpha()
            convert_image = pygame.transform.scale(convert_image,(150 , 150))
            self.dead_images.append(convert_image)

        self.current_image = random.randint(0,len(self.wizard_images)-1)

        self.image = self.wizard_images[self.current_image]
        self.rect = self.image.get_rect()

        self.dead = False
        self.shooting = True
        self.walking = True

        self.wizard_position = [xpos + 300, bridge*200 + 150 -self.rect[3]]
        self.final_position = xpos
        self.rect[0] = self.wizard_position[0]
        self.rect[1] = self.wizard_position[1]


    def update(self):
        if self.dead:
            self.current_image += settings.WIZARD_DEATH_ANIMATION_SPEED
        else:
            self.current_image += settings.WIZARD_CAST_SPEED

        if self.dead:
            if self.current_image >= len(self.dead_images):
                self.current_image = len(self.dead_images)-1
                self.kill()
            self.image = self.dead_images[int(self.current_image)]
        else:
            if self.current_image >= len(self.wizard_images):
                self.current_image = 0
                self.shooting = True
            else:
                self.shooting = False

            self.image = self.wizard_images[int(self.current_image)]

        if self.walking:
            if self.wizard_position[0] <= self.final_position:
                self.walking = False

            self.wizard_position[0] -= settings.WIZARD_WALKING_SPEED
            self.rect[0] = self.wizard_position[0]
            

 




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

class Fireball(pygame.sprite.Sprite):

    def __init__(self,xpos,ypos):
        pygame.sprite.Sprite.__init__(self)

        self.fireball_images = []
        
        for image in settings.FIREBALL:
            convert_image = pygame.image.load(image).convert_alpha()
            convert_image = pygame.transform.scale(convert_image,(120, 60))
            self.fireball_images.append(convert_image)

        self.speed = -settings.FIREBALL_SPEED

        self.current_image = 0


        self.image = self.fireball_images[self.current_image]

        self.rect = self.image.get_rect()

        self.fireball_position = [xpos,ypos]
        self.rect[0], self.rect[1] = xpos, ypos

        fireball_mask = pygame.mask.from_surface(self.image)

    def is_fireball_off_screen(self):
        if self.fireball_position[0] < -150:
            self.kill()
        
    def update(self):
        self.current_image += settings.FIREBALL_ANIMATION_SPEED
        if self.current_image >= len(self.fireball_images):
            self.current_image = 0

        self.image = self.fireball_images[int(self.current_image)]
        self.fireball_position[0] += self.speed
        self.rect[0] = self.fireball_position[0]
        self.is_fireball_off_screen()




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
        self.name = blue_image.split('/')[-1]
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
        self.audio_played = 1
        

    def update(self, mouse_x, mouse_y, click):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            self.image = self.red_image
            if self.audio_played:
                button_selection.play()
                self.audio_played = 0
            if click:
                self.clicked = True
        else:
            self.image = self.blue_image
            self.clicked = False
            self.audio_played = 1

class Slide_button(pygame.sprite.Sprite):
    def __init__(self,audio_bar_rect, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(settings.ROTATE_BUTTON).convert()
        self.image = pygame.transform.scale(self.image, (10, 50))
        #self.moving = False
        self.max_volume = 0.7
        self.min_volume = 0.007
    
        self.position = [audio_bar_rect[0] + settings.MENU_VOLUME * audio_bar_rect[2]/self.max_volume , ypos]

        self.rect = self.image.get_rect()
        self.rect[0] =  self.position[0]
        self.rect[1] = self.position[1]

    def update(self, audio_bar_rect, offset):
        if self.rect[0] - offset < audio_bar_rect[0]:
            self.rect[0] = audio_bar_rect[0]
        elif self.rect[0] + offset > audio_bar_rect[0] + audio_bar_rect[2] - self.rect[2]:
            self.rect[0] = audio_bar_rect[0] + audio_bar_rect[2] - self.rect[2]
        else:
            self.rect [0] = self.rect[0] + offset
        settings.MENU_VOLUME = (self.rect[0] - audio_bar_rect[0]) * self.max_volume / audio_bar_rect[2]
        pygame.mixer.music.set_volume(settings.MENU_VOLUME)

    

 
class Level_text(pygame.sprite.Sprite):
    def __init__(self,text_list,myfont):
        pygame.sprite.Sprite.__init__(self)
        self.font = myfont
        self.text_color = settings.TEXT_COLOR
        self.current_char = 0
        self.text_speed = settings.TEXT_SPEED
        self.text_duration = settings.TEXT_DURATION
        self.text_list = text_list
        self.char_lenght = 0
        self.second_word = False
        self.showing_text = []
        for text in text_list:
            self.char_lenght += len(text)

        self.image = pygame.image.load(settings.BUTTON_BACKGROUND).convert()
        self.background_label = pygame.image.load(settings.BUTTON_BACKGROUND).convert()
        if len(self.text_list) > 1:
            self.image = pygame.transform.scale(self.image, (900,100))
            self.background_label = pygame.transform.scale(self.background_label, (900,100))
        else:
            self.image = pygame.transform.scale(self.image, (900,70))
            self.background_label = pygame.transform.scale(self.background_label, (900,70))

        for text in self.text_list:
            self.showing_text.append('')
        self.rect = self.image.get_rect()
        self.rect[0] = settings.SCREEN_WIDTH/2 - self.rect[2]/2
        self.rect[1] = 30

    def update(self,tick_count,mixer_channel):
        
        if len(self.text_list) > 1:
            if not self.second_word:
                if self.current_char > len(self.text_list[0]):
                    self.current_char = 0
                    self.second_word = True
                elif len(self.showing_text[0]) <= self.current_char:# and current_char <= len(self.text_list[0]):
                    self.showing_text[0] += self.text_list[0][int(self.current_char)]
                    if mixer_channel.get_busy():
                        pass
                    else:
                        text_effect.play(maxtime = int((len(self.text_list[0])/self.text_speed)*1000), fade_ms = 200)
                
                self.current_char += self.text_speed

            else:
                if self.current_char > len(self.text_list[1]):
                    self.current_char = 0
                    self.second_word = True
                elif len(self.showing_text[1]) <= self.current_char:
                    #text_effect.play(-1)
                    self.showing_text[1] += self.text_list[1][int(self.current_char)]
                    if mixer_channel.get_busy():
                        pass
                    else:
                        text_effect.play(maxtime = int((len(self.text_list[1])/self.text_speed)*1000 - 500), fade_ms = 200)

                
                self.current_char += self.text_speed
            
            self.image.blit(self.background_label,(0,0))

            rendered_text = self.font.render(self.showing_text[0], 1, self.text_color)
            self.image.blit(rendered_text,(self.rect[2]/2 - rendered_text.get_width()/2,25))
           
            rendered_text2 = self.font.render(self.showing_text[1], 1, self.text_color)
            self.image.blit(rendered_text2,(self.rect[2]/2 - rendered_text2.get_width()/2,\
             35 + rendered_text.get_height()))
        
            if tick_count > settings.TICKS_PER_CHAR * len(self.text_list[0] + self.text_list[1]):
                self.kill()

        else:
            if self.current_char > len(self.text_list[0]):
                #mixer_channel.pause()
                pass
            elif len(self.showing_text[0]) <= self.current_char:
                self.showing_text[0] += self.text_list[0][int(self.current_char)]
                if mixer_channel.get_busy():
                    pass
                else:
                    text_effect.play(maxtime = int((len(self.text_list[0])/self.text_speed)*1000), fade_ms = 300)
            
            self.current_char += self.text_speed
            self.image.blit(self.background_label,(0,0))

            rendered_text = self.font.render(self.showing_text[0], 1, self.text_color)
            self.image.blit(rendered_text,(self.rect[2]/2 - rendered_text.get_width()/2,\
                self.rect[3]/2 - rendered_text.get_height()/2))

            if tick_count > settings.TICKS_PER_CHAR * 1.3 * len(self.text_list[0]):
                self.kill()


class State:
    def __init__(self):
        self.menu = False
        self.level_selection = False
        self.level1 = False
        self.level2 = False
        self.level3 = False
        self.level4 = False
        self.level5 = False
        self.level6 = False
        self.level7 = False
        self.level8 = False
        self.level9 = False
        self.level10 = False
        self.options = False
        self.about = False
        self.game_over = False
        self.text_list = []
        self.testing = False
        self.about_text = ""

def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = pygame.image.load(settings.ABOUT_BACKGROUND).get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            word_height += 12
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.



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

def check_simple_collision(arrow_group, slime_group):
    result = pygame.sprite.groupcollide(arrow_group, slime_group, False, False, \
        pygame.sprite.collide_mask)
    if len(result) > 0:
        for arrow,slime_list in result.items():
            for slime in slime_list:
                if slime.dead: 
                    pass
                else:
                    arrow.kill()
                    slime.dead = True
                    slime.current_image = 0
        
        return True
    else:
        return False

def check_roman_collision(arrow_group, roman_group):
    result = pygame.sprite.groupcollide(arrow_group, roman_group, False, False, \
        pygame.sprite.collide_mask)
    if len(result) > 0:
        for arrow,roman_list in result.items():
            for roman in roman_list:
                if roman.dead: 
                    pass
                else:
                    roman.health -= 1
                    arrow.kill()
                    if roman.health == 0:
                        roman.dead = True
                        roman.current_image = 0

def check_fireball_player_collision(fireball_group, archer):
    
    for fireball in fireball_group:
        if fireball.rect[0] <= 200:
            if pygame.sprite.collide_mask(fireball, archer):
                return True
    
def check_fireball_arrow_collision(arrow_group, fireball_group):
    pygame.sprite.groupcollide(arrow_group, fireball_group, True, True, \
        pygame.sprite.collide_mask)


def game_over_colission(player_group, enemy_group):
    if pygame.sprite.groupcollide(player_group, enemy_group, False, False, \
        pygame.sprite.collide_mask):
        return True
    else:
        return False
    

def check_target_center_hit(arrow_group, target_group):
    result = pygame.sprite.groupcollide(arrow_group, target_group, False, False, \
        pygame.sprite.collide_mask)

    if len(result) > 0:
        for arrow,target_list in result.items():
            for target in target_list:
                low_middle_point = target.rect[1] + target.rect[3] + 32
                high_middle_point = target.rect[1] + target.rect[3] + 56
                offset = 2
                arrow_tip_x = arrow.rect[0] + (3/4)*arrow.rect[2]
                arrow_tip_y = arrow.rect[1] + arrow.rect[3] + 15
                if arrow_tip_y > low_middle_point - 5 and arrow_tip_y < high_middle_point + offset:
                    if arrow_tip_x + 20 > target.rect[0] + (1/3)*target.rect[2] and arrow_tip_x< 1330 :
                        target.kill()
                        return True
        

def check_cloud_collision(arrow_group, cloud_group):
    result = pygame.sprite.groupcollide(arrow_group, cloud_group, False, False, \
        pygame.sprite.collide_mask)
    if len(result) > 0:
        for arrow,cloud_list in result.items():
            arrow_tip = arrow.rect[0] + (3/4)*arrow.rect[2]
            if arrow_tip > 555:
                pass
            else:
                arrow.kill()


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

def create_bridges(bridge_group):
    
    for i in range(4):
        bridge = Bridge(900+(250*i),200*i)
        bridge_group.add(bridge)

def create_slimes(slime_group, slime_number,easter_egg):
 
    if slime_number > 0:
        while len(slime_group) <= 7:
            new_slime = Slime(random.randint(1300,2000),random.randint(0,3))
            if pygame.sprite.spritecollide(new_slime, slime_group, False):
                new_slime.kill()
            else:
                if easter_egg == slime_number:
                    image_list = []
                    for image in settings.SLIME_EASTER_EGG:
                        convert_image = pygame.image.load(image).convert_alpha()
                        convert_image = pygame.transform.scale(convert_image,(120 , 120))
                        image_list.append(convert_image)
                    new_slime.slime_images = image_list
                    slime_group.add(new_slime)
                    slime_number -= 1
                else:
                    slime_group.add(new_slime)
                    slime_number -= 1
    return slime_number

def create_romans(roman_group, roman_number):
 
    if roman_number > 0:
        while len(roman_group) <= 6:
            new_roman = Roman(random.randint(1300,2300),random.randint(0,3))
            if pygame.sprite.spritecollide(new_roman, roman_group, False):
                new_roman.kill()
            else:
                roman_group.add(new_roman)
                roman_number -= 1


    return roman_number

def create_wizards(wizard_group):
    for bridge_number in range(4):
        new_wizard = Wizard(1100, bridge_number)
        wizard_group.add(new_wizard)


def create_clouds(cloud_group):
    cloud_1 = Clouds(random.randint(0,100), True)
    cloud_group.add(cloud_1)
    cloud_2 = Clouds(random.randint(500,600), False)
    cloud_group.add(cloud_2)

def wizard_cast_fireball(wizard_group,fireball_group):
    for wizard in wizard_group:
        if wizard.shooting:
            new_fireball = Fireball(wizard.rect[0] + 40, wizard.rect[1] + 50)
            fireball_group.add(new_fireball)



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
    popped_enemies = 0
    if player.arrows == 0 and len(arrow_group) == 0:
        for enemy in enemy_group:
            if enemy.popped:
                popped_enemies = 1
            if popped_enemies >= len(enemy_group):
                return False
        return True
    else:
        return False

def check_bridge_done(bridge_group):
    bridge_done_count = 0
    for bridge in bridge_group:
        if bridge.done:
            bridge_done_count += 1
    if bridge_done_count == 4:
        return True
    else:
        return False


def recreate_testing_arrow(arrow_group):
    if len(arrow_group) == 0:
        mouse_arrow_testing(True)

def go_next_next_level(enemy_group):
    if len(enemy_group) == 0:
        return True

def create_level_buttons(button_group):
    count = 0
    second_count = 0
    coord = [0,0]
    for blue,red in zip(settings.BUTTON_NUMBERS, settings.BUTTON_NUMBERS_RED):
        count_rest = count % 3

        if count <3:
            second_count = 0
        if count < 6 and count >= 3:
            second_count = 1
        if count > 5 and count < 9:
            second_count = 2
        if count == 9:
            second_count = 3

        coord = [400 + count_rest*300, 200 + second_count*100]
        new_button = Button(blue, red, coord[0], coord[1])
        button_group.add(new_button)
   

        count += 1



def play_menu_music(music_file,play):
    if play:
        pygame.mixer.music.load(settings.MENU_MUSIC)
        pygame.mixer.music.set_volume(settings.MENU_VOLUME) 
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()

def update_language():
    if settings.LANGUAGE == 'pt':
        return settings.TEXT_LEVELS_PT, settings.ABOUT_TEXT_PT
    else:
        return settings.TEXT_LEVELS, settings. ABOUT_TEXT
        



def main_menu():
    clock.tick(settings.CLOCK)

    click = False
    running = True
    button_group.empty()


    play_button = Button(settings.PLAY_BUTTON, settings.PLAY_BUTTON_RED,\
        settings.SCREEN_WIDTH/2 , 400)
    button_group.add(play_button)
    
    level_selection_button = Button(settings.LEVELS, settings.LEVELS_RED,\
        settings.SCREEN_WIDTH/2 , 400+ play_button.rect[3] + 10)
    button_group.add(level_selection_button)

    options_button = Button(settings.OPTIONS, settings.OPTIONS_RED,\
        settings.SCREEN_WIDTH/2 , 400 + 2*play_button.rect[3] + 20)
    button_group.add(options_button)

    about_button = Button(settings.ABOUT, settings.ABOUT_RED,\
        settings.SCREEN_WIDTH/2 , 400 + 3*play_button.rect[3] + 30)
    button_group.add(about_button)


    play_menu_music(settings.MENU_MUSIC, True)
   
    
    while running:
        if state.level1:
            state.level1 = False
            game_level_1()

        if state.level2:
            game_level_2()
            state.level2 = False

        if state.level3:
            game_level_3()
            state.level3 = False

        if state.level4:
            game_level_4()
            state.level4 = False

        if state.level5:
            game_level_5()
            state.level5 = False

        if state.level6:
            game_level_6()
            state.level6 = False

        if state.level7:
            game_level_7()
            state.level7 = False

        if state.level8:
            game_level_8()
            state.level8 = False

        if state.level9:
            game_level_9()
            state.level9 = False

        if state.level10:
            game_level_10()
            state.level10 = False
        

        if state.level_selection:
            state.level_selection= False
            level_selection()
            running = False

        if state.options:
            state.options = False
            options()
            running = False
        
        if state.about:
            state.about = False
            about()
            running = False



        mouse_x, mouse_y = pygame.mouse.get_pos()

        screen.blit(BACKGROUND, (0,0))
        screen.blit(GAME_NAME,\
            ((settings.SCREEN_WIDTH/2 - GAME_NAME.get_width()/2),50))



        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                   click = True 
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()


        button_group.update(mouse_x, mouse_y, click)
        button_group.draw(screen)

        if play_button.clicked:
            state.level1 = True
            play_button.clicked = False

        if level_selection_button.clicked:
            level_selection_button.clicked = False
            state.level_selection = True

        if options_button.clicked:
            options_button.clicked = False
            state.options = True

        if about_button.clicked:
            about_button.clicked = False
            state.about = True

        pygame.display.update()



def level_selection():
    clock.tick(settings.CLOCK)

    click = False
    button_group.empty()
    running = True
    menu_button = Button(settings.MENU_BUTTON, settings.MENU_BUTTON_RED,\
        settings.SCREEN_WIDTH/2 , 650)
    button_group.add(menu_button)

    level_description_color = (255, 255, 255)
    choose_level_description_1 = myfont.render('CHOOSE WHICH LEVEL YOU', 1, level_description_color)
    choose_level_description_2 = myfont.render('WOULD LIKE TO PLAY',1,level_description_color)
    button_background = pygame.image.load(settings.BUTTON_BACKGROUND).convert()
    button_background = pygame.transform.scale(button_background,(\
         (choose_level_description_1.get_width()+60, 2*choose_level_description_1.get_height() + 50)))
    create_level_buttons(button_group)

    while running:
        clock.tick(settings.CLOCK)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(BACKGROUND, (0,0))
        screen.blit(button_background,(settings.SCREEN_WIDTH/2 - choose_level_description_1.get_width()/2 - 30, 20))
        screen.blit(choose_level_description_1,(settings.SCREEN_WIDTH/2 - choose_level_description_1.get_width()/2, 50))
        screen.blit(choose_level_description_2,(settings.SCREEN_WIDTH/2 - choose_level_description_2.get_width()/2, 90))
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True 

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    state.level_selection = False

        if menu_button.clicked:
            running = False

        for button in button_group:
            if button.name == 'button_number1.png':
                if button.clicked:
                    game_level_1()
                    button.clicked = False

            if button.name == 'button_number2.png':
                if button.clicked:
                    game_level_2()
                    button.clicked = False

            if button.name == 'button_number3.png':
                if button.clicked:
                    game_level_3()
                    button.clicked = False

            if button.name == 'button_number4.png':
                if button.clicked:
                    game_level_4()
                    state.level5 = False
                    button.clicked = False

            if button.name == 'button_number5.png':
                if button.clicked:
                    game_level_5()
                    button.clicked = False

            if button.name == 'button_number6.png':
                if button.clicked:
                    game_level_6()
                    button.clicked = False
            if button.name == 'button_number7.png':
                if button.clicked:
                    game_level_7()
                    button.clicked = False
            if button.name == 'button_number8.png':
                if button.clicked:
                    game_level_8()
                    button.clicked = False
            if button.name == 'button_number9.png':
                if button.clicked:
                    game_level_9()
                    button.clicked = False
            if button.name == 'button_number10.png':
                if button.clicked:
                    game_level_10()
                    button.clicked = False
            
            

        state.level1 = False
        button_group.update(mouse_x, mouse_y, click)
        button_group.draw(screen)

        pygame.display.update()


def options():
    clock.tick(settings.CLOCK)
    click = False
    volume_draging = False
    button_group.empty()
    slide_button_group.empty()

    running = True
    font_color = (0, 0, 0)
   


    options_button = Button(settings.OPTIONS, settings.OPTIONS_RED,\
        settings.SCREEN_WIDTH/2 , 80)
    options_button.blue_image = pygame.transform.scale(options_button.blue_image,\
        (int(1.5*options_button.rect[2]), int(1.5*options_button.rect[3])))
    options_button.red_image = pygame.transform.scale(options_button.red_image,\
        (int(1.5*options_button.rect[2]), int(1.5*options_button.rect[3])))
    options_button.rect[2] = options_button.blue_image.get_width()
    options_button.rect[3] = options_button.blue_image.get_height()

    options_button.rect[0] = settings.SCREEN_WIDTH/2 - options_button.blue_image.get_width()/2
    button_group.add(options_button)
    audio_text = myfont.render('Music Volume', 1, font_color)
    language_text = myfont.render('Language', 1, font_color)
    audio_bar = pygame.image.load(settings.AUDIO_BAR).convert()
    audio_bar = pygame.transform.scale(audio_bar,(400,20))
    audio_bar_rect = audio_bar.get_rect()
    audio_bar_rect[0] = 200 + audio_text.get_width() + 50

    volume_slide = Slide_button(audio_bar_rect,350 + audio_text.get_height()/2 - audio_bar.get_height()/2 - 5)
    slide_button_group.add(volume_slide)
    offset = 0

    pt_button = Button(settings.PT_BUTTON, settings.PT_BUTTON_RED, 300 + audio_text.get_width() + 50,440)
    button_group.add(pt_button)
    us_button = Button(settings.US_BUTTON, settings.US_BUTTON_RED, 300 + audio_text.get_width() + 200, 440)
    button_group.add(us_button)

    while running:
        clock.tick(settings.CLOCK)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(BACKGROUND, (0,0))
        screen.blit(audio_text, (200,350))
        screen.blit(language_text, (200, 450))
        screen.blit(audio_bar, (200 + audio_text.get_width() + 50,\
             350 + audio_text.get_height()/2))



        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if volume_slide.rect.collidepoint(mouse_x, mouse_y):
                        offset = volume_slide.rect[0] - mouse_x
                        volume_draging = True
                    click = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    volume_draging = False

            if event.type == pygame.MOUSEMOTION:
                if volume_draging:
                    volume_slide.rect[0] = mouse_x + offset

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    state.level_selection = False

        for button in button_group:
            if button.name == 'pt.png':
                if button.clicked:
                    settings.LANGUAGE = 'pt'
                    state.text_list, state.about_text = update_language()
            if button.name == 'us.png':
                if button.clicked:
                    settings.LANGUAGE = 'us'
                    state.text_list, state.about_text = update_language()



        button_group.update(mouse_x, mouse_y, click)
        slide_button_group.update(audio_bar_rect, 0)

        button_group.draw(screen)
        slide_button_group.draw(screen)
        pygame.display.update()


def about():
    clock.tick(settings.CLOCK)
    click = False
    volume_draging = False
    button_group.empty()
    slide_button_group.empty()

    running = True
    font_color = (0, 0, 0)
   

    about_button = Button(settings.ABOUT, settings.ABOUT_RED,\
        settings.SCREEN_WIDTH/2 , 20)
    about_button.blue_image = pygame.transform.scale(about_button.blue_image,\
        (int(1.5*about_button.rect[2]), int(1.5*about_button.rect[3])))
    about_button.red_image = pygame.transform.scale(about_button.red_image,\
        (int(1.5*about_button.rect[2]), int(1.5*about_button.rect[3])))
    about_button.rect[2] = about_button.blue_image.get_width()
    about_button.rect[3] = about_button.blue_image.get_height()

    about_button.rect[0] = settings.SCREEN_WIDTH/2 - about_button.blue_image.get_width()/2
    button_group.add(about_button)
    about_font = pygame.font.Font(settings.PIXEL_FONT, 28)

    text_background = pygame.image.load(settings.ABOUT_BACKGROUND).convert()
    
    while running:
        clock.tick(settings.CLOCK)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(BACKGROUND, (0,0))
        screen.blit(text_background, (100, 140))    
        blit_text(screen, state.about_text, [150, 190], about_font )


        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    volume_draging = False


            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    state.level_selection = False




        button_group.update(mouse_x, mouse_y, click)

        button_group.draw(screen)
        slide_button_group.draw(screen)
        pygame.display.update()


def game_level_1():
    running = True
    tick_count = 0

    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()
    level_text_group.empty()

    mouse_arrow_testing(state.testing)
    archer = Archer()
    archer_group.add(archer)
    create_balloons(15)
    level_text1 = Level_text(state.text_list[0], text_font)
    level_text_group.add(level_text1)
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
                    state.level1 = False

                    
            if event.type == KEYUP:
                if event.key == settings.MOVE_UP_KEY:
                    archer.moving_up = False
                if event.key == settings.MOVE_DOWN_KEY:
                    archer.moving_down = False

        
        blit_game_static_elements(screen)
        update_sprites()
        level_text_group.update(tick_count, dialogue)

        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))
        screen.blit(arrow_count_label,(1305, 27))
        
        check_enemy_hit(arrow_group,balloon_group)
        draw_sprites(screen)
        level_text_group.draw(screen)
  

        if go_next_next_level(balloon_group):
            state.level2 = True
            running = False

        if check_game_over(archer, arrow_group, balloon_group):
            if state.level2:
                pass
            else:
                game_over()
                state.level4 = False
                running = False


        
        tick_count += 1
        pygame.display.update()


def game_level_2():
    running = True
    tick_count = 0

    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()
    level_text_group.empty()

    mouse_arrow_testing(state.testing)
    archer = Archer()
    archer_group.add(archer)
    create_random_balloons(15)

    level_text1 = Level_text(state.text_list[1], text_font)
    level_text_group.add(level_text1)

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
                    state.level2 = False

                    
            if event.type == KEYUP:
                if event.key == settings.MOVE_UP_KEY:
                    archer.moving_up = False
                if event.key == settings.MOVE_DOWN_KEY:
                    archer.moving_down = False

        blit_game_static_elements(screen)
        update_sprites()
        level_text_group.update(tick_count, dialogue)
        
        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))
        screen.blit(arrow_count_label,(1305, 27))

        check_enemy_hit(arrow_group, balloon_group)
        draw_sprites(screen)
        level_text_group.draw(screen)
  
        if go_next_next_level(balloon_group):
            state.level3 = True
            running = False
    
        if check_game_over(archer, arrow_group, balloon_group):
            if state.level3:
                pass
            else:
                game_over()
                running = False
                state.level2 = False

        tick_count += 1
        pygame.display.update()


def game_level_3():
    running = True
    tick_count = 0
    
    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()
    butterfree_group.empty()
    level_text_group.empty()

    mouse_arrow_testing(state.testing)
    archer = Archer()
    archer_group.add(archer)
    create_butterfree(15)
    level_text3 = Level_text(state.text_list[2], text_font)
    level_text_group.add(level_text3)

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
                    state.level3 = False

                    
            if event.type == KEYUP:
                if event.key == settings.MOVE_UP_KEY:
                    archer.moving_up = False
                if event.key == settings.MOVE_DOWN_KEY:
                    archer.moving_down = False

        blit_game_static_elements(screen)

        archer_group.update()
        butterfree_group.update()
        arrow_group.update()
        level_text_group.update(tick_count, dialogue)

        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))
        screen.blit(arrow_count_label,(1305, 27))

        check_enemy_hit(arrow_group,butterfree_group)
        
        archer_group.draw(screen)
        butterfree_group.draw(screen)
        arrow_group.draw(screen)
        level_text_group.draw(screen)

        if go_next_next_level(butterfree_group):
            state.level4 = True
            running = False
  
        if check_game_over(archer, arrow_group, butterfree_group):
            if state.level4:
                pass
            else:
                game_over()
                state.level3 = False
                running = False

        tick_count += 1
        pygame.display.update()



def game_level_4():
    running = True
    tick_count = 0
    
    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()
    target_group.empty()
    level_text_group.empty()

    mouse_arrow_testing(state.testing)
    archer = Archer()
    archer_group.add(archer)
    target = Target()
    target_group.add(target)
    level_text4 = Level_text(state.text_list[3], text_font)
    level_text_group.add(level_text4)


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
                    state.level4 = False

                    
            if event.type == KEYUP:
                if event.key == settings.MOVE_UP_KEY:
                    archer.moving_up = False
                if event.key == settings.MOVE_DOWN_KEY:
                    archer.moving_down = False

        blit_game_static_elements(screen)

        archer_group.update()
        target_group.update()
        arrow_group.update()
        level_text_group.update(tick_count, dialogue)
        
        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))
        screen.blit(arrow_count_label,(1305, 27))

        check_target_center_hit(arrow_group, target_group)

        
        archer_group.draw(screen)
        target_group.draw(screen)
        arrow_group.draw(screen)
        level_text_group.draw(screen)
  

        if go_next_next_level(target_group):
            state.level5 = True
            running = False

        if archer.arrows == 0 and len(arrow_group) == 0:
            if state.level5:
                pass
            else:
                game_over()
                state.level4 = False
                running = False

       
        pygame.display.update()
        tick_count += 1


def game_level_5():
    running = True
    bridge_done = False
    bridge_count = 0
    tick_count = 0
        
    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()
    bridge_group.empty()
    slime_group.empty()
    level_text_group.empty()

    mouse_arrow_testing(state.testing)
    archer = Archer()
    archer_group.add(archer)
    create_bridges(bridge_group)
    slime_count = settings.SLIME_SPAWN_NUMBER
    easter_egg = random.randint(0,slime_count -1)

    level_text5 = Level_text(state.text_list[4], text_font)
    level_text_group.add(level_text5)


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
                    state.level5 = False

                    
            if event.type == KEYUP:
                if event.key == settings.MOVE_UP_KEY:
                    archer.moving_up = False
                if event.key == settings.MOVE_DOWN_KEY:
                    archer.moving_down = False

        blit_game_static_elements(screen)

        

        if tick_count > 500:
            slime_count = create_slimes(slime_group,slime_count,easter_egg)
        
  
        archer_group.update()
        butterfree_group.update()
        arrow_group.update()
        bridge_group.update()
        slime_group.update()
        level_text_group.update(tick_count, dialogue)
        
        

        bridge_group.draw(screen)
        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))

        check_simple_collision(arrow_group,slime_group)
        
        archer_group.draw(screen)
        arrow_group.draw(screen)
        slime_group.draw(screen)
        screen.blit(ARROW_COUNT_MENU, ( settings.SCREEN_WIDTH - ARROW_COUNT_MENU.get_width(), 0))
        screen.blit(arrow_count_label,(1305, 27))
        level_text_group.draw(screen)


        if go_next_next_level(slime_group):
            if tick_count > 700:
                state.level6 = True
                running = False
  
        if game_over_colission(archer_group,slime_group):
            if state.level6:
                pass
            else:
                state.level5 = False
                game_over()
                running = False

        tick_count += 1
        pygame.display.update()


def game_level_6():
    running = True
    bridge_done = False
    bridge_count = 0
    tick_count = 0
    
    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()
    bridge_group.empty()
    roman_group.empty()

    mouse_arrow_testing(state.testing)
    archer = Archer()
    archer_group.add(archer)
    create_bridges(bridge_group)
    roman_count = settings.ROMAN_SPAWN_NUMBER
    level_text6 = Level_text(state.text_list[5], text_font)
    level_text_group.add(level_text6)


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
                    state.level6 = False

                    
            if event.type == KEYUP:
                if event.key == settings.MOVE_UP_KEY:
                    archer.moving_up = False
                if event.key == settings.MOVE_DOWN_KEY:
                    archer.moving_down = False

        blit_game_static_elements(screen)

        

        if tick_count > 500:
            roman_count = create_romans(roman_group,roman_count)
        
  
        archer_group.update()
        arrow_group.update()
        bridge_group.update()
        roman_group.update()
        level_text_group.update(tick_count, dialogue)
        

        bridge_group.draw(screen)
        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))

        check_roman_collision(arrow_group,roman_group)
        
        archer_group.draw(screen)
        arrow_group.draw(screen)
        roman_group.draw(screen)
        screen.blit(ARROW_COUNT_MENU, ( settings.SCREEN_WIDTH - ARROW_COUNT_MENU.get_width(), 0))
        screen.blit(arrow_count_label,(1305, 27))
        level_text_group.draw(screen)


        if go_next_next_level(roman_group):
            if tick_count > 700:
                state.level7 = True
                running = False

        if game_over_colission(archer_group, roman_group):
            if state.level7:
                pass
            else:
                state.level6 = False
                game_over()
                running = False

        tick_count += 1
        pygame.display.update()


def game_level_7():
    running = True
    tick_count = 0
    
    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()
    butterfree_group.empty()
    level_text_group.empty()
    bridge_group.empty()
    roman_group.empty()
    slime_group.empty()
    target_group.empty()
    cloud_group.empty()

    mouse_arrow_testing(state.testing)
    archer = Archer()
    archer_group.add(archer)
    create_butterfree(15)
    level_text7 = Level_text(state.text_list[6], text_font)
    level_text_group.add(level_text7)
    create_clouds(cloud_group)


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
                    state.level3 = False

                    
            if event.type == KEYUP:
                if event.key == settings.MOVE_UP_KEY:
                    archer.moving_up = False
                if event.key == settings.MOVE_DOWN_KEY:
                    archer.moving_down = False

        blit_game_static_elements(screen)

        archer_group.update()
        butterfree_group.update()
        arrow_group.update()
        cloud_group.update()
        level_text_group.update(tick_count, dialogue)

        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))
        screen.blit(arrow_count_label,(1305, 27))

        check_enemy_hit(arrow_group,butterfree_group)
        check_cloud_collision(arrow_group, cloud_group)


        archer_group.draw(screen)
        butterfree_group.draw(screen)
        arrow_group.draw(screen)
        cloud_group.draw(screen)
        level_text_group.draw(screen)

        if go_next_next_level(butterfree_group):
            state.level8 = True
            running = False
  
        if check_game_over(archer, arrow_group, butterfree_group):
            if state.level8:
                pass
            else:
                game_over()
                state.level7 = False
                running = False

        tick_count += 1
        pygame.display.update()


def game_level_8():
    running = True
    tick_count = 0

    
    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()
    target_group.empty()
    level_text_group.empty()
    cloud_group.empty()
    slime_group.empty()
    roman_group.empty()
    bridge_group.empty()
    butterfree_group.empty()


    mouse_arrow_testing(state.testing)
    archer = Archer()
    archer_group.add(archer)
    target = Target()
    target.speed =  target.speed*2.6
    target_group.add(target)
    level_text8 = Level_text(state.text_list[7], text_font)
    level_text_group.add(level_text8)


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
                    state.level4 = False

                    
            if event.type == KEYUP:
                if event.key == settings.MOVE_UP_KEY:
                    archer.moving_up = False
                if event.key == settings.MOVE_DOWN_KEY:
                    archer.moving_down = False

        blit_game_static_elements(screen)

        archer_group.update()
        target_group.update()
        arrow_group.update()
        level_text_group.update(tick_count, dialogue)
        
        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))
        screen.blit(arrow_count_label,(1305, 27))

        if check_target_center_hit(arrow_group, target_group):
            state.level5 = True
            running = False
        
        archer_group.draw(screen)
        target_group.draw(screen)
        arrow_group.draw(screen)
        level_text_group.draw(screen)
  

        if go_next_next_level(target_group):
            state.level9 = True
            running = False

        if archer.arrows == 0 and len(arrow_group) == 0:
            if state.level9:
                pass
            else:
                game_over()
                state.level8 = False
                running = False

       
        pygame.display.update()
        tick_count += 1


def game_level_9():
    running = True
    bridge_done = False
    bridge_counting = True
    tick_count = 0
    
    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()
    bridge_group.empty()
    roman_group.empty()
    cloud_group.empty()
    butterfree_group.empty()
    target_group.empty()
    wizard_group.empty()
    fireball_group.empty()

    mouse_arrow_testing(state.testing)
    archer = Archer()
    archer_group.add(archer)
    create_bridges(bridge_group)
    level_text9 = Level_text(state.text_list[8], text_font)
    level_text_group.add(level_text9)


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
                    state.level9 = False

                    
            if event.type == KEYUP:
                if event.key == settings.MOVE_UP_KEY:
                    archer.moving_up = False
                if event.key == settings.MOVE_DOWN_KEY:
                    archer.moving_down = False

        blit_game_static_elements(screen)
        
        archer_group.update()
        arrow_group.update()
        bridge_group.update()
        wizard_group.update()
        fireball_group.update()

        level_text_group.update(tick_count, dialogue)
        
        if bridge_counting:
            if check_bridge_done(bridge_group):
                new_wizard = Wizard(1100, 2)
                wizard_group.add(new_wizard)
                bridge_counting = False


        bridge_group.draw(screen)
        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))

        check_simple_collision(arrow_group, wizard_group)
        wizard_cast_fireball(wizard_group, fireball_group)
        check_fireball_arrow_collision(arrow_group, fireball_group)
        
        
        archer_group.draw(screen)
        arrow_group.draw(screen)
        wizard_group.draw(screen)
        fireball_group.draw(screen)
        screen.blit(ARROW_COUNT_MENU, ( settings.SCREEN_WIDTH - ARROW_COUNT_MENU.get_width(), 0))
        screen.blit(arrow_count_label,(1305, 27))
        level_text_group.draw(screen)


        if go_next_next_level(wizard_group):
            if tick_count > 700:
                state.level10 = True
                running = False

        if check_fireball_player_collision(fireball_group,archer):
            if state.level10:
                pass
            else:
                state.level9 = False
                game_over()
                running = False

        tick_count += 1
        pygame.display.update()


def game_level_10():
    running = True
    bridge_done = False
    bridge_counting = True
    tick_count = 0
    
    archer_group.empty()
    balloon_group.empty()
    arrow_group.empty()
    bridge_group.empty()
    roman_group.empty()
    cloud_group.empty()
    butterfree_group.empty()
    target_group.empty()
    wizard_group.empty()
    fireball_group.empty()

    mouse_arrow_testing(state.testing)
    archer = Archer()
    archer_group.add(archer)
    create_bridges(bridge_group)
    level_text10 = Level_text(state.text_list[9], text_font)
    level_text_group.add(level_text10)


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
                    state.level9 = False

                    
            if event.type == KEYUP:
                if event.key == settings.MOVE_UP_KEY:
                    archer.moving_up = False
                if event.key == settings.MOVE_DOWN_KEY:
                    archer.moving_down = False

        blit_game_static_elements(screen)
        
        archer_group.update()
        arrow_group.update()
        bridge_group.update()
        wizard_group.update()
        fireball_group.update()

        level_text_group.update(tick_count, dialogue)
        
        if bridge_counting:
            if check_bridge_done(bridge_group):
                create_wizards(wizard_group)
                bridge_counting = False


        bridge_group.draw(screen)
        arrow_count_label = myfont.render(str(archer.arrows),1,(255,255,255))

        check_simple_collision(arrow_group, wizard_group)
        wizard_cast_fireball(wizard_group, fireball_group)
        check_fireball_arrow_collision(arrow_group, fireball_group)
        
        
        archer_group.draw(screen)
        arrow_group.draw(screen)
        wizard_group.draw(screen)
        fireball_group.draw(screen)
        screen.blit(ARROW_COUNT_MENU, ( settings.SCREEN_WIDTH - ARROW_COUNT_MENU.get_width(), 0))
        screen.blit(arrow_count_label,(1305, 27))
        level_text_group.draw(screen)


        if go_next_next_level(wizard_group):
            if tick_count > 700:
                running = False

        if check_fireball_player_collision(fireball_group,archer):
            if state.level7:
                pass
            else:
                state.level9 = False
                game_over()
                running = False

        tick_count += 1
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
            state.level1 = True
        if menu_button.clicked:
            running = False
            state.level1 = False
        pygame.display.update()


pygame.init()
pygame.mixer.init()

pygame.display.set_caption(settings.WINDOW_NAME)


myfont = pygame.font.Font(settings.PIXEL_FONT, 50)
text_font = pygame.font.Font(settings.PIXEL_FONT, 25)

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
language = settings.LANGUAGE





dialogue = pygame.mixer.Channel(2)

button_selection = pygame.mixer.Sound(settings.BUTTON_SELECTION_AUDIO)
button_selection.set_volume(0.11)

text_effect = pygame.mixer.Sound(settings.TEXT_EFFECT)
text_effect.set_volume(0.06)



state = State()
state.text_list, state.about_text = update_language()


archer_group = pygame.sprite.Group()
archer = Archer()
archer_group.add(archer)

balloon_group = pygame.sprite.Group()
butterfree_group = pygame.sprite.Group()
target_group = pygame.sprite.Group()
arrow_group = pygame.sprite.Group()
button_group = pygame.sprite.Group()
slime_group = pygame.sprite.Group()
bridge_group = pygame.sprite.Group()
roman_group = pygame.sprite.Group()
level_text_group = pygame.sprite.Group()
cloud_group = pygame.sprite.Group()
wizard_group = pygame.sprite.Group()
fireball_group = pygame.sprite.Group()
slide_button_group = pygame.sprite.Group()

clock = pygame.time.Clock()

gaming = True

while True:
    main_menu()


