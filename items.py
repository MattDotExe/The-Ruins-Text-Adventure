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
 
 
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)
 
 
class Wooden Club(Weapon):
    def __init__(self):
        super().__init__(name="Wooden Club",
                         description="A Large Wooden Club that seems to have a dried blood covered everywhere. I wonder what happened..",
                         value=10,
                         damage=10)
                         
class Brimstone(Weapon):
    def __init__(self):
        super().__init__(name="Brimstone",
                         description="A stone completely identical to the Rock, although strangely enough you feel as though it has a skin-like texture to it. It seems to often pus out blood in a straight line at random",
                         value=0,
                         damage=5)
                         
