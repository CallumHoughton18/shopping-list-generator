# Shopping List Generator

A simple CLI tool written in Python for generating a shopping list text file from multiple recipe files. Written so my girlfriend stops taking an extra 15 minutes every week copying the recipe contents...

## Quick Setup

The app uses [Pipenv](https://pipenv.pypa.io/en/latest/) for dependency managment. So you will need to be familiar with this to run the application locally.

The application uses your working directory to find recipe text files, and outputs a shopping_list.txt file to the working directory. The file extension of the recipe file does not need to be specified, it is assumed to be .txt.

So running the app from the src folder would look like:
`pipenv run python -m shopping_list_generator "test_recipes/daal, test_recipes/curry"`