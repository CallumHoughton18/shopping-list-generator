

from dataclasses import dataclass
from typing import Counter, List, Tuple
from shopping_list_generator.recipe import Recipe


@dataclass
class ShoppingList:
    _recipes: List[Tuple[Recipe, int]]

    def __init__(self):
        self._recipes = []

    def add_recipe(self, recipe: Recipe, quantity: int):
        self._recipes.append((recipe, quantity))

    def get_shopping_list_text(self) -> str:
        combined_ingredients = Counter()

        for (recipe, quantity) in self._recipes:
            recipe_counter = recipe.get_ingredients()

            multipled_recipe = Counter({ingredient: recipe_counter[ingredient] * quantity
                                       for ingredient in recipe_counter})

            combined_ingredients += multipled_recipe

        return "\n".join([f'{count} {name}' for (name, count) in combined_ingredients.items()])
