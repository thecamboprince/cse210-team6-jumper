from display import Display
from secretword import SecretWord
from jumper import Jumper

class Director: # Directs the game. (tracks game state, turns, and flow control.)
	"""A code template for a person who directs the game. The responsibility of 
    this class of objects is to track score, turns, and control sequence of play.

    
    Attributes:
		currentPlayer (string): Represents who is playing. Either "P1" or "P2".
        isRunning (boolean): Whether or not the game is running.
        p1score (number): The total number of points earned by Player 1.
		p2score (number): The total number of points earned by Player 2.
        display (Display): An instance of the class of objects known as Display.
		secretWord (SecretWord): An instance of the class of objects known as SecretWord.
		jumper (Jumper): An instance of the class of objects known as Jumper.
    """

	def __init__(self):
		"""Initializes the Director class object with scores of 0, a Display/SecretWord/Jumper objects,
		the game running, and the first player as "P1".

        Args:
            self (Director): An instance of Director.
        """
		self.currentPlayer = "P1"
		self.isRunning = True
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
		"""Plays one round of the game. Displays the word and jumper, guesses, and repeats until the round ends.

        Args:
            self (Director): An instance of Director.
        
        Returns:
            boolean: Representing if the currentPlayer won the round.
        """
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

		return jumper.isAlive() # if Jumper is still alive, they won

	def addPoint(self):
		"""Adds one point to whoever is currently playing

        Args:
            self (Director): An instance of Director.
        """
		if self.currentPlayer == "P1":
			self.p1Score += 1
		else:
			self.p2Score += 1

	def toggleCurrentPlayer(self):
		"""Swaps the currentPlayer. Either P1 to P2 or vice versa.

        Args:
            self (Director): An instance of Director.
        """
		self.currentPlayer = "P2" if self.currentPlayer == "P1" else "P1"