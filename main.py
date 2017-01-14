from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

import time
import random
from tankEnemy import enemy_tank
from sho import shot


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

#jogo snake
def snake(pixel,score):
    global MODE

    #para dar a volta na tela
    if pixel['snake'][0].x <= 10 and pixel['direcao'] == 2:
        pixel['snake'][0].set_position(500,pixel['snake'][0].y)
    elif pixel['snake'][0].x >= 500 and pixel['direcao'] == 1:
        pixel['snake'][0].set_position(10,pixel['snake'][0].y)
    elif pixel['snake'][0].y <= 10 and pixel['direcao'] == 3:
        pixel['snake'][0].set_position(pixel['snake'][0].x,500)
    elif pixel['snake'][0].y >= 500 and pixel['direcao'] == 4:
        pixel['snake'][0].set_position(pixel['snake'][0].x,10)


    #configura a direção da snake e faz as movimentações
    x=0
    y=0
    currentTime = window.last_time
    if(currentTime - pixel['ultimoMov'] > delay):
        pixel['ultimoMov'] = currentTime
        if keyboard.key_pressed("RIGHT") and pixel['direcao'] != 2:
            pixel['direcao'] = 1
        elif  keyboard.key_pressed("LEFT") and pixel['direcao'] != 1:
            pixel['direcao'] = 2
        elif  keyboard.key_pressed("UP") and pixel['direcao'] != 4:
            pixel['direcao'] = 3
        elif keyboard.key_pressed("DOWN") and pixel['direcao'] != 3:
            pixel['direcao'] = 4

    if pixel['direcao'] == 1:
        x = 10
    if pixel['direcao'] == 2:
        x = -10
    if pixel['direcao'] == 3:
        y = -10
    if pixel['direcao'] == 4:
        y = 10

    posi_x = pixel["snake"][0].x
    posi_y = pixel["snake"][0].y

    pixel["snake"][0].set_position(posi_x+x, posi_y+y)
    pixel["snake"][0].draw()
    i=0
    for pix in pixel["snake"]:
        if i!=0:
            pos_x_aux=pix.x
            pos_y_aux = pix.y
            pix.set_position(posi_x, posi_y)
            posi_x = pos_x_aux
            posi_y = pos_y_aux
            pix.draw()
        i=1

    if(pixel['snake'][0].collided(red_pix)):
        red_pix.set_position(random.randint(0,512),random.randint(0,512))
        snake_pixel = Sprite("Snake/snake.png", 1)
        snake_pixel.set_total_duration(0)
        snake_pixel.set_position(999, 999)
        pixel['pontos'] = pixel['pontos']+50
        pixel['snake'].append(snake_pixel)
        print(pixel['pontos'])
        score = score + 50
        audio_shot.play()

    for i in range(len(pixel['snake'])):
        if (len(pixel['snake']) > i+4):
            j = i + 4
            while j < (len(pixel['snake'])):
                if pixel['snake'][i].collided(pixel['snake'][j]):
                    MODE = 9
                    audio_end.play()
                j = j +1

    red_pix.draw()
    return score

#configurções iniciais do snake
def startSnake():
    snake_x = [290, 290, 290, 290, 290]
    snake_y = [290, 280, 270, 260, 250]
    red_pix.set_total_duration(0)
    red_pix.set_position(random.randint(0, 512), random.randint(0, 512))
    pixel = {'snake': [], 'direcao': 1, 'ultimoMov': 0, 'pontos': 0}
    i = 0
    for snk in snake_x:
        snake_pixel = Sprite("Snake/snake.png", 1)
        snake_pixel.set_total_duration(0)
        snake_pixel.set_position(snake_x[i], snake_y[i])
        pixel['snake'].append(snake_pixel)
        i = i + 1
    return pixel

