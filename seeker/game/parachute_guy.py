
class ParachuteGuy:
    """The graphic countdown of how many wrong guesses are left. 
    The responsibility of a ParachuteGuy is to draw the jumper

    Attributes:
        jumper_image(list of strings)
    """
    


    def __init__(self):
        """Constructs a ParachuteGuy.

        Args:
            self (ParachuteGuy): An instance of ParachuteGuy.
        """
        self._jumper_image = ["  ___", " /___\\", " \   /", "  \ /", "   O",
        "  /|\\", "  / \\", "\n^^^^^^^" ]

    def get_jumper(self):
        return self._jumper_image
        
    def update_jumper(self, alive):

        self._jumper_image.pop(0) 
        if alive == False:
            self._jumper_image.insert(0, "   x")
            

    
        

    

        
        
       

        
