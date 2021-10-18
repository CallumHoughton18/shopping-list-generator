# Shopping List Generator

A simple CLI tool written in Python for generating a shopping list text file from multiple recipe files. Written so my girlfriend stops taking an extra 15 minutes every week copying the recipe contents...

## Quick Install

The application is available on PyPI and so can installed via pip using:
`pip install shopping-list-generator`

## Usage

The application uses your working directory to find recipe text files, and outputs a shopping_list.txt file to the working directory. The file extension of the recipe file does not need to be specified, it is assumed to be .txt.

So running the app from within a directory with a `test_recipes` sub-directory would look like:

`shopping_list_generator "test_recipes/daal, test_recipes/curry"`

You can also specify the quantity to multiply each recipe ingredient by like:

`shopping_list_generator "test_recipes/daal-2, test_recipes/curry-2"`

Which would multiply both the daal and curry ingredients by 2.

## Quick Setup

The app uses [pipenv](https://pipenv.pypa.io/en/latest/) for dependency management. So you will need to be familiar with this to run the application locally.

Once pipenv is installed you can install the dependencies by running:

`pipenv install`

**from within the `src` directory.**

You can then run associated commands via pipenv, like:

`pipenv run python -m shopping_list_generator "test_recipes/daal, test_recipes/curry"`

## Tests

The application uses pytest for writing and running tests.

Within the `src/tests` dirctory there are a few integration tests from the easiest point of entry of the entire application. Each test takes a given set of recipe inputs, and the output shopping_list contents can be asserted on. These integration tests mock the underlying file system operations.

You can run the tests via pytest:

`pipenv run pytest ./tests`

**from within the `src` directory.**
