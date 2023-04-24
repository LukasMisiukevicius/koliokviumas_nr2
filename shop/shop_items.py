# Item klase
class Item:
    # Pagrindinis Item klases konstruktorius
    def __init__(self, name, quantity=1, price=10):
            self._name = name
            self._quantity = quantity
            self._price = price


    # Frivati funkcija, skirta gauti pilną kainą
    def _get_total_price(self):
        try:
            return self._quantity * self._price
        except:
            print("Error returning total price")
            exit(1)

    # Funkcija, skirta išvesti pilną informaciją apie produkta
    def full_info(self):
        return f"{self._name} {self._quantity} {self._price} {self._get_total_price()}"

    # Funkcija, skirta sudėti informaciją į dictionary
    def to_dict(self):
        return {
            "name": self._name,
            "quantity": self._quantity,
            "price": self._price,
            "total_price": self._get_total_price()
        }

# Drink klase
class Drink(Item):
    def __init__(self, name, quantity=1, price=10):
        super().__init__(name, quantity, price) # Funkcija super() paveldi Item klases konstruktoriu __init___

    # Funkcija, skirta gauti "Gerimas" + visa gerimo produkto informacija
    def full_info(self): 
        return f"Gerimas {super().full_info()}"

# Food klase
class Food(Item):
    def __init__(self, name, quantity=1, price=10):
        super().__init__(name, quantity, price) # Funkcija super() paveldi Item klases konstruktoriu __init___

    # Funkcija, skirta gauti "Maistas" + visa maisto produkto informacija
    def full_info(self):
        return f"Maistas {super().full_info()}"
