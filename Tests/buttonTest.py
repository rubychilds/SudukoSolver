import sys, os
import pygame
from pygame.locals import *

# Simple test for button loading and use of Sprite class inbuilt in pygame

def load_image(name, colorkey=None):
    
 #   fullname = os.path.join('data', name)

    fullname = name
    
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error, message:
        print 'Issue'
        print 'Cannot load image:', fullname
        raise SystemExit, message
    
  #  image = image.convert()
    
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    
    return image, image.get_rect()

class Button(pygame.sprite.Sprite):
    """Class used to create a button, use setCords to set 
        position of topleft corner. Method pressed() returns
        a boolean and should be called inside the input loop."""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('C:\Users\Ruby\Documents\GitHub\SudukoSolver\_button.jpg', -1)
        
    def setCords(self,x,y):
        self.rect.topleft = x,y
        
    def pressed(self,mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

def main():
    pygame.init()
    button = Button() #Button class is created
    button.setCords(200,200) #Button is displayed at 200,200

    while 1:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if button.pressed(mouse):   #Button's pressed method is called
                    print ('button hit')

    self.screen.blit(self.background,(0,0))
    pygame.display.flip()

if __name__ == '__main__': main()