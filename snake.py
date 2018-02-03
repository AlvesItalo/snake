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
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

#FPS:
fps_controller = pygame.time.Clock()

#Game variables:
snk_pos = [100, 50]
snk = [[100, 50],[90, 50],[80, 50]]

food_pos = [random.randrange(1,60)*10, random.randrange(1,40)*10]
food_spawn = True

direction = ''
changeto = direction


game_over()