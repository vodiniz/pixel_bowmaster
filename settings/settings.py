import pygame.locals

WINDOW_NAME = 'Pixel Bowmaster'
ICON = 'Assets/menu/icon.png'

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
 

ARROW_COUNT_LEVEL_1 = 15
ARCHER_STARTING_POSITION = [20,20]
ARCHER_SHOOTING_ANIMATION_SPEED = 0.10
ARCHER_IDLE_ANIMATION_SPEED = 0.07
ARCHER_MOVING_SPEED = 7

BALLOON_SPEED = 1.7
BALLOON_ANIMATION_SPEED = 0.15
FIRST_BALLOON_DISTANCE = 600

ARROW_SPEED = 6.8

BUTTERFREE = ['Assets/butterfree/Butterfree1.png',
'Assets/butterfree/Butterfree2.png',
'Assets/butterfree/Butterfree3.png',
'Assets/butterfree/Butterfree4.png',
'Assets/butterfree/Butterfree5.png',
'Assets/butterfree/Butterfree6.png',
'Assets/butterfree/Butterfree7.png',
'Assets/butterfree/Butterfree8.png',
'Assets/butterfree/Butterfree9.png',
'Assets/butterfree/Butterfree10.png'
]

FLYING_BUTTERFREE = ['Assets/butterfree/flying_buterfree1.png',
'Assets/butterfree/flying_buterfree2.png',
'Assets/butterfree/flying_buterfree3.png',
'Assets/butterfree/flying_buterfree4.png',
'Assets/butterfree/flying_buterfree5.png'
]

BUTTERFREE_SPEED = 1.9
BUTTERFREE_ANIMATION_SPEED = 0.15
FIRST_BUTTERFREE_DISTANCE = 600


TARGET = ['Assets/target/target.png']
TARGET_SPEED = 2.5
TARGET_ANIMATION_SPEED = 3


SLIME = ['Assets/slime/slime1.png',
'Assets/slime/slime2.png',
'Assets/slime/slime3.png',
'Assets/slime/slime4.png',
'Assets/slime/slime5.png'
]

SLIME_DEATH = ['Assets/slime/slime_death1.png',
'Assets/slime/slime_death2.png',
'Assets/slime/slime_death3.png',
'Assets/slime/slime_death4.png',
'Assets/slime/slime_death5.png'
]

SLIME_SPEED = 9
SLIME_ANIMATION_SPEED = 0.2
SLIME_DEATH_ANIMATION_SPEED = 0.11
SLIME_SPAWN_NUMBER = 60

ROMAN = ['Assets/roman/roman_walking1.png',
'Assets/roman/roman_walking2.png',
'Assets/roman/roman_walking3.png',
'Assets/roman/roman_walking4.png'
]


ROMAN_DEATH = ['Assets/roman/roman_dying1.png',
'Assets/roman/roman_dying2.png',
'Assets/roman/roman_dying3.png',
'Assets/roman/roman_dying4.png',
'Assets/roman/roman_dying5.png',
'Assets/roman/roman_dying6.png',
'Assets/roman/roman_dying7.png',
'Assets/roman/roman_dying8.png',
'Assets/roman/roman_dying9.png',
'Assets/roman/roman_dying10.png',
'Assets/roman/roman_dying11.png',
'Assets/roman/roman_dying12.png',
'Assets/roman/roman_dying13.png'

]

ROMAN_SPEED = 5
ROMAN_ANIMATION_SPEED = 0.15
ROMAN_DEATH_ANIMATION_SPEED = 0.17
ROMAN_SPAWN_NUMBER = 45




BRIDGE = 'Assets/textures/wood_floor_bridge.png'
BRIDGE_SPEED = 2.4


CLOCK = 60

MOVE_UP_KEY = pygame.K_UP
MOVE_DOWN_KEY = pygame.K_DOWN
SHOOT_KEY = pygame.K_SPACE


MENU_TITLE = ('Assets/menu/game_title_with_arrow.png')
MENU_SIZE_MULTIPLIER = 6.5
MENU_SIZE = (int(111*MENU_SIZE_MULTIPLIER),int(58*MENU_SIZE_MULTIPLIER))

PIXEL_FONT = ('Assets/font/pixel_font.ttf')






