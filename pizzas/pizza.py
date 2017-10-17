def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizzas with the following toppings")
    for topping in toppings:
        print("-" + topping)
