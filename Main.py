from eventManager import *
from pyGame import *
from StartScreen import *
from Game import *
from keyBoardManager import *
from CPUSpinnerController import *


# MAIN
def main():
	event_manager = EventManager()
	game = Game(event_manager)
	StartScreen()
	pyGame(event_manager)
	input_controller = KeyboardController(event_manager)
	spinner = CPUSpinnerController(event_manager)
	spinner.run()

# CALL FOR MAIN
if __name__ == "__main__":
	main()