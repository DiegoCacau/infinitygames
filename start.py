from PPlay.sprite import *


class start():
	
	def __init__(self,lastClick):
		self.lastClick = lastClick
		#first page menu
		self.select = Sprite("gun.png",1)
		self.select.set_total_duration(1000)
		self.select.set_position(100,190)


	def game(self, window,MODE,tempo, keyboard,delay):
		window.draw_text("Selecione o Jogo", 130, 60, 40, (255, 255, 0), "Arial", True, True)
		window.draw_text("Snake", 170, 180, 40, (0, 255, 0), "Arial", True, True)
		window.draw_text("Runnning", 170, 260, 40, (255, 0, 0), "Arial", True, True)
		window.draw_text("Tank", 170, 340, 40, (200, 120, 255), "Arial", True, True)
		window.draw_text("Aperte ENTER", 160, 430, 25, (255, 255, 0), "Arial", True, True)

		currentTime = window.last_time
		if currentTime - self.lastClick > delay+70:
			if (keyboard.key_pressed("ENTER")):
				if (self.select.y <= 210):
					MODE = 1
				elif (self.select.y <= 300):
					MODE = 2
				else:
					MODE = 3
				tempo = time.time()
				self.lastClick = currentTime


			elif (keyboard.key_pressed("UP")):
				if self.select.y > 200:
					self.select.y =  self.select.y - 80
				self.lastClick = currentTime
			elif (keyboard.key_pressed("DOWN")):
				if self.select.y < 300:
					self.select.y = self.select.y + 80
				self.lastClick = currentTime


		self.select.update()
		self.select.draw()	

		return MODE, tempo