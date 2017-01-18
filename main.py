from PPlay.window import *

import time
import random

from tank import tank
from snake import snake
from running import running
from start import start


#game config
window = Window(527,527)
window.set_title("Infinity Games")
rgb = [0,0,255]
window.set_background_color(rgb)
window.update()
MODE = 0
clock = pygame.time.Clock()
delay = 50
GAME_SPEED = 1
tempo = 0

#keyboard
keyboard = Window.get_keyboard()

lastClick=0
score = 0


game = [start(lastClick)]

#tela de game over
def fim(window, last,rgb):
    window.set_background_color([0,0,0])
    window.draw_text("Você fez: " + str(int(score)) + ' pontos', 120, 230, 32, (0, 255, 0), "Arial", True,
                             False)
    window.draw_text('Aperte ENTER', 160, 430, 25, (255, 255, 0), "Arial", True, False)


    if keyboard.key_pressed("ENTER"):
        last = window.last_time
        rgb = [0, 0, 255]
        return 0, window, last,rgb
    else:
        return 9, window, last,rgb


#main
while True:
    window.set_background_color(rgb)

    #menu inicial
    if(MODE == 0):
        #MODE,tempo = start(MODE,select,tempo)
        MODE,tempo = game[0].game(window,MODE,tempo, keyboard,delay)
        score = 0
        GAME_SPEED = 1
        if(MODE == 1):
            game = []
            game.append(snake())
        elif(MODE == 2):
            #running
            game = []
            game.append(running(window))
        elif(MODE == 3):
            # tank
            game = []
            game.append(tank(window.last_time))    


    #snake
    elif(MODE == 1):
        clock.tick(GAME_SPEED*10)
        rgb[0] = 255
        rgb[1] = 255
        score,MODE = game[0].game(delay,score,MODE,window,keyboard)
    #running
    elif(MODE == 2):
        clock.tick(GAME_SPEED * 10)
        rgb[0] = 255
        rgb[1] = 255
        GAME_SPEED,score,MODE  = game[0].game(GAME_SPEED,score,MODE,window,keyboard,delay)
    #tank
    elif(MODE == 3):
        clock.tick(GAME_SPEED * 20)
        rgb[0] = 255
        rgb[1] = 255

        score,MODE = game[0].game(score,MODE,window,keyboard)
        
        
    #game over
    elif(MODE == 9):
        MODE,window, lastClick,rgb = fim(window, lastClick,rgb)
        game = []
        if MODE == 0:
            game.append(start(lastClick))
        

    window.update()
