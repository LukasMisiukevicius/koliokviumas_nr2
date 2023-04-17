import json
from shop.shop_items import Food
from shop.shop_items import Drink
from shop.shop_items import Item

class Customer:
    identifier = 0

    def __init__(self, name, items=[]):
        self._name = name
        Customer.identifier += 1
        self._id = Customer.identifier
        self._items = items

    def get_items(self):
        return [item.full_info() for item in self._items]

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item_index):
        try:
            self._items.remove(self._items[item_index])
        except IndexError:
            print("Error removing item")

    def _to_dict(self):
        items = []
        for item in self._items:
            items.append({
                "name": item._name,
                "quantity": item._quantity,
                "price": item._price,
                "total_price": item._get_total_price(),
                "full": item.full_info()
            })
        return {
            "name": self._name,
            "identifier": self._id,
            "items": items
        }

    def export_to_json(self, path):
        if not path.endswith(".json"):
            print("Must provide json file")
        else:
            with open(path, "w") as file:
                file.write(json.dumps(self._to_dict(), indent=4))

    @classmethod
    def import_from_json(cls, path):
        try:
            with open(path, "r") as file:
                data = json.load(file)
            new_name = data["name"]
            items = []
            for item_data in data["items"]:
                name = item_data["name"]
                quantity = item_data["quantity"]
                price = item_data["price"]
                total_price = item_data["total_price"]
                if "full" in item_data:
                    item_type = item_data['full'].split()[0]
                    if item_type == "Maistas":
                        item = Food(name, quantity, price)
                    elif item_type == "Gerimas":
                        item = Drink(name, quantity, price)
                else:
                    item = Item(name, quantity, price)
                items.append(item)
            return cls(name, items)

        except:
            print("Something went wrong(probably no file exists, need to check")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def get_identifier(self):
        return self._id

    def full_info(self):
        return f"{self._id} {self._name}"

# Klasės konstruktorius priima vieną parametrą name ir priskiria ją privačiai _name savybei. Ši savybė yra
# pasiekiamas tik iš klasės vidaus.
#
# Tada yra du dekoratoriai, kurie naudojami, kad būtų galima gauti ir nustatyti kliento pavadinimą.
#
# @property dekoratorius naudojamas su name funkcija, kad būtų galima gauti kliento pavadinimą. Tai reiškia,
# kad jūs galite pasiekti pavadinimą kaip customer.name, o ne customer.name(), kai customer yra Customer klasės
# objektas.
#
# @name.setter dekoratorius naudojamas su name funkcija, kad būtų galima nustatyti kliento pavadinimą. Tai reiškia,
# kad jūs galite priskirti naują pavadinimą kaip customer.name = "Naujas pavadinimas", o ne customer.name("Naujas
# pavadinimas").
#
# Naudojant šias funkcijas, galite užtikrinti, kad tiesioginis kliento pavadinimo priėjimas yra uždraustas,
# o kliento pavadinimas yra nustatomas ir gautas naudojant name funkcijas, kurios naudoja property dekoratorių.
#
