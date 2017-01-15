from PPlay.sprite import *
from PPlay.sound import *
import random




class snake():

	#audio
	


	def __init__(self):
		snake_x = [290, 290, 290, 290, 290]
		snake_y = [290, 280, 270, 260, 250]
		self.pixel = {'snake': [], 'direcao': 1, 'ultimoMov': 0, 'pontos': 0}
		i = 0
		for snk in snake_x:
			snake_pixel = Sprite("Snake/snake.png", 1)
			snake_pixel.set_total_duration(0)
			snake_pixel.set_position(snake_x[i], snake_y[i])
			self.pixel['snake'].append(snake_pixel)
			i = i + 1
		self.red_pix = Sprite('Snake/pixel.png', 1)
		self.red_pix.set_total_duration(0)
		self.red_pix.set_position(random.randint(0, 512), random.randint(0, 512))

		self.audio = Sound("Sounds/shot.ogg")
		self.audio.set_volume(100)
		self.audio_end = Sound("Sounds/end.ogg")
		self.audio_end.set_volume(100)	

	def move(self, delay,window,keyboard):
		self.red_pix.draw()

		#configura a direção da snake e faz as movimentações
		x=0
		y=0
		currentTime = window.last_time
		if(currentTime - self.pixel['ultimoMov'] > delay):
			self.pixel['ultimoMov'] = currentTime
			if keyboard.key_pressed("RIGHT") and self.pixel['direcao'] != 2:
				self.pixel['direcao'] = 1
			elif  keyboard.key_pressed("LEFT") and self.pixel['direcao'] != 1:
				self.pixel['direcao'] = 2
			elif  keyboard.key_pressed("UP") and self.pixel['direcao'] != 4:
				self.pixel['direcao'] = 3
			elif keyboard.key_pressed("DOWN") and self.pixel['direcao'] != 3:
				self.pixel['direcao'] = 4
		        

		if self.pixel['direcao'] == 1:
			x = 15
		if self.pixel['direcao'] == 2:
			x = -15
		if self.pixel['direcao'] == 3:
			y = -15
		if self.pixel['direcao'] == 4:
			y = 15

		posi_x = self.pixel["snake"][0].x
		posi_y = self.pixel["snake"][0].y

		self.pixel["snake"][0].set_position(posi_x+x, posi_y+y)
		self.pixel["snake"][0].draw()

		self.draw(posi_x,posi_y)


	def getApple(self, score):
		if(self.pixel['snake'][0].collided(self.red_pix)):
			self.red_pix.set_position(
				random.randint(self.red_pix.height,527-self.red_pix.height),
				random.randint(self.red_pix.height,527-self.red_pix.height))
			snake_pixel = Sprite("Snake/snake.png", 1)
			snake_pixel.set_total_duration(0)
			snake_pixel.set_position(999, 999)
			self.pixel['pontos'] = self.pixel['pontos']+50
			self.pixel['snake'].append(snake_pixel)
			score = score + 50
			self.audio.play()
		return score

	def lost(self, MODE):
		for i in range(len(self.pixel['snake'])):
			if (len(self.pixel['snake']) > i+4):
				j = i + 4
				while j < (len(self.pixel['snake'])):
					if self.pixel['snake'][i].collided(self.pixel['snake'][j]):
						MODE = 9
						self.audio_end.play()
						return MODE
					j = j +1
		return MODE			

	def draw(self,posi_x,posi_y):
		i=0
		for pix in self.pixel["snake"]:
			if i!=0:
				pos_x_aux=pix.x
				pos_y_aux = pix.y
				pix.set_position(posi_x, posi_y)
				posi_x = pos_x_aux
				posi_y = pos_y_aux
				pix.draw()
			i=1

	def border(self):
		if self.pixel['snake'][0].x <= self.pixel['snake'][0].height \
			and self.pixel['direcao'] == 2:

			self.pixel['snake'][0].set_position(
				527- self.pixel['snake'][0].height, self.pixel['snake'][0].y)

		elif self.pixel['snake'][0].x >= 527-self.pixel['snake'][0].height \
			and self.pixel['direcao'] == 1:

			self.pixel['snake'][0].set_position(
				self.pixel['snake'][0].height, self.pixel['snake'][0].y)

		elif self.pixel['snake'][0].y <= self.pixel['snake'][0].height \
			and self.pixel['direcao'] == 3:

			self.pixel['snake'][0].set_position(
				self.pixel['snake'][0].x,527- self.pixel['snake'][0].height)

		elif self.pixel['snake'][0].y >= 527-self.pixel['snake'][0].height \
			and self.pixel['direcao'] == 4:

			self.pixel['snake'][0].set_position(
				self.pixel['snake'][0].x, self.pixel['snake'][0].height)		

	def game(self,delay,score,MODE,window,keyboard):
		self.border()
		self.move(delay,window,keyboard)
		score = self.getApple(score)
		MODE = self.lost(MODE)
		return score,MODE					