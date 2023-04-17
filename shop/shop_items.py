class Item:
    def __init__(self, name, quantity=1, price=10):
        self._name = name
        self._quantity = quantity
        self._price = price

    def _get_total_price(self):
        return self._quantity * self._price

    def full_info(self):
        return f"{self._name} {self._quantity} {self._price} {self._get_total_price()}"

    def to_dict(self):
        return {
            "name": self._name,
            "quantity": self._quantity,
            "price": self._price,
            "total_price": self._get_total_price()
        }

class Drink(Item):
    def __init__(self, name, quantity=1, price=10):
        super().__init__(name, quantity, price)

    def full_info(self):
        return f"Gerimas {super().full_info()}"

class Food(Item):
    def __init__(self, name, quantity=1, price=10):
        super().__init__(name, quantity, price)

    def full_info(self):
        return f"Maistas {super().full_info()}"

