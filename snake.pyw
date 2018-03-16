#Snake
import pygame, sys, random, time

#Display:
game_display = pygame.display.set_mode((600,400))
pygame.display.set_caption('Snake')

#Color variables:
red = pygame.Color(255, 0, 0)     # Game Over font color
green = pygame.Color(0, 255, 0)   # Snake body color
blue = pygame.Color(0, 0, 255)    # Score color
black = pygame.Color(0, 0, 0)     # Background color
brown = pygame.Color(165, 42, 42) # Food color

def game_over():
	while(1):
		game_font = pygame.font.SysFont('Liberation sans', 68)
		playAg_font = pygame.font.SysFont('Liberation sans', 12)

		game_over = game_font.render('YOU DIED', True, red)
		playag_font = game_font.render('Play Again? (S/N)', True, blue)
		game_over_rect = game_over.get_rect()
		playag_rect = playag_font.get_rect()
		playag_rect.midtop = (300, 218)
		game_over_rect.midtop = (300, 150)
		game_display.blit(game_over, game_over_rect)
		game_display.blit(playag_font, playag_rect)

		for event in pygame.event.get():
			if((event.key == ord('s'))):
				game()
			elif(event.key == ord('n')):
				pygame.quit()
				sys.exit()

		pygame.display.flip()

def display_score(score):
	score_font = pygame.font.SysFont('Liberation sans', 28)
	score_display = score_font.render('Score: '+ str(score), True, blue)
	score_display_rect = score_display.get_rect()
	score_display_rect.midtop = (300, 10)
	game_display.blit(score_display, score_display_rect)

#Game loop:
def game():
	errors = pygame.init()

	if(errors[1]):
		print(errors[0]+" errors.")
		sys.exit(-1)
	else:
		print("No errors.")

	#FPS:
	fps_controller = pygame.time.Clock()
	fps = 10

	#Game variables:
	snk_pos = [100, 50]
	snk = [[100, 50],[90, 50],[80, 50]]

	food_pos = [random.randrange(1,60)*10, random.randrange(1,40)*10]

	direction = 'RIGHT'
	changeto = direction

	score = 0

	while(1):
		if((snk_pos[0] < 0 or snk_pos[0] > 600) or (snk_pos[1] < 0 or snk_pos[1] > 400) or snk_pos in snk[1:-1]):
			game_over()

		game_display.fill(black)
		display_score(score)

		for event in pygame.event.get():
			#Main Event Handler:
			if (event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			elif(event.type == pygame.KEYDOWN):
				#Key alias:
				if((event.key == pygame.K_RIGHT or event.key == ord('d')) and direction != 'LEFT' ):
					changeto = 'RIGHT'
				if((event.key == pygame.K_LEFT or event.key == ord('a')) and direction != 'RIGHT'):
					changeto = 'LEFT'
				if((event.key == pygame.K_UP or event.key == ord('w')) and direction != 'DOWN'):
					changeto = 'UP'
				if((event.key == pygame.K_DOWN or event.key == ord('s')) and direction != 'UP'):
					changeto = 'DOWN'
				if(event.key == pygame.K_ESCAPE):
					pygame.event.post(pygame.event.Event(pygame.QUIT))


		#Movement:
		direction = changeto

		if(direction == 'RIGHT'):
			snk_pos[0] += 10
		elif(direction == 'LEFT'):
			snk_pos[0] -= 10
		elif(direction == 'UP'):
			snk_pos[1] -= 10
		elif(direction == 'DOWN'):
			snk_pos[1] += 10

		#Snake body:
		snk.insert(0, list(snk_pos))
		if(snk_pos[0] == food_pos[0] and snk_pos[1] == food_pos[1]):
			food_pos = [random.randrange(1,60)*10, random.randrange(1,40)*10]
			score +=  10
			fps += 0.1
		else:
			snk.pop()

		for pos in snk:
			pygame.draw.rect(game_display, green,
			pygame.Rect(pos[0], pos[1], 10, 10))

		pygame.draw.rect(game_display, brown,
		pygame.Rect(food_pos[0], food_pos[1], 10, 10))


		pygame.display.flip()
		fps_controller.tick(int(fps))

game()
