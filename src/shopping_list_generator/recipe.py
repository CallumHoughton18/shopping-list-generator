from dataclasses import dataclass
from typing import Counter


@dataclass
class Recipe:
    recipe_name: str
    _ingredients: Counter

    def __init__(self, recipe_name: str):
        self.name = recipe_name
        self._ingredients = {}

    def add_ingredient(self, ingredient_name: str, amount: int):
        if ingredient_name in self._ingredients:
            self._ingredients[ingredient_name] += amount
        else:
            self._ingredients[ingredient_name] = amount

    def get_ingredients(self) -> Counter:
        return self._ingredients
