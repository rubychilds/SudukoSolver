import pygame
from pygame.locals import *
from pygame import Color, Rect, Surface

# COLOURS
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)


HIGHLIGHTCOLOUR = BLUE
BOXCOLOUR = WHITE
INCORRECTCOLOUR = RED
CORRECTCOLOUR = GREEN

class Board:

	rectGroup = []
	change = 42

	def __init__(self, screen):

		rectGroup = []
		# self.SCREEN = screen
		SCREEN = screen
		# screen_size = SCREEN.get_size()

		# deals with background
		self.background = pygame.Surface(SCREEN.get_size())
		self.background = self.background.convert()
		self.background.fill ((250,250,250))

		# Font 
		font = pygame.font.SysFont('Subway Black', 30, bold = False, italic = False)
	  	text = font.render("Suduko Solver", 1, (10, 10, 10)) # sets font type, size then rgb tuple
	  	textpos = text.get_rect()
	  	textpos.centerx = self.background.get_rect().centerx
	  	self.background.blit(text, textpos)

		#print screen_size
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

		change = 42

		for x in range(1,10):
			for y in range(1,10):
				
				tempRec = Rect(rect_x + rect_change_x, rect_y + rect_change_y, change, change)
				pygame.draw.rect(self.background, Color("white"), tempRec)			
				rectGroup.append(tempRec)
				rect_change_y += change

				if y % 3 == 0 :
					rect_change_y +=2

			rect_change_x += change
			rect_change_y = 0
			if x % 3 == 0 :
					rect_change_x +=2
			#print rect_change_x

	# gets rectangle for point clicked
	def rectangleForPoint(self, point):
		for rectangle in rectGroup:
			if rectangle.pointinrect(point, rectangle):
				return rectangle
		return None

	# highlighting of box
	def drawHighlightBox(self, rectangle):
		pygame.draw.rect(SCREEN, HIGHLIGHTCOLOUR, rectangle)
    #	pygame.display.update()

	def drawCorrectBox(self, rectangle):
		pygame.draw.rect(SCREEN, CORRECTCOLOUR, rectangle)
    #	pygame.display.update()

	def drawInCorrectBox(self, rectangle):
		pygame.draw.rect(SCREEN, INCORRECTCOLOUR, rectangle)
    #	pygame.display.update()

	# resets rectangle if it is wrong ....
	def resetRectangle(self, rectangle):
		pygame.draw.rect(SCREEN, HIGHLIGHTCOLOUR, rectangle)
	#	pygame.display.update()

	# gets board made
	def getBackground(self):
		return self.background

	# takes its self as a parameter
	def showBoard(self, SCREEN):
		SCREEN.blit(self.background,(0,0))
		pygame.display.flip()

	def Answer(self, answer, rectangle):
		font = pygame.font.SysFont('Subway Black', 30, bold = False, italic = False)
	  	text = font.render( str(answer), (10, 10, 10)) # sets font type, size then rgb tuple
	  	textpos = text.get_rect()
	  	textpos.centerx = rectangle.centerx
	  	textpos.centery = rectangle.centery
	  	self.background.blit(text, textpos)

	# draws board - is in its own function to handle updates
	def drawBoard(self, board, solvedAnswers):

		for answer in solvedAnswers:
			rectGroup.get_rect(answer)
			drawCorrectBox(rectangle)
			drawAnswer(answer, rectangle)

	def updateRect(self,identification, point):
		
		if(identification is "selected"):
			# gets rectangle that has been selected
			rect = rectangleForPoint(point)
			# now highlights that rectangle
			drawHighlightBox(rect)
			# return the fact it has been updated		
			return true
			if(rect != None):
				drawHighlightBox(rect)
			
		return false


# MAIN PROGRAMME 
def main():
	# Initialise screen
 	pygame.init() # calls font initialisation automatically otherwise we can use pygame.font.init()
 	SCREEN = pygame.display.set_mode((580, 500))
 	pygame.display.set_caption('Suduko program')

	#  Displays board
	board_inst = Board(SCREEN)
	# for running of the game
	running = 1
	#  Initiate mouse movements
	mouse = False
	clicked = (0,0)

	# Event loop - infinite until event i.e. closing of window
  	while (running == 1):
  		mouseclicked = False
  		selected = False
  	#	for event in pygame.event.get():
  	#		if event.type is QUIT: #or event.key is K_ESCAPE:
  	 #			running = 0
  	 #		elif (event.type == MOUSEBUTTONUP and event.type == MOUSEMOTION):
  	 #			clicked = event.pos
  	 #			board_inst.updateRect("selected", clicked)
  	 #		elif event.type == MOUSEBUTTONUP:
  	 #			clicked = event.pos
  	 #			board_inst.updateRect("selected", clicked)
  	 #			mouseclicked = True
  	 #			pygame.event.clear()

  	 	board_inst.showBoard(SCREEN)

class Point:

	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

if __name__ == "__main__":
	main()