#configurações iniciais de running
def startRunning():
    # Running
    car_user = Sprite("Running/car1_1.png", 1)
    car_user.set_total_duration(0)

    car_enemy = Sprite("Running/car2_1.png", 1)
    car_enemy.set_total_duration(0)

    delta = 10

    car_user.set_position(14 * wall_x + delta, window.height - car_user.height)
    car_enemy.set_position(14 * wall_x + delta, -car_enemy.height)
    tempoAnterior = time.time()+10
    score = time.time()

    car_enemies = []
    xx = 0
    while xx < window.height:
        ene = Sprite("Running/car2_1.png", 1)
        ene.set_total_duration(0)
        xx = xx + ene.height * 2 + random.randint(30, 50)
        if (random.randint(0, 1) == 0):
            ene.set_position(14 * wall_x + delta, -xx)
            car_enemies.append(ene)
        else:
            ene.set_position(18 * wall_x + delta, -xx)
            car_enemies.append(ene)
    return matrizMundo, car_user,car_enemies,tempoAnterior,score,delta

#cria a tela de running
def runningWorld(matrizMundo):
    a = open("Running/running.txt", "r")

    for i in a:
        linha = []
        for j in i.split():
            linha.append(int(j))
        matrizMundo.append(linha)
    a.close()

    return matrizMundo

#função jogo de running
def running(tempoAnterior,score,GAME_SPEED,lastClick,delta):
    global MODE


    for i in range(len(matrizMundo)):
        for j in range(len(matrizMundo[0])):
            if int(matrizMundo[i][j]) == 1:
                posX = j*wall_x
                posY = window.height - i*wall_y


                wall.set_position(posX,posY)
                wall.draw()
            else:
                pass
        if i==0:
            lin = matrizMundo[0]
            matrizMundo.remove(lin)
            matrizMundo.append(lin)

    for car in car_enemies:
        car.set_position(car.x, car.y+wall_y)
        car.draw()
        if(car.y-car.height > window.height):
            if random.randint(0,1)==0:
                car.set_position(14 * wall_x + delta, - car.height+20)
            else:
                car.set_position(18 * wall_x + delta, - car.height+20)

        if car.collided(car_user) and car_user.x == car.x:
            MODE = 9
            audio_end.play()
            score = int(time.time()-score)

    currentTime = window.last_time

    if (currentTime - lastClick > delay + 20):
        if keyboard.key_pressed("RIGHT") and car_user.x == 14 * wall_x + delta:
            car_user.set_position(18 * wall_x + delta,car_user.y)
            audio_shot.play()
        elif keyboard.key_pressed("LEFT") and car_user.x == 18 * wall_x + delta:
            car_user.set_position(14 * wall_x + delta,car_user.y)
            audio_shot.play()

    car_user.draw()

    if time.time() - tempoAnterior >= 15:
        tempoAnterior = time.time()
        GAME_SPEED+=10

    return tempoAnterior,score,GAME_SPEED,lastClick




