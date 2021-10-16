class SecretWord: # Handles the secret word. (is it solved? set it, which are showing)
	
	def __init__(self):
		self.secretChars = [] # the SecretWord as an array of SecretChars

	def setWord(self): # intializes secretChars
		pass

	def getChar(self, index): # returns the char at index or '_' if it isHidden
		pass

	def getLength(): # gets length of the word
		pass

	def isUnsolved(self):
		for c in self.secretChars:
			if c.isHidden:
				return True
		return False
	
	def guess(self, letter): # returns true if correct
		pass

class SecretChar:
	def __init__(self):
		self.isHidden = True
		self.value = ''