PLAY_BUTTON = ('Assets/menu/Play_button.png')
PLAY_BUTTON_RED = ('Assets/menu/Play_button_red.png')
PLAY_BUTTON_MULTIPLIER = 5
PLAY_BUTTON_SIZE = ((int(55*PLAY_BUTTON_MULTIPLIER), int(20*PLAY_BUTTON_MULTIPLIER)))
PLAY_BUTTON_RED = ('Assets/menu/Play_button_red.png')

LEVELS = ('Assets/menu/levels.png')
LEVELS_RED = ('Assets/menu/levels_red.png')

BUTTON_BACKGROUND = ('Assets/menu/button_background.png')

BUTTON_NUMBERS = [
    ('Assets/menu/button_number/button_number1.png'),
    ('Assets/menu/button_number/button_number2.png'),
    ('Assets/menu/button_number/button_number3.png'),
    ('Assets/menu/button_number/button_number4.png'),
    ('Assets/menu/button_number/button_number5.png'),
    ('Assets/menu/button_number/button_number6.png'),
    ('Assets/menu/button_number/button_number7.png'),
    ('Assets/menu/button_number/button_number8.png'),
    ('Assets/menu/button_number/button_number9.png'),
    ('Assets/menu/button_number/button_number10.png')
]

BUTTON_NUMBERS_RED = [
    ('Assets/menu/button_number/button_number1_red.png'),
    ('Assets/menu/button_number/button_number2_red.png'),
    ('Assets/menu/button_number/button_number3_red.png'),
    ('Assets/menu/button_number/button_number4_red.png'),
    ('Assets/menu/button_number/button_number5_red.png'),
    ('Assets/menu/button_number/button_number6_red.png'),
    ('Assets/menu/button_number/button_number7_red.png'),
    ('Assets/menu/button_number/button_number8_red.png'),
    ('Assets/menu/button_number/button_number9_red.png'),
    ('Assets/menu/button_number/button_number10_red.png')
]

MENU_BUTTON = ('Assets/menu/menu_text.png')
MENU_BUTTON_RED = ('Assets/menu/menu_text_red.png')
TRY_AGAIN_BUTTON = ('Assets/menu/try_again.png')
TRY_AGAIN_BUTTON_RED = ('Assets/menu/try_again_red.png')
BUTTON_SCALE = 4

GAME_OVER = [
'Assets/menu/game_over/game_over_1.png',\
'Assets/menu/game_over/game_over_2.png',\
'Assets/menu/game_over/game_over_3.png',\
'Assets/menu/game_over/game_over_4.png',\
'Assets/menu/game_over/game_over_5.png',\
'Assets/menu/game_over/game_over_6.png',\
'Assets/menu/game_over/game_over_7.png',\
'Assets/menu/game_over/game_over_8.png',\
'Assets/menu/game_over/game_over_9.png',\
'Assets/menu/game_over/game_over_10.png',\
'Assets/menu/game_over/game_over_11.png',\
'Assets/menu/game_over/game_over_12.png',\
'Assets/menu/game_over/game_over_13.png',\
'Assets/menu/game_over/game_over_14.png',\
'Assets/menu/game_over/game_over_15.png',\
'Assets/menu/game_over/game_over_16.png',\
'Assets/menu/game_over/game_over_17.png',\
'Assets/menu/game_over/game_over_18.png',\
'Assets/menu/game_over/game_over_19.png',\
'Assets/menu/game_over/game_over_20.png',\
'Assets/menu/game_over/game_over_21.png',\
'Assets/menu/game_over/game_over_22.png',\
'Assets/menu/game_over/game_over_23.png',\
'Assets/menu/game_over/game_over_24.png',\
'Assets/menu/game_over/game_over_25.png',\
'Assets/menu/game_over/game_over_26.png',\
'Assets/menu/game_over/game_over_27.png',\
'Assets/menu/game_over/game_over_28.png',\
'Assets/menu/game_over/game_over_29.png',\
'Assets/menu/game_over/game_over_30.png',\
'Assets/menu/game_over/game_over_31.png',\
'Assets/menu/game_over/game_over_32.png',\
'Assets/menu/game_over/game_over_33.png'
]



STATIC_GAME_OVER =  'Assets/menu/game_over/game_over.png'
GAME_OVER_ANIMATION_SPEED = 0.3
GAME_OVER_SCALE = 9