#função jogo de tank
def tank( score,lastClick,direcao, tank_user):
    global MODE
    posi_x = tank_user.x
    posi_y = tank_user.y
    currentTime = window.last_time


    if (currentTime - lastClick > delay+20):
        if keyboard.key_pressed("RIGHT"):
            direcao = 1
            tank_user = Sprite(tank_images[1], 1)
            tank_user.set_position(posi_x+velocidade,posi_y)

        elif keyboard.key_pressed("LEFT"):
            direcao = 3
            tank_user = Sprite(tank_images[3], 1)
            tank_user.set_position(posi_x-velocidade, posi_y)

        elif keyboard.key_pressed("UP"):
            direcao = 0
            tank_user = Sprite(tank_images[0], 1)
            tank_user.set_position(posi_x, posi_y-velocidade)

        elif keyboard.key_pressed("DOWN"):
            direcao = 2
            tank_user = Sprite(tank_images[2], 1)
            tank_user.set_position(posi_x, posi_y+velocidade)

        elif keyboard.key_pressed("SPACE"):
            x = tank_user.x + tank_user.width / 2
            y = tank_user.y + tank_user.height / 2
            shots.append(shot("Tank/shot.png",direcao,x,y))
            audio_shot.play()

        if(tank_user.x<0):
            tank_user.x = 0
        elif(tank_user.x>527-tank_user.height):
            tank_user.x = 527-tank_user.height
        if (tank_user.y < 0):
            tank_user.y = 0
        elif (tank_user.y > 527-tank_user.height):
            tank_user.y = 527-tank_user.height

        lastClick = currentTime

    tank_user.draw()

    if len(enemies) < max_enemies:
        enemies.append(enemy_tank())

    for enemy in enemies:
        enemy.move()

    for sh in shots:
        sh.atualizar()
        x,y = sh.posicao()
        if(x<0 or x>527 or y<0 or y>527):
            shots.remove(sh)

    for sh in shots:
        for en in enemies:
            if sh.spr().collided(en.spr()):
                shots.remove(sh)
                enemies.remove(en)
                score = score + 20

    for sh in shots_enemy:
        sh.atualizar()
        x,y = sh.posicao()
        if(x<0 or x>527 or y<0 or y>527):
            shots_enemy.remove(sh)

    for sh in shots_enemy:
        if sh.spr().collided(tank_user):
            MODE = 9
            audio_end.play()
        else:
            for sh2 in shots:
                if sh.spr().collided(sh2.spr()):
                    shots.remove(sh2)
                    shots_enemy.remove(sh)
                    score = score + 5

    if MODE != 9:
        for en in enemies:
            if tank_user.collided(en.spr()):
                MODE = 9
                audio_end.play()
            else:
                for en2 in enemies:
                     if en2 != en:
                         if en.spr().collided(en2.spr()):
                             if(en.direcao < 2):
                                 en.direcao = en.direcao + 2
                             else:
                                 en.direcao = en.direcao - 2

                             en.move()

                if random.randint(0,50) > 48:
                    x = en.spr().x + en.spr().width / 2
                    y = en.spr().y + en.spr().height / 2
                    shots_enemy.append(shot("Tank/shot2.png", en.direcao, x, y))

    return score, lastClick,direcao, tank_user

#configurações iniciais do jogo tank
def startTank():
    tank_user = Sprite(tank_images[0], 1)
    tank_user.set_total_duration(0)
    tank_user.set_position(100, 300)
    shots = []
    enemies = []
    shots_enemy = []
    max_enemies = 4
    velocidade = 10
    direcao = 0
    return tank_user,shots,enemies,shots_enemy,max_enemies,velocidade,direcao

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
        if(MODE == 1):
            # Snake
            red_pix = Sprite('Snake/pixel.png', 1)
            pixel = startSnake()
        elif(MODE == 2):
            #running
            wall = Sprite("Running/pixel.png")
            wall.set_total_duration(0)
            wall_x = int(window.width / wall.width) / 2 - 3
            wall_y = int(window.height / wall.height) / 2 - 3
            matrizMundo = []
            matrizMundo = runningWorld(matrizMundo)
            matrizMundo, car_user, car_enemies, tempoAnterior,score,delta = startRunning()
        elif(MODE == 3):
            # tank
            tank_images = ['Tank/tank.png', 'Tank/tank_1.png', 'Tank/tank_2.png',
                           'Tank/tank_3.png']
            tank_user, shots, enemies, shots_enemy, max_enemies, velocidade, direcao = startTank()

    #snake
    elif(MODE == 1):
        clock.tick(GAME_SPEED*10)
        rgb[0] = 255
        rgb[1] = 255
        score = snake(pixel,score)
    #running
    elif(MODE == 2):
        clock.tick(GAME_SPEED * 10)
        rgb[0] = 255
        rgb[1] = 255
        tempoAnterior,score,GAME_SPEED,lastClick = running(tempoAnterior,score,GAME_SPEED,lastClick,delta)
    #tank
    elif(MODE == 3):
        clock.tick(GAME_SPEED * 40)
        rgb[0] = 255
        rgb[1] = 255

        if time.time() - tempo >=30:
            max_enemies = max_enemies + 1
            tempo = time.time()
        score,lastClick,direcao, tank_user = tank(score,lastClick,direcao, tank_user)
    #game over
    elif(MODE == 9):
        MODE,window, lastClick,rgb = fim(window, lastClick,rgb)

    window.update()
