class Store:
    def __init__(self, name, address):
        self.name = name  # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Ассортимент товаров (словарь)

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def __str__(self):
        """Возвращает строковое представление магазина и его ассортимента."""
        items_list = ', '.join([f"{item}: {price}" for item, price in self.items.items()])
        return f"Магазин '{self.name}' по адресу '{self.address}'. Ассортимент: {items_list if items_list else 'Нет товаров'}."


# Пример использования
if __name__ == "__main__":
    store = Store("Магазин фруктов", "Улица Фруктовая, 123")

    # Добавление товаров
    store.add_item("яблоки", 0.5)
    store.add_item("бананы", 0.75)

    # Вывод информации о магазине
    print(store)

    # Получение цены товара
    print("Цена яблок:", store.get_price("яблоки"))

    # Обновление цены товара
    store.update_price("яблоки", 0.6)
    print("Обновленная цена яблок:", store.get_price("яблоки"))

    # Удаление товара
    store.remove_item("бананы")
    print(store)

    # Пример использования
    if __name__ == "__main__":
        store = Store("Бакалея", "Улица Гороховая, 123")

        # Добавление товаров
        store.add_item("рис", 0.1)
        store.add_item("сахар", 0.1)

        # Вывод информации о магазине
        print(store)

        # Получение цены товара
        print("Цена риса:", store.get_price("рис"))

        # Обновление цены товара
        store.update_price("рис", 0.2)
        print("Обновленная цена риса:", store.get_price("рис"))

        # Удаление товара
        store.remove_item("сахар")
        print(store)
    