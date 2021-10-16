class Jumper:
	"""A code template for person jumping with a parachute. The responsibility of 
    this class of objects is to track the parachute and person's vitality.

    
    Attributes:
        parachuteSize (number): The total number of "strands" on the chute.
		parachuteStrands (number): The total number of "strands" left on the chute.
    """

	def __init__(self):
		"""Initializes the Jumper class object with a chute of size 4 and current strands 4.

        Args:
            self (Jumper): An instance of Jumper.
        """
		self.parachuteSize = 4
		self.parachuteStrands = self.parachuteSize

	def breakStrands(self):
		"""Breaks (subtracts) one of the strands.

        Args:
            self (Jumper): An instance of Jumper.
        """
		self.parachuteStrands -= 1

	def getChuteSize(self):
		"""Returns the number of strands the parachute started with

        Args:
            self (Jumper): An instance of Jumper.
        
        Returns:
            number: Representing the count of strands at the start.
        """
		return self.parachuteSize

	def getStrandsLeft(self):
		"""Returns the number of strands still left

        Args:
            self (Jumper): An instance of Jumper.
        
        Returns:
            number: Representing the count of strands left.
        """
		return self.parachuteStrands

	def isAlive(self):
		"""Checks the number of strands left to see if he is freefalling (dead).

        Args:
            self (Jumper): An instance of Jumper.
        
        Returns:
            boolean: Representing if the jumpMan has/will imminently die.
        """
		return self.getStrandsLeft() > 0