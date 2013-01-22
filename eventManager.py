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

class SelectedRectangle(Event):
    def __init__(self, rectangle):
        self.name = "Select Rectangle"
        self.rectangle = rectangle

class DeselectedRectangle(Event):
    def __init__(self, rectangle):
        self.name = "De-Select Rectangle"
        self.rectangle = rectangle

class CorrectNumber(Event):
    def __init__(self, rectangle, number):
        self.name = "CorrectNumber"
        self.number  = number
        self.rectangle = rectangle

class IncorrectNumber(Event):
    def __init__(self, rectangle, number):
        self.name = "InCorrectNumber"
        self.number  = number
        self.rectangle = rectangle

class Number(Event):
    def __init__(self, number):
        self.name = "InCorrectNumber"
        self.number  = number

class SelectedButton(Event):
    def __init__(self, button):
        self.name = "Button Selected"
        self.button  = button
        

class EventManager:

    # coordinates communication between different classes
    # creates weak dictionary to listen
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def RegisterListener(self, listener):
      #  print "registering "
        self.listeners[listener] = 1
        print listener

    def UnregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def post(self, event):
        print "NOTIFYING"
       # print event.name
        for listener in self.listeners.keys():
            listener.Notify(event)
