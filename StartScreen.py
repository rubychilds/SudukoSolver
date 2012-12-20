import pygame
import time

WINDOWHEIGHT = 500
WINDOWWIDTH  = 650

class StartScreen:

	def __init__(self):

		pygame.init()

		self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill ((250,250,250))
		
		# Font 
		font = pygame.font.SysFont('Subway Black', 70, bold = False, italic = False)
	  	text = font.render("Suduko Solver", 100, (10, 10, 10)) # sets font type, size then rgb tuple
	  	textpos = text.get_rect()
	  	textpos.centerx = self.background.get_rect().centerx
	  	textpos.centery = self.background.get_rect().centery
	  	self.background.blit(text, textpos)

		self.screen.blit(self.background,(0,0))
		pygame.display.flip()
		pygame.time.wait(1000)