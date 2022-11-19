from game.terminal_service import TerminalService
from game.secret_word import SecretWord
from game.parachute_guy import ParachuteGuy


class Director:
    """A person/class who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        secret_word (SecretWord): The game's secret word.
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
        jumper_image (ParachuteGuy): Graphic countdown for how many wrong guesses are left.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._secret_word = SecretWord()
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._jumper_image = ParachuteGuy()
        
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._do_outputs()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()


    def _get_inputs(self):
        """ Gets letter guess from player and gets position of letter in the secret word.

        Args:
            self (Director): An instance of Director.
        """
        self._hint()
        
        # Prompts player for letter guess.
        letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")

        # Check for letter in the secret word.
        self._letter_index = self._secret_word.is_found(letter)
        
        
    def _do_updates(self):
        """Updates the jumper image and is_playing

        Args:
            self (Director): An instance of Director.
        """
        # Update the jumper image
        if self._letter_index == -1:
            self._jumper_image.update_jumper(self._is_playing)

        # Get the list of correct letters.
        players_guess = self._secret_word.get_hint()
        # Get the secret word and put the letters in a list
        secret = list(self._secret_word.get_word())

        # If the player has 4 incorrect guesses the game ends.
        if self._secret_word.get_incorrect_guesses() == 4:
            self._is_playing = False
            self._jumper_image.update_jumper(self._is_playing)
            self._terminal_service.write_text("So sorry, you lose. Better luck next time.\n")
        # If the player's guess matches the secret word the game ends.
        elif secret == players_guess: 
            print(*players_guess)
            self._is_playing = False
            self._terminal_service.write_text("CONGRATULATIONS! You Win.\n")

    
    def _hint(self):
        """Provides a letter-placement hint for the player. (Hint is encapsulted in SecretWord)

        Args:
            self (Director): An instance of Director.
        """
        print(*(self._secret_word.get_hint()))

    def _do_outputs(self):
        """Provides a graphic countdown for how many wrong guesses are left.

        Args:
            self (Director): An instance of Director.
        """
        newArr = self._jumper_image.get_jumper()
        print(*newArr, sep = "\n")
       
        
    