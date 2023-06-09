from shop.shop_items import Food
from shop.shop_items import Drink
from shop.shop_items import Item

from shop.shop_customers import Customer

def firstTask():
    # Test case
    c1 = Customer("Jonas Jonaitis")
    c2 = Customer("Petras Petraitis")
    c3 = Customer("Lukas Lukauskas")
    print(Customer.identifier)
    print(c1.get_identifier())
    print(c2.get_identifier())
    print(c3.get_identifier())
    print(Customer.identifier)
    print(c1.full_info())
    print(c2.full_info())
    print(c3.full_info())

def secondTask():
    # Test case
    i1 = Item("Morkos")
    i2 = Item("Pienas", 2, 1.5)
    i3 = Item("Batonas", price=0.5)
    print(i1.full_info())
    print(i2.full_info())
    print(i3.full_info())
    print(i1.to_dict())
    print(i2.to_dict())
    print(i3.to_dict())


def thirdTask():
    # Test case
    f1 = Food("Batonas", 2, 1.3)
    f2 = Food("Sviestas", 1, 1.3)
    d1 = Drink("CocaCola", 3, 1.7)
    d2 = Drink("Sprite", 2, 1.7)
    print(f1.full_info())
    print(f2.full_info())
    print(d1.full_info())
    print(d2.full_info())

def fourthTask():
    # Test case
    c1 = Customer("Jonas Jonaitis", [Food("Batonas", 2, 1.3), Drink("CocaCola", 3, 1.7)])
    c2 = Customer("Petras Petraitis", [Food("Sviestas", 1, 1.3), Drink("Sprite", 2, 1.7)])
    print(c1.get_items())
    print(c2.get_items())
    c1.add_item(Drink("Fanta", 10, 1.7))
    print(c1.get_items())
    c2.remove_item(2)
    c2.remove_item(1)
    print(c2.get_items())

def fifthTask():
    # Test case
    # Export to json
    c1 = Customer("Jonas Jonaitis", [Food("Batonas", 2, 1.3), Drink("CocaCola", 3, 1.7)])
    c1.export_to_json("./c1.json")
    print(c1.full_info())
    print(c1.get_items())

    # Import form json
    c2 = Customer.import_from_json("./c1.json")
    print(c2.full_info())
    print(c2.get_items())

    # Main function
if __name__ == '__main__':
    while(1):
        print(f'[1] First task\n[2] Second task\n[3] Third task\n[4] Fourth task\n[5] Fifth task\n\n[0] Exit')
        try:
            userInput = int(input('Enter your choice: '))
        except:
            print("Something went wrong...")
            exit(1)

        if userInput == 1:
            firstTask()
        elif userInput == 2:
            secondTask()
        elif userInput == 3:
            thirdTask()
        elif userInput == 4:
            fourthTask()
        elif userInput == 5:
            fifthTask()
        else:
            exit(0)