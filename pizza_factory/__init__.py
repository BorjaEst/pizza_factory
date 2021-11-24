__all__ = ["Factory", "Pizza"]


class Factory:
    def __init__(self, location, recipes) -> None:
        self.location = location
        self.recipes = recipes

    def make(self, order, name):
        toppings = self.recipes["pizza"][name]
        return order(name, toppings)


class Pizza:
    def __init__(self, name, toppings) -> None:
        self.name = name
        self.toppings = toppings
