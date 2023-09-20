import math


def cakes(recipe, available):

    counterArr = []

    for ingredient in recipe:
        try:
            if(available[ingredient]):
                counterArr.append(math.floor(available[ingredient]/recipe[ingredient]))
        except:
            counterArr.append(0)
    
    print(min(counterArr))




recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
cakes(recipe, available)