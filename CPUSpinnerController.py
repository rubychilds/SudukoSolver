import time
from eventManager import *


# Deals with event listening
class CPUSpinnerController:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)
        self.keepGoing = True

    def run(self):
        while self.keepGoing:
            event = TickEvent()
            self.event_manager.post(event)
            time.sleep(0.05)

    def Notify(self, event):
		if isinstance (event, QuitEvent):
			self.keepGoing = False
			sys.exit()
