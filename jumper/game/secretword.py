class SecretChar:
	"""A code template for the secretchar. The responsibility of 
    this class of objects is to store a char and whether it is hidden.

    
    Attributes:
        isHidden (Boolean): Represents if the char is hidden.
		letter (char): The letter to display when not hidden.
    """
	def __init__(self, letter):
		"""Initializes the SecretChar class object as hidden with a letter.

        Args:
            self (SecretChar): An instance of SecretChar.
			letter (char): The letter to keep a secret.
        """
		self.isHidden = True
		self.letter = letter

class SecretWord:
	"""A code template for the secretword. The responsibility of 
    this class of objects is to store a secretword and report about it.

    
    Attributes:
        secretChars (list[SecretChar]): A list of SecretChar objects representing the SecretWord
    """
	def __init__(self):
		"""Initializes the SecretWord class object with an empty array of secretChars

        Args:
            self (SecretWord): An instance of SecretWord.
        """
		self.secretChars = [] # the SecretWord as an array of SecretChars

	def setWord(self, newWord): # intializes secretChars
		"""Initializes the secretChars list with chars from the newWord.

        Args:
            self (SecretWord): An instance of SecretWord.
			newWord (String): Representing the word to store.
        """
		for char in newWord:
			self.secretChars.append(SecretChar(char))

	def getChar(self, index): # returns the char at index or '_' if it isHidden
		"""Gets the char that should be displayed at a given index.

        Args:
            self (SecretWord): An instance of SecretWord.
			index (Number): Representing the index of the char to return.

		Returns:
			char: The letter in the word or "_" at the specified index.
        """
		charAtIndex = self.secretChars[index]
		if charAtIndex.isHidden:
			return "_"
		else:
			return charAtIndex.letter

	def getLength(self): # gets length of the word
		"""Gets the length of the SecretWord.

		Returns:
			number: The length of the word.
        """
		return len(self.secretChars)

	def isUnsolved(self):
		"""Returns a boolean representing if the word isUnsolved.
		
		Returns:
			Boolean: True if it is unsolved. False if it is solved.
        """
		for c in self.secretChars:
			if c.isHidden:
				return True
		return False
	
	def guess(self, guessedLetter): # returns true if correct
		"""Returns true if the guess was correct. Unhides letters appropriately.

        Args:
            self (SecretWord): An instance of SecretWord.
			guessedLetter (char): The letter that the player guessed.

		Returns:
			Boolean: Representing whether or not the guess was correct.
        """
		isGuessCorrect = False
		for c in self.secretChars:
			if c.letter.lower() == guessedLetter.lower():
				isGuessCorrect = True
				c.isHidden = False
		return isGuessCorrect