class Event:
    def __init__(self):
        self.name = "Generic Event"

class TickEvent(Event):
    def __init__(self):
        self.name = "Tick Event"

class QuitEvent(Event):
    def __init__(self):
        self.name = "Quit Event"

class GameStartedEvent(Event):
    def __init__(self, game):
        self.name = "Game Started Event"
        self.game = game

class BoardBuiltEvent(Event):
    def __init__(self, board):
        self.name = "Board Built"
        self.board = board

class MouseClick(Event):
    def __init__(self, pos):
        print " CLICKED EVENT"
        self.name = "Mouse Click Event"
        self.pos = pos

class SelectStartEvent(Event):
    def __init__(self, pos):
        self.name = "Select Start Event"
        self.pos = pos

class SelectEndEvent(Event):
    def __init__(self, pos):
        self.name = "Select End Event"
        self.pos = pos

class NumberEvent(Event):
    def __init__(self, number):
      #  print number
        self.name = "Number"
        self.number  = number

class SelectedButton(Event):
    def __init__(self, button):
        self.name = "Button Selected"
        self.button = button
        
class SelectedRectangle(Event):
    def __init__(self, rectangle):
        self.name = "rectangle Selected"
        self.rectangle= rectangle


class EventManager:

    # coordinates communication between different classes
    # creates weak dictionary to listen
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = []

    def RegisterListener(self, listener):
        self.listeners.append(listener)

        for listener in enumerate(self.listeners):
            print listener

    def UnregisterListener(self, listener):
        if listener in self.listeners.keys():
            listeners.remove(listener)

    def post(self, event):
        try:
            for pos, listener in enumerate(self.listeners):
                listener.Notify(event)
        except KeyError:
            print "No Listener"
            pass