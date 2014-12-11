class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0                         
class Tiny Spider(Enemy):
    def __init__(self):
        super().__init__(name="Tiny Spider", hp=5, damage=2)
 
 
class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton", hp=15, damage=10)


class Humongous Spider(Enemy):
    def __init__(self):
        super().__init__(name="Humongous Spider", hp=20, damage=15)        
