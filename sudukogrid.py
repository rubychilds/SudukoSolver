import pygame, sys, time
import pyHook
from event_manager import *
from pygame.locals import *
from pygame import Color, Rect, Surface

# COLOURS
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)

COLORS = [WHITE, BLUE, RED, GREEN]

STATE_START = 0
STATE_SELECT = 1
STATE_WRONG = 2
STATE_CORRECT = 3

WINDOWHEIGHT = 580
WINDOWWIDTH  = 500

class Board(pygame.sprite.Sprite):

	change = 42

	def __init__(self, screen):

		self.rectGroup = []
		self.screen = screen

		width, height = screen.get_size()
		scale = 9/10

		# deals with background
		self.background = pygame.Surface((scale*width,scale*height))
		self.background = self.background.convert()
		self.background.fill ((250,0,0))

		#print screen_size
		self.background.draw.rect(self.background, Color("Black"), Rect(30, 54,400,400))

	def changeCol(self, rectangle):
		currentCol = rectangle.colour
	#	print currentCol
		if currentCol != STATE_SELECT:
			self.drawHighlightBox(rectangle.getRectangle(), STATE_SELECT)
			rectangle.setColour(HIGHLIGHTCOLOUR)
  	 	elif currentCol == STATE_SELECT:
			self.drawHighlightBox(rectangle.getRectangle(), STATE_START)
			rectangle.setColour(WHITE)

	# highlighting of box
	def drawHighlightBox(self, rectangle, color):
		self.background.draw.rect(self.background, color, rectangle)

	def updateRect(self,identification, point):

		if(identification is "selected"):
			# gets rectangle that has been selected
			rect = rectangleForPoint(point)
			# now highlights that rectangle
			rect
			# return the fact it has been updated		
			return true
			if(rect != None):
				drawHighlightBox(rect)

		return false

# MAIN PROGRAMME 
class PygameView(pygame.sprite.Sprite):

	def __init__(self, event_manager):
		pygame.sprite.Sprite.__init__(self)
		# Initialise screen
	 	pygame.init() # calls font initialisation automatically otherwise we can use pygame.font.init()
		
	 	self.screen = pygame.display.set_mode((WINDOWHEIGHT, WINDOWWIDTH))
	 	pygame.display.set_caption('Suduko')
	 	startScreen()
	 	
	 	# make background
	 	self.background = pygame.Surface(self.screen.get_size())
	 	self.background.fill(WHITE)
	 	self.screen.blit(self.background, (0,0))
	    
		# Font 
		font = pygame.font.SysFont('Subway Black', 30, bold = False, italic = False)
		text = font.render("Suduko Solver", 1, (10, 10, 10)) # sets font type, size then rgb tuple
		textpos = text.get_rect()
		textpos.centerx = self.background.get_rect().centerx
		self.background.blit(text, textpos)

	    # draws rectangles
		self.DrawRec()
	    # creates sprites
		self.buttons = pygame.sprite.RenderUpdates()
		self.selected = pygame.sprite.RenderUpdates()
		self.cursor = pygame.sprite.GroupSingle()

	    # updates the display
		pygame.display.update()

		textButtons = "Start Game", "Hint", "Help", "End Game"
		dirty = []
		buttonSize = (10, 20)
		index = 0

		for text in textButtons:
			button = Button(((9/10)*WINDOWHEIGHT, (9/10)*WINDOWHEIGHT + index), text)
			index += 10
			self.buttons.add(button)

		# buttons.draw(SCREEN)

	def DrawRec(self):

		self.rectangleGroup = []
		# Starting position of the rectangle
		rect_x = 36
		rect_y = 60

			# Speed and direction of rectangle
		rect_change_x = 0
		rect_change_y = 0

			# Width and height of rectangles
		height = 40
		width = 40
		change = 42

		for x in range(1,10):
			for y in range(1,10):
				rectangle = Rect(rect_x + rect_change_x, rect_y + rect_change_y, height, width)
				tempRec = recID(rectangle, rect_x + rect_change_x, rect_y + rect_change_y)
				pygame.draw.rect(self.screen, WHITE, rectangle)			
				self.rectangleGroup.append(tempRec)
				rect_change_y += change

				if y % 3 == 0 :
					rect_change_y +=2

			rect_change_x += change
			rect_change_y = 0
			if x % 3 == 0 :
				rect_change_x +=2

	# gets rectangle for point clicked
	def rectangleForPoint(self, point):

		for rectangleID in self.rectGroup:
			rectangleCheck = rectangleID.rectangle
			if rectangleCheck.collidepoint(point[0],point[1]):
				return rectangleID
		return None



