from shop.shop_items import Food
from shop.shop_items import Drink
from shop.shop_items import Item

from shop.shop_customers import Customer

def firstTask():
    my_customer = Customer("Lukas")
    my_customer2 = Customer("Jonas")
    print(Customer.identifier)
    print(my_customer2.get_identifier())
    print(my_customer.full_info())

def secondTask():
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
    f1 = Food("Batonas", 2, 1.3)
    f2 = Food("Sviestas", 1, 1.3)

    d1 = Drink("CocaCola", 3, 1.7)
    d2 = Drink("Sprite", 2, 1.7)

    print(f1.full_info())
    print(f2.full_info())
    print(d1.full_info())
    print(d2.full_info())

def fourthTask():
    pass


if __name__ == '__main__':
    while(1):
        print(f'[1] First task\n[2] Second task\n[3] Third task\n[4] Fourth task\n[5] Fifth task\n\n[0] Exit')
        userInput = int(input('Enter your choice: '))
        if userInput == 1:
            firstTask()
        elif userInput == 2:
            secondTask()
        elif userInput == 3:
            thirdTask()
        elif userInput == 4:
            fourthTask()
        # elif userInput == 5:
        #     fifthTask()
        else:
            exit(0)

