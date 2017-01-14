from PPlay.sprite import *

#classe de tiros
class shot():
    direcao = 0
    velocidade = 3

    #construtor
    def __init__(self,imagem_path,direc,x,y):

        self.direcao = direc
        self.sprite = Sprite(imagem_path,1)
        self.sprite.set_total_duration(0)
        if direc == 0:
            x = x - self.sprite.width / 2
            y = y - self.sprite.height / 2
        elif direc == 1:
            x = x - self.sprite.width / 2
            y = y - self.sprite.height / 2
        elif direc == 2:
            x = x - self.sprite.width / 2
            y = y + self.sprite.height / 2
        else:
            x = x - self.sprite.width / 2
            y = y - self.sprite.height/2

        self.sprite.set_position(x,y)
        self.sprite.draw()

    #atualiza posição
    def atualizar(self):
        x = self.sprite.x
        y = self.sprite.y

        if self.direcao == 0:
            self.sprite.set_position(x,y-self.velocidade)
        elif self.direcao == 1:
            self.sprite.set_position(x+self.velocidade,y)
        elif self.direcao == 2:
            self.sprite.set_position(x,y+self.velocidade)
        else:
            self.sprite.set_position(x-self.velocidade,y)
        self.sprite.draw()

    #retorna a poição
    def posicao(self):
        return self.sprite.x, self.sprite.y

    #retorna o sprite
    def spr(self):
        return self.sprite

