import pygame
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
        self.arrow_position = pygame.mouse.get_pos()[0]-self.rect[2]/2, pygame.mouse.get_pos()[1]-self.rect[3]/2
        self.rect[0],self.rect[1] = self.arrow_position





class StandingBalloon(pygame.sprite.Sprite):

    def __init__(self):
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

        self.balloon_position = [300, 300]
        self.rect = self.image.get_rect()
        self.popped = False
        self.rect[0] = self.balloon_position[0]
        self.rect[1] = self.balloon_position[1]
        
        balloon_mask = pygame.mask.from_surface(self.image)



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
            self.balloon_position[1] -= 0

        self.rect[1] = self.balloon_position[1]



standing_balloon = StandingBalloon()
balloon_group.add(standing_balloon)



mouse_arrow = MouseArrow(pygame.mouse.get_pos()[1],pygame.mouse.get_pos()[1])
arrow_group.add(mouse_arrow)