class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен по цене {price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена на {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден.")



store1 = Store("Магазин 1", "Улица 1, д. 1")
store2 = Store("Магазин 2", "Улица 2, д. 2")
store3 = Store("Магазин 3", "Улица 3, д. 3")


store1.add_item("Яблоки", 50)
store1.add_item("Бананы", 75)

store2.add_item("Хлеб", 25)
store2.add_item("Молоко", 40)

store3.add_item("Кофе", 150)
store3.add_item("Чай", 100)


print("\nТестирование методов на примере магазина 1:")
store1.add_item("Апельсины", 60)
print("Цена на Яблоки:", store1.get_price("Яблоки"))
store1.update_price("Яблоки", 55)
print("Обновленная цена на Яблоки:", store1.get_price("Яблоки"))
store1.remove_item("Бананы")
print("Цена на Бананы:", store1.get_price("Бананы"))