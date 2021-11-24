__all__ = ["Factory", "Machine", "Pizza"]


class Factory:
    def __init__(self, location, recipes) -> None:
        self.location = location
        self.recipes = recipes
        self.machine = Machine()

    def make(self, order, name):
        toppings = self.recipes["pizza"][name]
        return order(name, toppings)


class Machine:
    def cook(self):
        pass


class Pizza:
    def __init__(self, name, toppings) -> None:
        self.name = name
        self.toppings = toppings
