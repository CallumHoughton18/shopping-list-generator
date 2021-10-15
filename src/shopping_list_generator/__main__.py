import argparse
import os
import sys
from typing import List

from shopping_list_generator.recipelocator import RecipeParsingError, read_and_parse_recipe
from shopping_list_generator.shoppinglist import ShoppingList
from shopping_list_generator.parsingutils import parse_recipe_name_and_quantity


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("recipes", help="""relative path of the recipe files, with optional quantity.
    \nExample usage:
    shopping-list-generator \"recipe_folder/daal, recipe_folder/spaghetti-2\"""")
    args = parser.parse_args(argv[1:])

    # Strip white space and append .txt to filename string if it does not end with .txt
    # and parses quantity if it's specified, if not it defaults to 1
    recipe_file_names_with_quantity = [parse_recipe_name_and_quantity(x, separator='-')
                                       for x in args.recipes.split(',')]
    shopping_list = ShoppingList()
    for (recipe_file_name, quantity) in recipe_file_names_with_quantity:
        try:
            recipe = read_and_parse_recipe(recipe_file_name)
            shopping_list.add_recipe(recipe, quantity)
        except IOError as err:
            print(f"Could not read the recipe file {recipe_file_name}: {err}")
            return 1
        except RecipeParsingError as err:
            print(f"Could not parse recipe {recipe_file_name}: {err}")
            return 1

    shopping_list_text = shopping_list.get_shopping_list_text()

    cwd = os.getcwd()
    shopping_list_path = os.path.join(cwd, "shoppinglist.txt")

    try:
        with open(shopping_list_path, 'w') as filetowrite:
            filetowrite.write(shopping_list_text)
    except IOError as err:
        print(f"Could not write to file {shopping_list_path}: {err}")
        return 1

    return 0


def cli_entrypoint():
    sys.exit(main(sys.argv))


if __name__ == "__main__":
    cli_entrypoint()
