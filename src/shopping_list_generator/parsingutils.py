

def parse_recipe_name_and_quantity(recipe_input: str, separator='-'):
    recipes_split = recipe_input.rsplit(separator, 1)
    quantity_input = recipes_split[1] if len(recipes_split) == 2 else "1"

    return _generate_recipe_file_name_and_quantity(recipes_split[0], quantity_input)


def _generate_recipe_file_name_and_quantity(recipe_name: str, quantity_input: str):
    recipe_file_name = recipe_name.strip() + '.txt' if not recipe_name.endswith('.txt') else recipe_name.strip()
    quantity = int(quantity_input.strip())
    return recipe_file_name, quantity
