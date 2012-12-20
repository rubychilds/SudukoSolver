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
            for event in pygame.event.get():
                ev = None
                # QUIT GAME
                if event.type == pygame.QUIT and event.key == pygame.K_ESCAPE:
                    ev = QuitEvent()

                # MOUSE CLICK
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    point = event.pos
                    ev = MouseClick(point)
                
                elif event.type == KEYDOWN:
                # NUMBER ENTERED
                    if int(event.unicode) <= 9 and int(event.unicode) >= 1:
                        ev = Number(int(event.unicode))
               
                # if we do have an event then we pass this onto event Manager
                if ev != None:
                    self.evManager.post(ev)