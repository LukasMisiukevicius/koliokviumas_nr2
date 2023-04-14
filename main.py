from shop.shop_items import Food
from shop.shop_items import Drink
from shop.shop_items import Item

from shop.shop_customers import Customer

my_food = Food()
my_drink = Drink()
my_item = Item()
my_customer = Customer("Lukas")
print(my_customer._identifier)