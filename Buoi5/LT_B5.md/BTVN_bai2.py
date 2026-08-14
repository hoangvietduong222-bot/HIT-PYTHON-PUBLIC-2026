class Character:

    def __init__(self, name, hp, level):
        self.name = name
        self.__hp = hp
        self._level = level

    def get_hp(self):
        return self.__hp

    def take_damage(self, damage):
        if damage > 0:
            self.__hp -= damage

            # HP không được nhỏ hơn 0
            if self.__hp < 0:
                self.__hp = 0

    def heal(self, amount):
        if amount > 0:
            self.__hp += amount

    def attack(self):
        return 0

    def show_info(self):
        print(f"Tên: {self.name}")
        print(f"HP: {self.__hp}")
        print(f"Level: {self._level}")


class Warrior(Character):
    def __init__(self, name, hp, level, strength):
        super().__init__(name, hp, level)
        self.strength = strength

    def attack(self):
        damage = self._level * 5 + self.strength
        return damage

    def show_info(self):
        super().show_info()
        print(f"Strength: {self.strength}")


class Mage(Character):

    def __init__(self, name, hp, level, mana, magic_power):
        super().__init__(name, hp, level)
        self.__mana = mana
        self.magic_power = magic_power

    def attack(self):
        if self.__mana < 10:
            return 0
        
        self.__mana -= 10

        damage = self._level * 3 + self.magic_power
        return damage

    def show_info(self):
        super().show_info()
        print(f"Mana: {self.__mana}")
        print(f"Magic Power: {self.magic_power}")


characters = [
    Warrior("Warrior 1", 150, 10, 20),
    Warrior("Warrior 2", 180, 8, 25),
    Mage("Mage 1", 100, 12, 50, 30),
    Mage("Mage 2", 120, 10, 40, 35)
]


damage = characters[0].attack()
characters[1].take_damage(damage)

damage = characters[1].attack()
characters[0].take_damage(damage)

damage = characters[2].attack()
characters[3].take_damage(damage)

damage = characters[3].attack()
characters[2].take_damage(damage)


print("THÔNG TIN SAU KHI CHIẾN ĐẤU")

for character in characters:
    character.show_info()
    print("\n")


max_character = characters[0]

for character in characters:
    if character.get_hp() > max_character.get_hp():
        max_character = character

print("Nhân vật còn nhiều HP nhất:")
print(max_character.name)
print("HP:", max_character.get_hp())


print("\nKIỂM TRA isinstance()")

for character in characters:
    if isinstance(character, Warrior):
        print(character.name, "là Warrior")

    if isinstance(character, Mage):
        print(character.name, "là Mage")


print("\nKIỂM TRA issubclass()")

print("Warrior kế thừa Character:",
      issubclass(Warrior, Character))

print("Mage kế thừa Character:",
      issubclass(Mage, Character))