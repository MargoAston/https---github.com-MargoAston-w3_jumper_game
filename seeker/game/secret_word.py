import random

class SecretWord:
    """The secret word choosen from a given list. 
    
    The responsibility of SecretWord is to keep track of secret_word, the correct letters that have been guessed, and the number of incorrect letters guessed. 
    
    Attributes:
        word_bank (list of strings): List of words to choose from.
        secret_word (string): The choosen word.
        hint (list of letters): correct letter guesses
        incorrect_letters (int): number of incorrect letters guessed  
        got_it (int): is letter in word
    """

    def __init__(self):
        """Constructs a new secret_word.

        Args:
            self (SecretWord): An instance of SecretWord.
        """
        # This is the word bank.
        self._word_bank = ['from', 'small', 'and', 'simple', 'things', 'great', 'come', 'to', 'pass']

        # This is the secret word.
        self._secret_word = random.choice(self._word_bank)

        # A list containing an underscore for each letter in the secret word.
        self._hint = []
        for index in range(0, len(self._secret_word)):
            self._hint.append("_")

        # Number of incorrect guesses.
        self._incorrect_guesses = 0

        # Is the letter in the word.
        self._got_it = -1

    def get_word(self):
        return self._secret_word

    def get_hint(self):
        return self._hint
    
    def get_incorrect_guesses(self):
        return self._incorrect_guesses

    def is_found(self, letter):
        """Determines if the guessed letter is in the secret word.

        Args:
            self (SecretWord): An instance of SecretWord.
            
        Returns:
            integer: -1 if letter was not found
        """
        # Looks for letter in secret word, if found places the letter in a list of correct letters.
        self._got_it = -1
        for index in range (0, len(self._secret_word)):
            found_it = self._secret_word.find(letter, index, len(self._secret_word))
            if found_it > -1:
                self._hint[found_it] = letter 
                #Increments index to continue looking for duplicate letters.
                index += found_it
                self._got_it += 1

        if self._got_it == -1:
           self._incorrect_guesses += 1
        
        return self._got_it
        
        
  
