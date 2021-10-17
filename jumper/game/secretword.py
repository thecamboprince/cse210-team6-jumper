## SecretChar will have acces to the characters and set them as hidden.
class SecretChar: 
	def __init__(self,letter):
		self.isHidden = True
		self.letter = letter
		
class SecretWord: # Handles the secret word. (is it solved? set it, which are showing)
	
	def __init__(self):
		self.secretChars = [] # the SecretWord as an array of SecretChars

	def setWord(self,NewWord): # intializes secretChars and appends the letters that are in it.
		for char in NewWord:
			letter = SecretChar(char)
			self.secretChars.append(letter)


	def getChar(self, letterIndex): # returns the char at index or '_' if it isHidden.
		stored_char = self.secretChars[letterIndex]
		if stored_char.isHidden:
			return "_"
		else:
			return stored_char.letter
	

	def getLength(self): # gets length of the word
		return len(self.secretChars)
		
	def isUnsolved(self): ## It iterates through secretChars (each letter) and checks if every single word is indeed hidden.
		for c in self.secretChars:
			if c.isHidden:
				return True
			else:
				return False
	
## For the guess method it first sets it up to false so we can iterate through each letter (even if it has letter that repeat),
## Then it iterates through secretChars and checks if the letter the user inputted is equal to what we have there
## if it is it setups isHidden to False and show the letter on the display.
	def guess(self, letter): 
		wasCorrect = False
		for l in self.secretChars:
			if l.letter == letter:
				l.isHidden = False
				wasCorrect = True
		return wasCorrect