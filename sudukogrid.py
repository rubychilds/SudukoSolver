import pygame
from pygame.locals import *
from pygame import Color, Rect, Surface

class Board:

	def __init__(self, screen):

		screen_size = screen.get_size()

		# deals with background
		self.background = pygame.Surface(screen.get_size())
		self.background = self.background.convert()
		self.background.fill ((250,250,250))

		# Font 
		font = pygame.font.SysFont('Subway Black', 30, bold = False, italic = False)
	  	text = font.render("Suduko Solver", 1, (10, 10, 10)) # sets font type, size then rgb tuple
	  	textpos = text.get_rect()
	  	textpos.centerx = self.background.get_rect().centerx
	  	self.background.blit(text, textpos)

		print screen_size
		pygame.draw.rect(self.background, Color("Black"), Rect(30, 40,400,400))

		# Starting position of the rectangle
		rect_x = 36
		rect_y = 46
	 
		# Speed and direction of rectangle
		rect_change_x = 0
		rect_change_y = 0

		# Width and height of rectangles
		height = 40
		width = 40

		for x in range(1,10):
			for y in range(1,10):
				pygame.draw.rect(self.background, Color("white"), Rect(rect_x + rect_change_x, rect_y + rect_change_y, width, height))			
				rect_change_y += 42 

				if y % 3 == 0 :
					rect_change_y +=2

			rect_change_x += 42
			rect_change_y = 0
			if x % 3 == 0 :
					rect_change_x +=2
			#print rect_change_x
	

		# function to set numbers on grid
	#def initNumbers(numbers):

		# add buttons to window

		# mouse position

	def getBackground(self):
		return self.background

	# takes its self as a parameter
	def showBoard(self,ttt):
			ttt.blit(self.background,(0,0))
			pygame.display.flip()

# MAIN PROGRAMME 
def main():
	# Initialise screen
 	pygame.init() # calls font initialisation automatically otherwise we can use pygame.font.init()
 	screen = pygame.display.set_mode((580, 500))
 	pygame.display.set_caption('Basic Pygame program')

	#  Displays board
	board_inst = Board(screen)
	# for running of the game
	running = 1
	# 
	mouse = false



	# Event loop - infinite until event i.e. closing of window
  	while (running == 1):
  		for event in pygame.event.get():
  			if event.type is QUIT:
  	 			running = 0
  	 		elif event.type == MOUSEMOTION:
  	 			mousex, mousey = event.pos
  	 		elif event.type == MOUSEBUTTONUP:
  	 			mousex, mousey = event.pos
  	 			mouseclicked = true


  	 	board_inst.showBoard(screen)

if __name__ == "__main__":
	main()
