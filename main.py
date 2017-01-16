from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

import time
import random

from tank import tank
from snake import snake
from running import running


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

#audio
audio_shot = Sound("Sounds/shot.ogg")
audio_shot.set_volume(100)
audio_end = Sound("Sounds/end.ogg")
audio_end.set_volume(100)


#keyboard
keyboard = Window.get_keyboard()
lastClick=0

#first page menu
select= Sprite("gun.png",1)
select.set_total_duration(1000)
select.set_position(100,190)


score = 0


game = []

#tela de inicialização
def start(MODE,select, tempo):
    global lastClick
    window.draw_text("Selecione o Jogo", 130, 60, 40, (255, 255, 0), "Arial", True, True)
    window.draw_text("Snake", 170, 180, 40, (0, 255, 0), "Arial", True, True)
    window.draw_text("Runnning", 170, 260, 40, (255, 0, 0), "Arial", True, True)
    window.draw_text("Tank", 170, 340, 40, (200, 120, 255), "Arial", True, True)
    window.draw_text("Aperte ENTER", 160, 430, 25, (255, 255, 0), "Arial", True, True)

    currentTime = window.last_time
    if currentTime - lastClick > delay+70:
        if (keyboard.key_pressed("ENTER")):
            if (select.y <= 210):
                MODE = 1
            elif (select.y <= 300):
                MODE = 2
            else:
                MODE = 3
            tempo = time.time()
            lastClick = currentTime


        elif (keyboard.key_pressed("UP")):
            if select.y > 200:
                select.y =  select.y - 80
            lastClick = currentTime
        elif (keyboard.key_pressed("DOWN")):
            if select.y < 300:
                select.y = select.y + 80
            lastClick = currentTime


    select.update()
    select.draw()

    return MODE,tempo



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
        MODE,tempo = start(MODE,select,tempo)
        score = 0
        GAME_SPEED = 1
        if(MODE == 1):
            game.append(snake())
        elif(MODE == 2):
            #running
            game.append(running(window))
        elif(MODE == 3):
            # tank
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
        

    window.update()
