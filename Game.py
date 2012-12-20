from eventManager import *

class Game:

	STATE_CONFIG = -1
	STATE_RUNNING = 1
	STATE_PAUSED = 0

	def __init__(self, event_manager):
		self.event_manager = event_manager
		self.event_manager.RegisterListener(self)
		self.state = Game.STATE_CONFIG

	def Start(self):
		self.state = Game.STATE_PAUSED
		event = GameStartedEvent(self)
		self.state = Game.STATE_RUNNING
		self.event_manager.post(event)
		
	def Notify(self, event):
		if isinstance(event, TickEvent):
			if self.state == Game.STATE_CONFIG:
				self.Start()
