import pygame, sys, time
import pyHook
from eventManager import *
from pygame.locals import *
from pygame import Color, Rect, Surface


# COLOURS
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
BLACK    = (0 ,0 , 0)

textButtons = ["Start Game", "Hint", "Help", "End Game"]

COLOURS = [WHITE, BLUE, RED, GREEN]

WINDOWHEIGHT = 500
WINDOWWIDTH  = 580
CELL_SIZE = 40

#------------------------------------------------------------------------------
class Button(pygame.sprite.Sprite):

    def __init__(self, xy, text):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.xy = xy
        self.font = pygame.font.SysFont('Subway Black', 20, bold = False, italic = False)
        self.colour = (255,255,255)
        self.generateImage()

    def generateImage(self):
        self.image = self.font.render(self.text, True, self.colour, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.xy

#------------------------------------------------------------------------------
class pyGame:

    def __init__(self, evManager):

        self.evManager = evManager
        self.evManager.RegisterListener(self)
        print "REGISTERED VIEW"

        pygame.init()

        self.screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
        pygame.display.set_caption('Suduko Solver')

        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255, 255, 255))
        self.screen.blit(self.background, (0,0))

        # Font 
        self.font = pygame.font.SysFont('Subway Black', 30, bold = False, italic = False)
        self.text = self.font.render("Suduko Solver", 1, (10, 10, 10)) # sets font type, size then rgb tuple
        self.textpos = self.text.get_rect()   
        self.textpos.centerx = self.background.get_rect().centerx
        self.background.blit(self.text, self.textpos)
        pygame.draw.rect(self.background, WHITE,(30, 54, 400, 400),0)
        pygame.display.update() 

        self.buttons = pygame.sprite.Group()

        self.ShowBoard()
        self.ShowButtons()
        self.ShowRectangles()

        # self.buttons = pygame.sprite.RenderUpdates()
        # holds a single sprite
        # self.backRectangle = pygame.sprite.GroupSingle()
        # self.rectangleSprites = pygame.sprite.RenderUpdates()

    def ShowBoard(self):
        # creates rectangle
        pygame.draw.rect(self.background, BLACK,(30, 54, 400, 400),0)
        self.screen.blit(self.background, (0,0))
        pygame.display.update()        

    def ShowButtons(self):

        buttonSize = (10, 20)
        index = 0

        for text in textButtons:
            button = Button((500, 100 + index), text)
            index += 50
            self.buttons.add(button)
            self.screen.blit(button.image, button.rect)
        pygame.display.update() 

    def ShowRectangles(self):

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
                recClass(rectangle, self.screen)
                self.rectangleGroup.append(rectangle)
                rect_change_y += change

                if y % 3 == 0 :
                    rect_change_y +=2

            rect_change_x += change
            rect_change_y = 0
            if x % 3 == 0 :
                rect_change_x +=2

        # rectangleSprite = RectangleSprite(self.rectangleSprites)
        # rectangleSprite = self.GetRectangleSprite(sector)
        pygame.display.update() 

    # IF A RECTANGLE HAS BEEN CLICKED - RETURN IT
    def selectRectangle(pos):
        print "clicked rectangle"
        index = 0
        for R in self.rectangleGroup:
            if R.collidepoint(pos):
                return R, index
            index += 1
        return None

        # CHECKS IF CLICKS ON BOARD
    def clickInBoard(self, pos):
        # if clicked on the board
        print "has clicked in BOARD"
        for R in self.backRectangle.sprites():
            # checks if rectangle is true - selected
            if R.collidepoint(pos):
                event = SelectedRectangle(R)
                event_manager.post(ev)
                return True
        return False

        # CHECKS IF BUTTON CLICKED
    def buttonClick(self, pos):
        buttonClicked = False
        for B in self.buttons.sprites():
            if B.collidepoint(pos):
                buttonClicked = True
                id = B.text
                break
        if buttonClicked:
            selectedButton(id)

    def selectedButton(self, id):

        # starts the game
        if id is textButtons[0]:
            pass

        elif id is textButtons[1]:
            pass

        elif id is textButtons[2]:
            pass

        elif id is textButtons[3]:
            pass

        # IF SOMETHING HAS BEEN clicked
    def clicked(self, pos):
        print "clicked"
        if(clickInBoard(pos) == True):
            rectagle, index = selectRectangle(pos)
            ev = SelectedRectangle(rectangle)
            self.rectangle = rectangle
        else:
            buttonClick(pos)

        # DEALS WITH NOTIFICATIONS TO BOARD
    def Notify(self, event):
        print "notified PYGAME"
       # if isinstance(event, TickEvent):
        #    print ""
           # Draw Everything
        #    self.backRectangle.clear( self.window, self.background)
         #   self.rectangleSprites.clear( self.window, self.background)

         #   self.backRectangle.update()

            # pygame.display.update()

        if isinstance(event, BoardBuiltEvent):
            board = event.board
            self.ShowBoard(board)
        elif isinstance(event, MouseClick):
            print "MouseClick"
            pos = event.pos
            self.clicked(pos)
        elif isinstance(event, QuitEvent):
            pygame.quit()
        elif isinstance(event, )
        elif isinstance(event, SelectedButton):
            self.buttonSelected = event.B

#------------------------------------------------------------------------------
class Board(pygame.sprite.Sprite):
    """..."""
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)
        self.rectangles = range(81)
        self.selected = None
        self.index = 0

    def Build(self):
        for i in range(81):
            self.rectangleGroup[i] = 0
        ev = BoardBuiltEvent(self)
        self.evManager.post(ev)

    def Notify(self, event):
        
        # deals with selection of rectangles
        if isinstance(event, SelectedRectangle):
            self.selected = event.rectangle
            id = 0
        elif isinstance(event, DeselectedRectangle):
            self.selected = event.rectangle
            id = 1
        elif isinstance(event, CorrectNumber):
            self.selected = event.rectangle
            id = 2
        elif isinstance(event, IncorrectNumber):
            self.selected = event.rectangle
            id = 3

        if(self.selected != None):
            self.selected.setState(id)

        elif isinstance(event, number):
            if(self.selected !=None):
                self.selected = event.number
                event.rectangle.colour.select() 
                self.selected = None

#------------------------------------------------------------------------------
    # RECTANGLE CLASS
class recClass(pygame.sprite.Sprite):

    def __init__(self, rectangle, screen):
        pygame.sprite.Sprite.__init__(self)

        self.screen =screen
        self.colour = COLOURS[0]
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(self.colour)
        self.rectangle = rectangle
        self.freeze = False
        self.number = None
        # draws  it
        pygame.draw.rect(self.screen, self.colour, self.rectangle)

    def update(self):
        self.image.fill(self.colour)

        # Draws number
    def updateNumber(self, number):
        # If we have not frozen this one yet... and if we are not passing through None
        if(freeze != True and number != None):
            self.number = number
            font = pygame.font.SysFont(chr(self.number), 30, bold = False, italic = False)
            text = font.render("Suduko Solver", 1, (10, 10, 10)) 
            textpos.centerx = self.rectangle.centerx
            textpos.centery = self.rectangle.centery
            
        elif number == None:
            self.update()

        self.image.blit(text, textpos)

    def setState(self, id):
        if(freeze != True):
            self.colour = COLOURS[id]
            # If correct freezes the cell
            if(id == 2):
                self.freeze = True
