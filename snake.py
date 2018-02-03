#Snake

import pygame, sys, random, time

def game_over():
	game_font = pygame.font.SysFont('Liberation sans', 68)
	game_over = game_font.render('Game Over.', True, red)
	game_over_rect = game_over.get_rect()
	game_over_rect.midtop = (300, 50)
	game_display.blit(game_over, game_over_rect)
	pygame.display.flip()
	time.sleep(5)
	pygame.quit()
	sys.exit()

errors = pygame.init()

if(errors[1]):
	print(errors[0]+" errors.")
	sys.exit(-1)
else:
	print("No errors.")

#Display:
game_display = pygame.display.set_mode((600,400))
pygame.display.set_caption('Snake')

#Color variables:
red = pygame.Color(255, 0, 0) #Game Over font color
green = pygame.Color(0, 255, 0) #Snake body color
blue = pygame.Color(0, 0, 255) 
black = pygame.Color(0, 0, 0) #Background Color
brown = pygame.Color(165, 42, 42)

#FPS:
fps_controller = pygame.time.Clock()

#Game variables:
snk_pos = [100, 50]
snk = [[100, 50],[90, 50],[80, 50]]

food_pos = [random.randrange(1,60)*10, random.randrange(1,40)*10]

direction = 'RIGHT'
changeto = direction

#Game loop:
while(1):
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
	else:
		snk.pop()

	for pos in snk:
		pygame.draw.rect(game_display, green, 
		pygame.Rect(pos[0], pos[1], 10, 10));

	pygame.draw.rect(game_display, brown, 
	pygame.Rect(food_pos[0], food_pos[1], 10, 10));

	pygame.display.flip()
	fps_controller.tick(14)