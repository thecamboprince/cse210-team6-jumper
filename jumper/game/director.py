

class Director:

    def int(self):
        pass

    def jumper(self):
        guess = input("Guess a letter [a-z]:").lower()
        if guess in self.secret_word:
            return False
        else:
            return True
    #I chose to arange the true false because I thought that what ever jumper it goes to whether to cut the parachute or not. Feel free to change it
    #I like the enhancement of the word selection from being an external file. there is a prepared file with a bunch of words.
'''Compares to see if the user's input is in the string and returns either true or false'''