class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.MAX_HEALTH = 100

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_damage(self, damage_points):
        if damage_points > self.health:
            self.health = 0
        else:
            self.health -= damage_points

    def can_cast(self):
        return self.mana > 0

    def take_healing(self, healing_points):
        if not self.is_alive():
            self.health += healing_points
        return True
