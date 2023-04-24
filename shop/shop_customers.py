import json
from shop.shop_items import Food
from shop.shop_items import Drink
from shop.shop_items import Item

# Customer klase
class Customer:
    identifier = 0 # Pradinis vartotojo identifikavimo numeris

    def __init__(self, name, items=[]):
        self._name = name
        Customer.identifier += 1
        self._id = Customer.identifier
        self._items = items

    # Funkcija, kuri eina per kiekvieną daiktą ir išveda jo full_info
    def get_items(self):
        return [item.full_info() for item in self._items]

    # Funkcija, kuri prideda daiktą prie sąrašo
    def add_item(self, item):
        self._items.append(item)

    # Funkcija, kuri pagal duota indeksa pasalina daikta is saraso
    def remove_item(self, item_index):
        try:
            self._items.remove(self._items[item_index])
        except IndexError: # jei daiktu nera / nera daikto su tokiu indeksu
            print("Error removing item")

    # Funkcija, kuri raso vartotojo ir daiktu informacija i dictionary
    def _to_dict(self):
        items = [] # sukuriamas tuscias masyvas
        for item in self._items: # eina per kiekvieną daiktą ir jį sudeda į sąrašą
            items.append(
                {
                "name": item._name,
                "quantity": item._quantity,
                "price": item._price,
                "total_price": item._get_total_price(),
                "full": item.full_info()
                }
            )
        return { # grazina varda, id ir daiktu daiktu masyva su visa daiktu informacija
            "cust_name": self._name,
            "identifier": self._id,
            "items": items
        }

    # Funkcija, skirta iskelti informacija i json faila
    def export_to_json(self, path):
        if not path.endswith(".json"): # tikrina ar nurodytas "path" yra su "".json" galune
            print("Must provide json file")
        else:
            with open(path, "w") as file:
                file.write(json.dumps(self._to_dict(), indent=4)) # kviečią funckiją to_dict ir tai ką ji gražiną įrašo į failą

    # Funkcija, skirta importuoti duomenims is ".json" failo
    @classmethod 
    def import_from_json(cls, path):
        try:
            with open(path, "r") as file:
                data = json.load(file) # nuskaito failą
        except:
            print("No such file exists or file is empty")
            exit(1)
        try:
            new_name = data["cust_name"] # gauna vartotojo vardą
            items = [] # sukuria tuscia masyva, i kuri bus rasomi nuskaityti daiktai ir ju informacija
            for item_data in data["items"]: # eina per kiekvieną daiktą
                name = item_data["name"]
                quantity = item_data["quantity"]
                price = item_data["price"]
                item_type = item_data['full'].split()[0] # [0] paima pirma 'full' elemento zodi (maistas/gerimai)
                if item_type == "Maistas": # tikrina ar tipas "Maistas"
                    item = Food(name, quantity, price)
                elif item_type == "Gerimas": # tikrina ar tipas "Gerimas"
                    item = Drink(name, quantity, price)
                items.append(item) # prideda daiktą prie list'o
            return cls(new_name, items) # grazina klienta su daiktų sąrašu
        except:
            print("Json format is not recognised by system")
            exit(1)

    # Funkcija su property dekoratoriumi, kad uzdrausti tiesiogini priejima prie kliento vardo reiksmes
    @property
    def name(self):
        return self._name

    # Funkcija, skirta gauti kliento ID numeri
    def get_identifier(self):
        return self._id

    # Funkcija, skirta gauti pilna informacija apie vartotoja (varda ir ID)
    def full_info(self):
        return f"{self._id} {self._name}"
