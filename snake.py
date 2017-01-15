from PPlay.sprite import *
import random



def snake():


	def __init__(self):
		snake_x = [290, 290, 290, 290, 290]
		snake_y = [290, 280, 270, 260, 250]
		self.pixel = {'snake': [], 'direcao': 1, 'ultimoMov': 0, 'pontos': 0}
		i = 0
	    for snk in self.snake_x:
			snake_pixel = Sprite("Snake/snake.png", 1)
			snake_pixel.set_total_duration(0)
			snake_pixel.set_position(snake_x[i], snake_y[i])
			self.pixel['snake'].append(snake_pixel)
			i = i + 1
		self.red_pix = Sprite('Snake/pixel.png', 1)
		self.red_pix.set_total_duration(0)
		self.red_pix.set_position(random.randint(0, 512), random.randint(0, 512))	

	def move(self):
		self.red_pix.draw()

	def getApple(self, score):
		if(self.pixel['snake'][0].collided(self.red_pix)):
			self.red_pix.set_position(random.randint(0,527),random.randint(0,527))
			snake_pixel = Sprite("Snake/snake.png", 1)
			snake_pixel.set_total_duration(0)
			snake_pixel.set_position(999, 999)
			self.pixel['pontos'] = self.pixel['pontos']+50
			self.pixel['snake'].append(snake_pixel)
			#print(pixel['pontos'])
			score = score + 50
			audio_shot.play()
			return score

	def lost(self, MODE):
		for i in range(len(pixel['snake'])):
			if (len(pixel['snake']) > i+4):
				j = i + 4
				while j < (len(pixel['snake'])):
					if pixel['snake'][i].collided(pixel['snake'][j]):
						MODE = 9
						audio_end.play()
						return MODE
					j = j +1
		return MODE			

	def draw(self):
		pass			