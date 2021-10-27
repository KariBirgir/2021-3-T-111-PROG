class PlayerCharacter:
    def __init__(self, max_hp=10, level=1):
        self.max_hp = max_hp if max_hp > 0 else 10
        self.current_hp = self.max_hp
        self.level = level if level > 0 else 1

    def __str__(self):
        return f"Player with {self.current_hp} HP out of {self.max_hp} HP at level {self.level}"

    def take_damage(self, damage):
        self.current_hp -= damage
    
    def heal(self, heal_amount):
        self.current_hp += heal_amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def level_up(self):
        self.level += 1
        self.max_hp += 3*self.level
        self.current_hp = self.max_hp

    def is_dead(self):
        return self.current_hp <= 0