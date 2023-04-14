from shop.shop_items import Food
from shop.shop_items import Drink
from shop.shop_items import Item

from shop.shop_customers import Customer

my_food = Food()
my_drink = Drink()
my_item = Item()
my_customer = Customer("Lukas")
my_customer2 = Customer("Jonas")
print(Customer.identifier)
print(my_customer2.get_identifier())
print(my_customer.full_info())


