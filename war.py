from abc import ABC, abstractmethod
import random


# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."


# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.__class__.__name__.lower()}.")

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        return "У бойца нет оружия!"


# Класс Monster
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_defeated(self):
        return self.health <= 0

    def take_damage(self):
        damage = random.randint(1, 10)
        self.health -= damage
        return damage


# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    print(f"{monster.name} появляется!")

    while not monster.is_defeated():
        print(fighter.attack())
        damage = monster.take_damage()
        print(f"{monster.name} получает {damage} урона. Здоровье: {monster.health}")

        if monster.is_defeated():
            print(f"{monster.name} побежден!")
            break


# Пример использования
if __name__ == "__main__":
    fighter = Fighter("Герой")

    # Бой с мечом
    sword = Sword()
    fighter.change_weapon(sword)
    monster1 = Monster("Монстр", 30)
    battle(fighter, monster1)

    print("\n---\n")

    # Бой с луком
    bow = Bow()
    fighter.change_weapon(bow)
    monster2 = Monster("Другой Монстр", 30)
    battle(fighter, monster2)