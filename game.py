import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} на {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            print(f"{self.computer.name} здоровье: {self.computer.health}")
            if not self.computer.is_alive():
                print(f"{self.computer.name} проиграл! {self.player.name} победил!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            print(f"{self.player.name} здоровье: {self.player.health}")
            if not self.player.is_alive():
                print(f"{self.player.name} проиграл! {self.computer.name} победил!")
                break


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()