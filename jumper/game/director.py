

class Director: # Directs the game. (tracks game state, turns, and flow control.)

	def __init__(self):
		self.currentPlayer = "P1" 	# is either P1 or P2
		self.isRunning = True 		# determines if the game is currently running
		self.p1Score = 0
		self.p2Score = 0

		self.display = Display()
		self.secretWord = SecretWord()
		self.jumper = Jumper()

	def run_game(self):
		while self.isRunning:
			didWin = self.play_round()

			if didWin:
				self.addPoint()
			
			if self.display.promptEndGame().lower() == 'y':
				self.isRunning = False

	def play_round(self):
		# so I don't have to write "self." every two seconds
		display = self.display
		secretWord = self.secretWord
		jumper = self.jumper

		secretWord.setWord(display.promptNewWord(self.currentPlayer))
		self.toggleCurrentPlayer()
		display.clearScreen() # so p2 can't see the word p1 chose

		while secretWord.isUnsolved() and jumper.isAlive():
			display.show(secretWord)
			display.show(jumper)

			letter = display.promptForLetter(self.currentPlayer)
			if not secretWord.guess(letter):
				jumper.breakStrands()

		# final view; no guess
		display.show(secretWord) 
		display.show(jumper)

		return jumper.isAlive() # return if they won

	def addPoint(self): # to the current player
		pass

	def toggleCurrentPlayer(self):
		pass