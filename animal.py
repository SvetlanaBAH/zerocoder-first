import json

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def eat(self):
        print(f"{self.name} is eating.")

# Подкласс Bird
class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

# Подкласс Mammal
class Mammal(Animal):
    def make_sound(self):
        return "Roar!"

# Подкласс Reptile
class Reptile(Animal):
    def make_sound(self):
        return "Hiss!"

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} says: {animal.make_sound()}")

# Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Added staff member {staff_member.name}.")

    def save_to_file(self, filename):
        zoo_data = {
            "animals": [{"name": animal.name, "age": animal.age, "type": type(animal).__name__} for animal in self.animals],
            "staff": [{"name": staff_member.name, "type": type(staff_member).__name__} for staff_member in self.staff]
        }
        with open(filename, 'w') as file:
            json.dump(zoo_data, file)
        print(f"Zoo data saved to {filename}.")

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            zoo_data = json.load(file)
            for animal_data in zoo_data["animals"]:
                if animal_data["type"] == "Bird":
                    animal = Bird(animal_data["name"], animal_data["age"])
                elif animal_data["type"] == "Mammal":
                    animal = Mammal(animal_data["name"], animal_data["age"])
                elif animal_data["type"] == "Reptile":
                    animal = Reptile(animal_data["name"], animal_data["age"])
                self.add_animal(animal)
            for staff_data in zoo_data["staff"]:
                if staff_data["type"] == "ZooKeeper":
                    staff_member = ZooKeeper(staff_data["name"])
                elif staff_data["type"] == "Veterinarian":
                    staff_member = Veterinarian(staff_data["name"])
                self.add_staff(staff_member)

# Класс ZooKeeper
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

# Класс Veterinarian
class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

# Пример использования
if __name__ == "__main__":
    zoo = Zoo()

    # Добавление животных
    bird = Bird("Parrot", 2)
    mammal = Mammal("Lion", 5)
    reptile = Reptile("Snake", 3)

    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)

    # Добавление сотрудников
    keeper = ZooKeeper("Alice")
    vet = Veterinarian("Bob")
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Демонстрация полиморфизма
    animal_sound(zoo.animals)

    # Сохранение состояния зоопарка в файл
    zoo.save_to_file('zoo_data.json')

    # Создание нового зоопарка и загрузка данных из файла
    new_zoo = Zoo()
    new_zoo.load_from_file('zoo_data.json')
    animal_sound(new_zoo.animals)


