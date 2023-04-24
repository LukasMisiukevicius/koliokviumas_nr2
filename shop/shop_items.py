class Item:
    def __init__(self, name, quantity=1, price=10):
            self._name = name
            self._quantity = quantity
            self._price = price


    # privati funkcija, skirta gauti pilną kainą
    def _get_total_price(self):
        try:
            return self._quantity * self._price
        except:
            print("Error returning total price")
            exit(1)

    # funkcija, skirta išvesti pilną informaciją
    def full_info(self):
        return f"{self._name} {self._quantity} {self._price} {self._get_total_price()}"

    # funkcija, skirta sudėti informaciją į dictionary
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
