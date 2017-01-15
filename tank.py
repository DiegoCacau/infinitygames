from PPlay.sprite import *
from PPlay.sound import *
from sho import shot
from tankEnemy import enemy_tank
import random
import time


class tank():

	tank_images = ['Tank/tank.png', 'Tank/tank_1.png', 'Tank/tank_2.png',
                           'Tank/tank_3.png']

	def __init__(self, lastClick):
		self.user = Sprite(self.tank_images[0], 1)
		self.user.set_total_duration(0)
		self.user.set_position(100, 300)
		self.shots = []
		self.enemies = []
		self.shots_enemy = []
		self.max_enemies = 4
		self.velocidade = 10
		self.direcao = 0
		self.audio = Sound("Sounds/shot.ogg")
		self.audio.set_volume(100)
		self.audio_end = Sound("Sounds/end.ogg")
		self.audio_end.set_volume(100)
		self.tempo = time.time()
		self.lastClick = lastClick
		self.delay = 50

	def move(self, window,keyboard):
		posi_x = self.user.x
		posi_y = self.user.y
		currentTime = window.last_time


		if (currentTime - self.lastClick > self.delay + 20):
			if keyboard.key_pressed("RIGHT"):
				self.direcao = 1
				self.user = Sprite(self.tank_images[1], 1)
				self.user.set_position(posi_x + self.velocidade, posi_y)

			elif keyboard.key_pressed("LEFT"):
				self.direcao = 3
				self.user = Sprite(self.tank_images[3], 1)
				self.user.set_position(posi_x - self.velocidade, posi_y)

			elif keyboard.key_pressed("UP"):
				self.direcao = 0
				self.user = Sprite(self.tank_images[0], 1)
				self.user.set_position(posi_x, posi_y - self.velocidade)

			elif keyboard.key_pressed("DOWN"):
				self.direcao = 2
				self.user = Sprite(self.tank_images[2], 1)
				self.user.set_position(posi_x, posi_y + self.velocidade)

			elif keyboard.key_pressed("SPACE"):
				x = self.user.x + self.user.width / 2
				y = self.user.y + self.user.height / 2
				self.shots.append(shot("Tank/shot.png", self.direcao, x, y))
				self.audio.play()

			if(self.user.x<0):
				self.user.x = 0
			elif(self.user.x > 527 - self.user.height):
				self.user.x = 527 - self.user.height
			if (self.user.y < 0):
				self.user.y = 0
			elif (self.user.y > 527 - self.user.height):
				self.user.y = 527 - self.user.height

			self.lastClick = currentTime

		self.user.draw()

	def shoting(self,score,MODE):
		for sh in self.shots:
			sh.atualizar()
			x,y = sh.posicao()
			if(x<0 or x>527 or y<0 or y>527):
				self.shots.remove(sh)

			for en in self.enemies:
				if sh.spr().collided(en.spr()):
					self.shots.remove(sh)
					self.enemies.remove(en)
					score = score + 20

		for sh in self.shots_enemy:
			sh.atualizar()
			x,y = sh.posicao()
			if(x<0 or x>527 or y<0 or y>527):
				self.shots_enemy.remove(sh)

			if sh.spr().collided(self.user):
				MODE = 9
				self.audio_end.play()
			else:
				for sh2 in self.shots:
					if sh.spr().collided(sh2.spr()):
						self.shots.remove(sh2)
						self.shots_enemy.remove(sh)
						score = score + 5
		return score,MODE

	def colisions(self, MODE):
		if MODE != 9:
			for en in self.enemies:
				if self.user.collided(en.spr()):
					MODE = 9
					self.audio_end.play()
				else:
					for en2 in self.enemies:
						if en2 != en:
							if en.spr().collided(en2.spr()):
								if(en.direcao < 2):
							 		en.direcao = en.direcao + 2
								else:
							 		en.direcao = en.direcao - 2

							en.move()
				self.fireEnemy(en)
							
		return MODE

	def fireEnemy(self, enemy):
		if random.randint(0,50) > 48:
			x = enemy.spr().x + enemy.spr().width / 2
			y = enemy.spr().y + enemy.spr().height / 2
			self.shots_enemy.append(shot("Tank/shot2.png", enemy.direcao, x, y))            						

	
	def respawEnemies(self):
		if len(self.enemies) < self.max_enemies:
			self.enemies.append(enemy_tank())

	
	def moveEnemies(self):
		for enemy in self.enemies:
			enemy.move()

	def increaseDificulty(self):
		if time.time() - self.tempo >=30:
			self.max_enemies = self.max_enemies + 1
			self.tempo = time.time()		

	
	def game(self,score,MODE,window,keyboard):
		self.move(window,keyboard)
		score,MODE = self.shoting(score,MODE)
		MODE = self.colisions(MODE)
		self.respawEnemies()
		self.moveEnemies()

		return score,MODE