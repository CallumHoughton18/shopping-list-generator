
import os
from typing import Tuple
from shopping_list_generator.recipe import Recipe
from pathlib import Path


class RecipeParsingError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def read_and_parse_recipe(relative_recipe_path: str) -> Recipe:
    cwd = os.getcwd()
    recipe_path = os.path.join(cwd, relative_recipe_path)
    new_recipe_name = Path(recipe_path).stem
    new_recipe = Recipe(new_recipe_name)

    for line in open(recipe_path):
        if not line.strip():
            continue
        format_err_msg = f"""Formatting error in {recipe_path} on line '{line}'.
        Ingredient must be in style '1 tomato'.
        With each ingredient on a new line"""

        (ingredient_amount, ingredient_name) = parse_recipe_text_line(line, format_err_msg)
        new_recipe.add_ingredient(ingredient_name, ingredient_amount)

    return new_recipe


def parse_recipe_text_line(line: str, error_msg: str) -> Tuple[int, str]:
    formatted_line = line.strip().lower()
    line_split = formatted_line.split(sep=" ", maxsplit=1)

    if len(line_split) != 2:
        raise RecipeParsingError(error_msg)

    try:
        ingredient_num = int(line_split[0])
        ingredient_name = line_split[1].strip()
        return (ingredient_num, ingredient_name)
    except ValueError:
        raise RecipeParsingError(error_msg)
