import random

class Jumper:

    def open_file(self):
        """ Import text file of words 

        """
        with open("words.txt") as f:
            word_list = f.read().splitlines()

    def random_word(self):
        """ Gets random words from the text file to guess

        """
        random_num = random.randint(0, len(self.open_file.word_list)-1)
        word_chosen = self.open_file.word_list[random_num]
        return random_num