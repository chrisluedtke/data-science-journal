#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    for k in recipe.keys():
        if k not in ingredients:
            ingredients[k] = 0

        ingredients[k] -= recipe[k]
        if ingredients[k] < 0:
            return 0

    return recipe_batches(recipe, ingredients) + 1


if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))