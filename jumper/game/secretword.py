class SecretChar:
	def __init__(self, letter):
		self.isHidden = True
		self.letter = letter

class SecretWord: # Handles the secret word. (is it solved? set it, which are showing)
	
	def __init__(self):
		self.secretChars = [] # the SecretWord as an array of SecretChars

	def setWord(self, newWord): # intializes secretChars
		for char in newWord:
			self.secretChars.append(SecretChar(char))

	def getChar(self, index): # returns the char at index or '_' if it isHidden
		charAtIndex = self.secretChars[index]
		if charAtIndex.isHidden:
			return "_"
		else:
			return charAtIndex.letter

	def getLength(self): # gets length of the word
		return len(self.secretChars)

	def isUnsolved(self):
		for c in self.secretChars:
			if c.isHidden:
				return True
		return False
	
	def guess(self, guessedLetter): # returns true if correct
		isGuessCorrect = False
		for c in self.secretChars:
			if c.letter == guessedLetter:
				guessIsCorrect = True
				c.isHidden = False
		return isGuessCorrect