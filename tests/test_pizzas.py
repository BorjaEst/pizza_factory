"""Pytest module to test sources as blackbox."""
import yaml
from pizza_factory import Factory
from pizza_factory import Pizza
from pytest import fixture


@fixture(scope="module")
def factory(recipes):
    return Factory(location="Valencia", recipes=recipes)


@fixture(scope="module")
def recipes():
    with open("tests/recipes.yaml", "r") as stream:
        return yaml.safe_load(stream)


class IsPizza:  # Common tests between all pizzas
    def test_has_tomato(self, pizza):
        assert "tomato" in pizza.toppings

    def test_has_cheese(self, pizza):
        assert "cheese" in pizza.toppings


class TestMargarita(IsPizza):
    @fixture(scope="class")
    def pizza(self, factory):
        return factory.make(Pizza, name="Margarita")

    def test_only_2_toppings(self, pizza):
        assert len(pizza.toppings) == 2


class TestVegetarian(IsPizza):
    @fixture(scope="class")
    def pizza(self, factory):
        return factory.make(Pizza, name="Vegetarian")

    def test_has_no_meet(self, pizza):
        assert "pepperoni" not in pizza.toppings


class TestPeperoni(IsPizza):
    @fixture(scope="class")
    def pizza(self, factory):
        return factory.make(Pizza, name="Pepperoni")

    def test_has_pepperoni(self, pizza):
        assert "pepperoni" in pizza.toppings
