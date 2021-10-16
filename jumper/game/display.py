from game.secretword import SecretWord
from game.jumper import Jumper
from os import system, name

# Chase
class Display:
	""" Displays part of the game

        Attributes:
            display (Display): An instance of Display.
			parachuteModel (Array): set of objects for displaying a figure
			secretWord (SecretWord): An instance of the class of objects known as SecretWord.
			objToDisplay (objToDisplay): An instance of the class of objects known as objToDisplay.
			currentPlayer (currentPlayer): An instance of the class of objects known as currentPlayer.
    """

	def __init__(self):
		"""The class constructor

		Args:
			self (Display): an instance of Display	
		"""
		self.parachuteModel = ["  ___  "," /___\ "," \   / ","  \ /  "]


	def promptNewWord(self, currentPlayer):
		""" Returns the new word of the player's choice

		Args:
			self (Display): an instance of Display

		Returns:
			string: string values represent player's word. The user's input as a string.
		""" 
		return input(f'{currentPlayer} What would you like the word to be?: ')

	 
	def clearScreen(self):
		""" Clears screen to hide from word from other player

		Args:
			self (Display): an instance of Display
		"""

		# for windows
		if name == 'nt':
			_ = system('cls')
		# for mac and linux(here, os.name is 'posix')
		else:
			_ = system('clear')

	 
	def show(self, objToDisplay):
		""" Diplays objects of the game

		Args:
			self (Display): an instance of Display
			objToDisplay (objToDisplay): An instance of the class of objects known as objToDisplay.
			placeholder (string): is an empty string that prints on every iteration
			printjumpman (printjumpman): prints the model of jumpman
			
		"""
		if objToDisplay is SecretWord:
			placeholder = ""
			for i in range (0, objToDisplay.getLenth()):
				# placeholder += objToDisplay.getChar(i) + " "
				placeholder = placeholder + objToDisplay.getChar(i) + " "
			print(placeholder)
		elif objToDisplay is Jumper:
			for i in range (objToDisplay.getNumStrands() - objToDisplay.getNumStrandsLeft(), objToDisplay.getNumStrands()):
				print(self.parachuteModel[i])
			self.printjumpman()
		else:
			print(objToDisplay)
		


	def printjumpman(self, jumper):
		""" Creates model of the jumpman

		Args:
			self (Display): an instance of Display
		"""
		jumpManModel = [
		"   0   ",
		"  /|\  ",
		"  / \  "
		]

		i = 0
		for part in jumpManModel:
			if not jumper.isAlive() and i == 0:
				print("   X   ")
			else:
				print(part)
			i += 1
			

	def promptForLetter(self, currentPlayer): 
		""" Returns the letter they guessed

		Args:
			self (Display): an instance of Display
			currentPlayer (currentPlayer): An instance of the class of objects known as currentPlayer.
		"""
		return input(f'{currentPlayer} Guess a Letter [a-z]: ')

	 
	def promptEndGame(self):
		""" returns 'Y' or 'N'

		Args:
			self (Display): an instance of Display
		""" 
		return input("Would you like to end game [Y/N]: ")
		
		