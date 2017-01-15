from PPlay.sprite import *
import random

#classe de tanks
class enemy_tank():
    tank_images = ['Tank/tank2.png', 'Tank/tank2_1.png', 'Tank/tank2_2.png', 'Tank/tank2_3.png']
    velocidade = 1
    moves = 0

    #construtor
    def __init__(self):
        x = random.randint(0, 527)
        y = random.randint(0, 527)

        if x < 527 / 2 and y < 527 / 2:
            self.direcao = 2
            self.sprite = Sprite(self.tank_images[2], 1)

        elif x >= 527 / 2 and y < 527 / 2:
            self.direcao = 3
            self.sprite = Sprite(self.tank_images[3], 1)

        elif x <= 527 / 2 and y >= 527 / 2:
            self.direcao = 1
            self.sprite = Sprite(self.tank_images[1], 1)

        else:
            self.direcao = 0
            self.sprite = Sprite(self.tank_images[0], 1)

        self.sprite.set_total_duration(0)
        self.sprite.set_position(x, y)

        self.ajustar()

    #ajusta a posição
    def ajustar(self):

        ajuste = False

        if (self.sprite.x < 0):
            self.sprite.x = 0
            ajuste = True
        elif (self.sprite.x > 527 - self.sprite.height):
            self.sprite.x = 527 - self.sprite.height
            ajuste = True
        if (self.sprite.y < 0):
            self.sprite.y = 0
            ajuste = True
        elif (self.sprite.y > 527 - self.sprite.height):
            self.sprite.y = 527 - self.sprite.height
            ajuste = True


        self.sprite.draw()

        return ajuste

    #move o tank
    def move(self, deltaX=0, deltaY=0):
        x = self.sprite.x+deltaX
        y = self.sprite.y+deltaY
        random.seed()
        if random.randint(0,30) > 28 and self.moves >=3:
            self.direcao = random.randint(0,3)
            self.mudarDirecao(self.direcao)
            self.moves = 0
        else:    
            if self.direcao == 0:
                self.sprite.set_position(x, y - self.velocidade)
            elif self.direcao == 1:
                self.sprite.set_position(x + self.velocidade, y)
            elif self.direcao == 2:
                self.sprite.set_position(x, y + self.velocidade)
            else:
                self.sprite.set_position(x - self.velocidade, y)

            self.moves = self.moves + 1    

        if (self.ajustar()):
            mudou  = False
            while not mudou:
                x = random.randint(0,3)
                if self.direcao != x:
                    self.direcao = x
                    mudou = True
                    self.mudarDirecao(x)

    #função para auxiliar a mudança de direção
    def mudarDirecao(self,dire):
        pos_x = self.sprite.x
        pos_y = self.sprite.y
        self.sprite = Sprite(self.tank_images[dire], 1)
        self.sprite.set_total_duration(0)
        self.sprite.set_position(pos_x, pos_y)
        self.sprite.draw()

    #retorna o sprite do tanl
    def spr(self):
        return self.sprite