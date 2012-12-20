import pygame
from pygame.locals import *
from pygame import Color, Rect, Surface

# Used in application of Sprites, and the development of separate classes used in rendering

white = (255,255,255)
black = (0,0,0)

# HELPER FUNCTIONS
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


class Button(pygame.sprite.Sprite):

    def __init__(self, xy, text):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.xy = xy
        self.font = pygame.font.SysFont('Subway Black', 20, bold = False, italic = False)
        self.colour = (255,255,255)
        self.generateImage()

    def generateImage(self):
        # draw text with a solid background - about as simple as we can get
        self.image = self.font.render(self.text, True, self.colour, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.xy

# MAIN FUNCTION 
def main():

    pygame.init()
    size=[700,500]
    # set mode - sets size of screen
    screen=pygame.display.set_mode(size)

    background = pygame.Surface(screen.get_size())

    # sets default text
    font = pygame.font.SysFont('Subway Black', 30, bold = False, italic = False)
    screen.fill(white)
    # convert allows speed out of blits
    background = background.convert()
    background.fill ((255,255,255))

    # starts up the background whilst we wait for other resources to load
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # sets default font for game
    font = pygame.font.Font(None, 36)
    # renders title render("text", anti-aliased - 1-yes, 0-no , colour)
    text = font.render("Test", 1, (10, 10, 10))
    # positioning of text
    textpos = text.get_rect(centerx = background.get_width()/2)
   # blits text
    background.blit(text, textpos)
    # attaches background to screen
    screen.blit(background,(0,0))
    # sets window caption
    pygame.display.set_caption("Test")

   # try:
    #    image = pygame.image.load("example.jpg")
        # .convert()
    # except pygame.error, message:
      #  print 'Issue'
       # print 'Cannot load image:', fullname
        # raise SystemExit, message



    sprites = pygame.sprite.RenderUpdates()

    buttonStart = Button( (100,100), "Start Game")
    sprites.add(buttonStart)
    dirty = sprites.draw(screen)

  #  rectangle = Rect(40, 40, 10, 10)
    #pygame.draw.ellipse(screen,black,[20,20,250,100],2) 

    # puts image onto screen
   # screen.blit(image, (0,0) , rectangle)

    # clock - can be used to retain a certain image on the board etc.
    clock = pygame.time.Clock()
 
    done = False
    # -------- Main Program Loop -----------
    while done==False: # can also fo while 1:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user clicked close
                done = True 

        # flip- applies graphics to screen. can use update to update the whole window , or use update(rectangle) for part of the image
        pygame.display.flip()

        pygame.display.update(dirty)                        # updates just the 'dirty' area


if __name__ == '__main__': main()