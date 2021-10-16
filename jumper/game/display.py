class Display: # Handles all of the printing. (Think of it as the "screen".)
	
	def __init__(self):
		self.parachuteModel = ["  ___  "," /___\ "," \   / ","  \ /  "]

	def promptNewWord(self, currentPlayer): # returns the new word
		pass

	def clearScreen(self):
		pass # either actually clears the screen, or vomits a wall of text

	def show(self, objToDisplay):
		if objToDisplay is SecretWord:
			pass
		elif objToDisplay is Jumper:
			pass
		else:
			print(objToDisplay)

	def promptForLetter(self, currentPlayer): # returns the letter they guessed
		pass

	def promptEndGame(self, currentPlayer): # returns 'Y' or 'N'
		pass