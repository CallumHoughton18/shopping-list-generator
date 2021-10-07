

from dataclasses import dataclass
from typing import Counter, List
from shopping_list_generator.recipe import Recipe


@dataclass
class ShoppingList:
    _recipes: List[Recipe]

    def __init__(self):
        self._recipes = []

    def add_recipe(self, recipe: Recipe):
        self._recipes.append(recipe)

    def get_shopping_list_text(self) -> str:
        combined_ingredients = Counter()
        for recipe in self._recipes:
            combined_ingredients += recipe.get_ingredients()

        return "\n".join([f'{count} {name}' for (name, count) in combined_ingredients.items()])
