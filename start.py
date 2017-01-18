class start():
	def game(self):
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