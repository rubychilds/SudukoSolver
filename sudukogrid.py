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

WINDOWHEIGHT = 580
WINDOWWIDTH  = 500


HIGHLIGHTCOLOUR = BLUE
DEFAULTCOLOUR = WHITE
INCORRECTCOLOUR = RED
CORRECTCOLOUR = GREEN

class Board:

	change = 42

	def __init__(self, screen):

		self.rectGroup = []
		self.screen = screen
		
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
				rectangle = Rect(rect_x + rect_change_x, rect_y + rect_change_y, change, change )
				tempRec = recID(rectangle, DEFAULTCOLOUR)
				pygame.draw.rect(self.background, Color("white"), rectangle)			
				self.rectGroup.append(tempRec)
				rect_change_y += change

				if y % 3 == 0 :
					rect_change_y +=2

			rect_change_x += change
			rect_change_y = 0
			if x % 3 == 0 :
					rect_change_x +=2
			#print rect_change_x

		print self.rectGroup

	# gets rectangle for point clicked
	def rectangleForPoint(self, point):
		for rectangleID in self.rectGroup:
			rect = rectangleID.getRectangle()
			if rect.collidepoint(point[0],point[1]):
				return rectangleID
		return None

	def changeCol(self, rectangle):
		currentCol = rectangle.getColour()
		print currentCol
		if currentCol != HIGHLIGHTCOLOUR:
			self.drawHighlightBox(rectangle.getRectangle(), HIGHLIGHTCOLOUR)
			rectangle.setColour(HIGHLIGHTCOLOUR)
  	 	elif currentCol == HIGHLIGHTCOLOUR:
			self.drawHighlightBox(rectangle.getRectangle(), WHITE)
			rectangle.setColour(WHITE)

	# highlighting of box
	def drawHighlightBox(self, rectangle, color):
		pygame.draw.rect(self.background, color, rectangle)
    #	pygame.display.update()

	# gets board made
	def getBackground(self):
		return self.background

	# takes its self as a parameter
	def showBoard(self, SCREEN):
		self.screen.blit(self.background,(0,0))
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


# CREATES BUTTON WHEN CALLED
class Button:

	def	__init__(self):
	    pygame.sprite.Sprite.__init__(self)
	
	def loadImage():
		pygame.loadImage("button.jpg")


	def setCords(self , x, y):
		self.rect.topleft = x , y


	def pressed(self, mouse):
		if mouse[0] < self.rect.topleft[0]:
			return False
		if mouse[1] < self.rect.topleft[1]:
			return False
		if mouse[0] > self.rect.bottomright[0]:
			return False
		if mouse[1] > self.rect.bottomright[1]:
			return False
		return True


class startScreen:

	def __init__(self, screen):
		drawText('Suduko Solver', font, screen, 50, 50)
		pygame.time.wait(10000)
		screen.clear()

# MAIN PROGRAMME 
def main():
	# Initialise screen
 	pygame.init() # calls font initialisation automatically otherwise we can use pygame.font.init()

 	# button = Button()
	# button.setCords(WINDOWHEIGHT/2, WINDOWWIDTH/2)

 	SCREEN = pygame.display.set_mode((WINDOWHEIGHT, WINDOWWIDTH))
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
  		event = pygame.event.poll()
  		if event.type == pygame.QUIT: #or event.key == pygame.K_ESCAPE:
  	 		running = 0
  	 	elif event.type == pygame.MOUSEBUTTONDOWN:
  	 		# check if in rectangle
			point = pygame.mouse.get_pos()
  	 		rectangle = board_inst.rectangleForPoint(point)
  	 		event_current = pygame.event.poll()
  	 		if event_current.type == pygame.MOUSEMOTION:
  	 			position = event.pos
  	 			points = []
  	 			if rectangle.getRectangle().collidepoint(position):
               		points = points + [position]
               		points = points[-256:]
               		drawLineBetween(screen, index, start, end, width, BLACK):
				while i < len(points) - 1:
            	drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            	i += 1
        
        pygame.display.flip()



  	 	board_inst.showBoard(SCREEN)

class recID:

	def __init__(self, rectangle, colour):
		self.rectangle = rectangle
		self.colour = colour

	def getRectangle(self):
		return self.rectangle

	def getColour(self):
		return self.colour


	def setColour(self, colour):
		self.colour = colour

def drawLineBetween(screen, index, start, end, width, BLACK):

    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in xrange(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = aprogress * start[0] + progress * end[0]
        y = aprogress * start[1] + progress * end[1]
        # cannot pass floats so must convert to integer
        pygame.draw.circle(screen, BLACK, (int(x), int(y)), width)

if __name__ == "__main__":
	main()
