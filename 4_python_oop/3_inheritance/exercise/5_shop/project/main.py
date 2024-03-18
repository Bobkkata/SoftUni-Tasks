from project_90_100.drink import Drink
from project_90_100.food import Food
from project_90_100.product_repository import ProductRepository


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
