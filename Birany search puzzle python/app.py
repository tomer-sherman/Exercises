from typing import TypedDict
import math 

class Product(TypedDict):
    id: int
    name: str
    price: float

    


# Already sorted by price, ascending
products: list[Product] = [
    {"id": 1, "name": "Espresso Cup", "price": 4.5},
    {"id": 2, "name": "Paper Filters", "price": 6.0},
    {"id": 3, "name": "Milk Frother Wand", "price": 9.9},
    {"id": 4, "name": "Coffee Scoop", "price": 12.0},
    {"id": 5, "name": "Ceramic Mug", "price": 14.5},
    {"id": 6, "name": "Reusable Cup", "price": 18.0},
    {"id": 7, "name": "Glass Carafe", "price": 18.0},
    {"id": 8, "name": "Pour-Over Dripper", "price": 22.0},
    {"id": 9, "name": "Bean Storage Jar", "price": 25.0},
    {"id": 10, "name": "Digital Scale", "price": 34.9},
    {"id": 11, "name": "Moka Pot", "price": 39.0},
    {"id": 12, "name": "French Press", "price": 45.0},
    {"id": 13, "name": "Gooseneck Kettle", "price": 59.0},
    {"id": 14, "name": "Cold Brew Maker", "price": 64.0},
    {"id": 15, "name": "Manual Grinder", "price": 79.0},
    {"id": 16, "name": "Travel Press", "price": 89.0},
    {"id": 17, "name": "Burr Grinder", "price": 129.0},
    {"id": 18, "name": "Drip Machine", "price": 189.0},
    {"id": 19, "name": "Espresso Machine", "price": 449.0},
    {"id": 20, "name": "Pro Espresso Machine", "price": 999.0},
]


def find_by_price(items: list[Product], target: float):

    high = len(items) -1
    low = 0


    while high >= low:


        
        middle = math.floor((high+low)/2)
        value = items[middle]["price"]


        if value == target:
            return items[middle]

        if value > target:
           high = middle -1
        else:
           low = middle + 1

            
            

       
        
       

    return None

product = find_by_price(products, 22.0)
print(product)


    


      
      



