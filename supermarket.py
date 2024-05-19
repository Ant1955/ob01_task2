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
magnit = Store("Магнит", "Фрунзе 12")
carusel = Store("Карусель", "Гагарина 5")
perekrestok = Store("Перекресток", "маяковского 8")
chijik = Store("Чижик", "Гарнаева 17")

# Добавление товаров
magnit.add_item("Яблоки", 0.45)
magnit.add_item("Бананы", 0.55)
magnit.add_item("Хлеб", 0.60)
magnit.add_item("Молоко", 0.78)

carusel.add_item("Яблоки", 0.55)
carusel.add_item("Бананы", 0.75)
carusel.add_item("Хлеб", 1.0)
carusel.add_item("Молоко", 0.9)

perekrestok.add_item("Яблоки", 0.73)
perekrestok.add_item("Бананы", 0.95)
perekrestok.add_item("Хлеб", 1.1)
perekrestok.add_item("Молоко", 1.9)

chijik.add_item("Яблоки", 0.35)
chijik.add_item("Бананы", 0.42)
chijik.add_item("Хлеб", 0.13)
chijik.add_item("Молоко", 0.56)

# Тестирование методов на примере магазина "Магнит"
magnit.update_price("Яблоки", 0.55)
print(magnit.get_price("Яблоки"))
magnit.remove_item("Бананы")
print(magnit.get_price("Бананы"))