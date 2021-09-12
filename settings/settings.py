import pygame.locals
import random 

WINDOW_NAME = 'Pixel Bowmaster'
ICON = 'Assets/menu/icon.png'

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

LANGUAGE_EN_US = True
LANGUAGE_PT_BR = False
 

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
TARGET_SPEED = round(random.uniform(2, 3.0), 1)
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

SLIME_EASTER_EGG = ['Assets/slime/slime_easter_egg1.png',
'Assets/slime/slime_easter_egg2.png',
'Assets/slime/slime_easter_egg3.png',
'Assets/slime/slime_easter_egg4.png',
'Assets/slime/slime_easter_egg5.png'
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
ROMAN_SPAWN_NUMBER = 60


CLOUD = ['Assets/cloud/cloud.png']
CLOUD_SPEED = round(random.uniform(2, 2.7), 1)



BRIDGE = 'Assets/textures/wood_floor_bridge.png'
BRIDGE_SPEED = 2.4

WIZARD = ['Assets/wizard/wizard1.png',
'Assets/wizard/wizard2.png',
'Assets/wizard/wizard3.png',
'Assets/wizard/wizard4.png',
'Assets/wizard/wizard5.png',
'Assets/wizard/wizard6.png',
'Assets/wizard/wizard7.png'
]

WIZARD_DEATH = ['Assets/wizard/wizard_death1.png',
'Assets/wizard/wizard_death2.png',
'Assets/wizard/wizard_death3.png',
'Assets/wizard/wizard_death4.png',
'Assets/wizard/wizard_death5.png',
'Assets/wizard/wizard_death6.png',
'Assets/wizard/wizard_death7.png'
]

WIZARD_ANIMATION_SPEED = 0.15
WIZARD_WALKING_SPEED = 2
WIZARD_DEATH_ANIMATION_SPEED = 0.17
WIZARD_CAST_SPEED = 0.06

FIREBALL = ['Assets/fireball/fireball1.png',
'Assets/fireball/fireball2.png',
'Assets/fireball/fireball3.png',
'Assets/fireball/fireball4.png',
'Assets/fireball/fireball5.png',
'Assets/fireball/fireball6.png',
'Assets/fireball/fireball7.png',
'Assets/fireball/fireball8.png'
]

FIREBALL_SPEED = 5
FIREBALL_ANIMATION_SPEED = 0.15

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

OPTIONS = ('Assets/menu/options.png')
OPTIONS_RED = ('Assets/menu/options_red.png')

CONTROLS = ('Assets/menu/controls.png')
CONTROLS_RED = ('Assets/menu/controls_red.png')

ABOUT = ('Assets/menu/about.png')
ABOUT_RED = ('Assets/menu/about_red.png')

BUTTON_BACKGROUND = ('Assets/menu/button_background.png')

PT_BUTTON = ('Assets/menu/pt.png')
PT_BUTTON_RED = ('Assets/menu/pt_red.png')

US_BUTTON = ('Assets/menu/us.png')
US_BUTTON_RED = ('Assets/menu/us_red.png') 

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
ABOUT_BACKGROUND = ('Assets/menu/about_background.png')
BUTTON_SCALE = 3.7

AUDIO_BAR = ('Assets/menu/audio_bar.png')
ROTATE_BUTTON = ('Assets/menu/rotate_button_background.png')

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

TEXT_SPEED = 0.30
TEXT_DURATION = 5
TEXT_COLOR = (255, 255, 255)


LANGUAGE = 'pt'
TICKS_PER_CHAR = 5
TEXT_LEVELS = []

TEXT_LEVEL1 = ["I guess it's quite simple, you have a bow and",\
                "there are some balloons, let's check that aim..."]
TEXT_LEVELS.append(TEXT_LEVEL1)
            
TEXT_LEVEL2 = ["Good luck ! It's quite harder"]
TEXT_LEVELS.append(TEXT_LEVEL2)

TEXT_LEVEL3 = ["Help the butterflies escape."]
TEXT_LEVELS.append(TEXT_LEVEL3)

TEXT_LEVEL4 = ["With all that training I hope you can get a bullseye."]
TEXT_LEVELS.append(TEXT_LEVEL4)

TEXT_LEVEL5 = ["Try not to get hit !"]
TEXT_LEVELS.append(TEXT_LEVEL5)

TEXT_LEVEL6 = ["Take care, a more resilient enemy is coming",\
                "hope you can handle it!"]
TEXT_LEVELS.append(TEXT_LEVEL6)

TEXT_LEVEL7 = ['These clouds appear to be soft,',\
                'but they are kind of misleading...']
TEXT_LEVELS.append(TEXT_LEVEL7)

TEXT_LEVEL8 = ['I know you already went through this',\
'but can you keep going ?']
TEXT_LEVELS.append(TEXT_LEVEL8)

TEXT_LEVEL9 = ['This is the deadliest enemy you will find',\
'he can cast spells, be careful.']
TEXT_LEVELS.append(TEXT_LEVEL9)

TEXT_LEVEL10 = ['An army of wizards lies ahead,',\
'is this the final challenge ?.']
TEXT_LEVELS.append(TEXT_LEVEL10)


TEXT_LEVELS_PT = []

TEXT_LEVEL1_PT = ["É muito simples, você tem um arco e há",\
                " alguns balões na tela, vamos testar essa mira..."]
TEXT_LEVELS_PT.append(TEXT_LEVEL1_PT)
            
TEXT_LEVEL2_PT = ["Boa sorte, a dificuldade aumentou!"]
TEXT_LEVELS_PT.append(TEXT_LEVEL2_PT)

TEXT_LEVEL3_PT = ["Ajude as borboletas a escaparem!"]
TEXT_LEVELS_PT.append(TEXT_LEVEL3_PT)

TEXT_LEVEL4_PT = ["Com todo esse treinamento, eu espero que pelo",\
                    "menos você consiga acertar o centro do alvo..."]
TEXT_LEVELS_PT.append(TEXT_LEVEL4_PT)

TEXT_LEVEL5_PT = ["Tente não ser atingido."]
TEXT_LEVELS_PT.append(TEXT_LEVEL5_PT)

TEXT_LEVEL6_PT = ["Cuidado!!! Um inimigo mais resiliente se encontra logo",\
                "à frente, espero que você consiga lidar com eles!"]
TEXT_LEVELS_PT.append(TEXT_LEVEL6_PT)

TEXT_LEVEL7_PT = ['Essas nuvens parecem bem macias,',\
                'mas não se deixe enganar pela aparência...']
TEXT_LEVELS_PT.append(TEXT_LEVEL7_PT)

TEXT_LEVEL8_PT = ['Sei que você já passou por isso,',\
                    'mas será que sua mira está afiada mesmo ?']
TEXT_LEVELS_PT.append(TEXT_LEVEL8_PT)

TEXT_LEVEL9_PT = ['Cuidado, a frente se encontra um inimigo poderoso,',\
                    'ele consegue até mesmo lançar magias.']
TEXT_LEVELS_PT.append(TEXT_LEVEL9_PT)

TEXT_LEVEL10_PT = ['Há um exercito de magos logo a frente,',\
                    'seria esse o desafio final ?']
TEXT_LEVELS_PT.append(TEXT_LEVEL10_PT)




ABOUT_TEXT = "This is a short game that I’ve decided to make after youtube started to recommend some "\
"game jam videos, they were so interesting and since I was learning programing, specifically "\
"python, I decided to make a little game with pygame as a learning method and to have some"\
"fun. After some thinking I decided to make my own remake of an old windows game that I used to play with "\
"my father. The original game is called Bow and Arrow. All of the pixel art was created "\
"by me, except the romans, which was made by my brother Rafael made for my game. This game can be found at "\
"https://vodiniz.itch.io/pixel-bowmaster or at https://github.com/vodiniz/Archer_Game"\
"\n"\
"\n"\
"Music: '8 Bit Power' By HeatleyBros https://youtu.be/UJ9NbyPFTvY"

ABOUT_TEXT_PT = "Esse é um pequeno jogo que eu decidi fazer logo após o youtube me recomendar alguns "\
"vídeos sobre game jams, os vídeos foram muito interessantes e como eu estava "\
"aprendendo programação, python para ser mais específico, eu decidi criar um pequeno "\
"jogo com o pygame como uma maneira de me aprofundar em programação, o jogo que eu "\
"escolhi fazer foi um remake de um antigo jogo de windows, que eu costumava jogar com "\
"meu pai, o jogo se chama Bow and Arrow. Toda a pixel art foi criada por mim, exceto o "\
"romano, que foi criado pelo meu irmão Rafael. O jogo pode ser encontrado em https://vodiniz.itch.io/pixel-bowmaster "\
"ou https://github.com/vodiniz/Archer_Game"\
"\n"\
"\n"\
"Music: '8 Bit Power' By HeatleyBros https://youtu.be/UJ9NbyPFTvY"


MENU_MUSIC = ('Assets/music/8bit_power.wav')
BUTTON_SELECTION_AUDIO = ('Assets/music/button_selection.wav')
TEXT_EFFECT = ('Assets/music/text_effect.wav')
MENU_VOLUME = 0.009