from PPlay.sprite import *
from PPlay.sound import *
import random
import time


class running():

	
	
	def __init__(self, window):
		a = open("Running/running.txt", "r")
		self.matrizMundo = []
		for i in a:
			linha = []
			for j in i.split():
				linha.append(int(j))
			self.matrizMundo.append(linha)
		a.close()

		self.wall = Sprite("Running/pixel.png")
		self.wall.set_total_duration(0)
		self.wall_x = int(window.width / self.wall.width) / 2 - 3
		self.wall_y = int(window.height / self.wall.height) / 2 - 3


		self.car_user = Sprite("Running/car1_1.png", 1)
		self.car_user.set_total_duration(0)

		self.car_enemy = Sprite("Running/car2_1.png", 1)
		self.car_enemy.set_total_duration(0)

		self.delta = 10

		self.car_user.set_position(14 * self.wall_x + 
			self.delta, window.height - self.car_user.height)
		self.car_enemy.set_position(14 * self.wall_x + 
			self.delta, -self.car_enemy.height)
		self.tempoAnterior = time.time()+10
		self.intialTime = time.time()

		self.audio = Sound("Sounds/shot.ogg")
		self.audio.set_volume(100)
		self.audio_end = Sound("Sounds/end.ogg")
		self.audio_end.set_volume(100)

		self.car_enemies = []
		xx = 0
		while xx < window.height:
			ene = Sprite("Running/car2_1.png", 1)
			ene.set_total_duration(0)
			xx = xx + ene.height * 2 + random.randint(30, 50)
			if (random.randint(0, 1) == 0):
				ene.set_position(14 * self.wall_x + self.delta, -xx)
				self.car_enemies.append(ene)
			else:
				ene.set_position(18 * self.wall_x + self.delta, -xx)
				self.car_enemies.append(ene)

		self.lastClick = window.last_time			


		

	def move(self,window,keyboard,delay):
		currentTime = window.last_time

		if (currentTime - self.lastClick > delay + 20):
			if keyboard.key_pressed("RIGHT") and \
				self.car_user.x == 14 * self.wall_x + self.delta:
				self.car_user.set_position(18 * self.wall_x + self.delta, self.car_user.y)
				self.audio.play()
				self.lastClick = window.last_time
			elif keyboard.key_pressed("LEFT") and \
				self.car_user.x == 18 * self.wall_x + self.delta:
				self.car_user.set_position(14 * self.wall_x + self.delta, self.car_user.y)
				self.audio.play()
				self.lastClick = window.last_time

		self.car_user.draw()

	def run(self, window, MODE, score):
		for i in range(len(self.matrizMundo)):
			for j in range(len(self.matrizMundo[0])):
			    if int(self.matrizMundo[i][j]) == 1:
			        posX = j * self.wall_x
			        posY = window.height - i * self.wall_y


			        self.wall.set_position(posX,posY)
			        self.wall.draw()

			if i==0:
				lin = self.matrizMundo[0]
				self.matrizMundo.remove(lin)
				self.matrizMundo.append(lin)

		for car in self.car_enemies:
			car.set_position(car.x, car.y + self.wall_y)
			car.draw()
			if(car.y - car.height > window.height):
				if random.randint(0,1)==0:
					car.set_position(14 * self.wall_x + self.delta, - car.height+20)
				else:
					car.set_position(18 * self.wall_x + self.delta, - car.height + 20)

			if car.collided(self.car_user) and self.car_user.x == car.x:
			    MODE = 9
			    self.audio_end.play()
			    score = int(time.time() - self.intialTime)

		self.currentTime = window.last_time

		return MODE,score	

	def increaseDificulty(self,GAME_SPEED):	
		if time.time() - self.tempoAnterior >= 15:
			self.tempoAnterior = time.time()
			GAME_SPEED+=10
		return GAME_SPEED	

	def game(self,GAME_SPEED,score,MODE,window,keyboard,delay):
		self.move(window,keyboard,delay)
		MODE, score = self.run(window, MODE, score)
		GAME_SPEED = self.increaseDificulty(GAME_SPEED)
		return GAME_SPEED,score,MODE 	

