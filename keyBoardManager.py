import pygame
from pygame.locals import *
from eventManager import *
import pyHook
from eventManager import *


class KeyboardController:

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

# This deals with anything which happens in event on keyboard
# Handle input events.
    def Notify(self, event):

        if isinstance(event, TickEvent):

            pygame.time.wait(5)

            for event in pygame.event.get():
                ev = None
                # QUIT GAME
                if event.type == pygame.QUIT and event.key == pygame.K_ESCAPE:
                    ev = QuitEvent()
                elif event.type == KEYDOWN: 
                    try:
                        number = int(event.unicode)
                        if number <= 9 and number >= 1:
                            ev = NumberEvent(number)
                    except Exception, e:
                        print "NAN"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    ev = MouseClick(pos)

                if ev:
                    self.evManager.post(ev)
                