#  создать класс `Store`, который можно будет использовать
#  для создания различных магазинов.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание объектов класса Store
store1 = Store("Магазин 1", "Адрес 1")
store2 = Store("Магазин 2", "Адрес 2")
store3 = Store("Магазин 3", "Адрес 3")

# Добавление товаров
store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)
store2.add_item("Хлеб", 1.0)
store3.add_item("Молоко", 0.9)

# Тестирование методов на примере store1
store1.update_price("Яблоки", 0.55)
print(store1.get_price("Яблоки"))  # Выведет обновленную цену 0.55
store1.remove_item("Бананы")
print(store1.get_price("Бананы"))  # Выведет None, так как товар был удален