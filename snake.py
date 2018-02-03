#Snake

import pygame, sys, random, time

errors = pygame.init()

if(errors[1]):
	print(errors[0]+" errors.")
	sys.exit(-1)
else:
	print("No errors.")

