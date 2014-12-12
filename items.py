class Item():
    """The default class for all items, use this class if you are new to the game"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
class Silver(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Silver",
                         description="A beautifully decorated round coin with {} stamped on the front. It is said that these coins were only found on bodies lurking inside the ruins. Most people disagree with this theory however because not one person has ever returned from The Ruins alive. .".format(str(self.amt)),
                         value=self.amt)
                         class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
 
class Book(Weapon):
    def __init__(self):
        super().__init__(name="Book",
                         description="A Book that you just so happened to notice as you walked into the Weaponsmith. Don't know why you would want to take the book instead of a Mace or a Sword, but it's your life to lead. As you look at the book more you realize that it is a book about the history of your village, but when you open it, the language used in the book is something that is out of this world.",
                         value=0,
                         damage=5)
 
 
class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A particularly large sword that the Weaponsmith tells you had been used in the great battle of the ruins, .",
                         value=10,
                         damage=10)
                         
class Brimstone(Weapon):
    def __init__(self):
        super().__init__(name="Brimstone",
                         description="A stone completely identical to the average rock, although strangely enough you feel as though it has a skin-like texture to it. It seems to often pus out blood in a straight line at random.",
                         value=0,
                         damage=7)

class Brimstone(Weapon):
    def __init__(self):
        super().__init__(name="Mace",
                         description="Back in the War of the Village, this very rusty Mace was used to fight off the Skeletons from The Ruins. Most people think that weapons like this should be with the soilders at the memorial, but the Weaponsmith insists that if something like that were to happen again, people would want them to be here.",
                         value=10,
                         damage=12)
