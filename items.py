class Item():
    """The default class for all items, use this class if you are new to the game"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Silver",
                         description="A beautifully decorated round coin with {} stamped on the front. It is said that these coins were only found on bodies lurking inside the ruins. Most people disagree with this theory however because not one person has ever returned from The Ruins alive. .".format(str(self.amt)),
                         value=self.amt) 		
