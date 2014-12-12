from The-Ruins-Text-Adventure import items, enemies
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def intro_text(self):
    raise NotImplementedError()
 
def modify_player(self, player):
    raise NotImplementedError()
class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You awake with only the simple idea that you were sent here by your village. You remember being awaked by the priest early yesterday morning with him telling you that you would be taken to The Ruins just outside the village
        as you hear the grinding shut to the door behind you, everything becomes dark and you fiddle to find you torch. As the blazing warmth of the torch engulfs your body, you see that there are three different pathways for you to walk down.
        You remember that the priest told you to "walk down the right most path, but you can go Forward, Left, or Right.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass    
