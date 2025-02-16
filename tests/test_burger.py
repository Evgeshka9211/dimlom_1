import praktikum.ingredient_types

from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database

class TestBurger:

    """Проверяем задание булочки. Успех."""
    def test_set_buns_success(self):
        burger = Burger()
        bun = Bun('New_bun', 1500.0)
        burger.set_buns(bun)
        assert burger.bun == bun

    """Проверяем добавление ингредиента. Успех."""
    def test_add_ingredient_success(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'New_bun'
        mock_ingredient.get_price.return_value = 150.0
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_price() == 150.0
        assert burger.ingredients[0].get_name() == 'New_bun'
        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

    """Проверяем удаление ингредиента. Успех."""
    def test_remove_ingredient_success(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    """Проверяем перемещение слоев. Успех."""
    def test_move_ingredient_success(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        first_ingredient = database.available_ingredients()[0]
        burger.add_ingredient(first_ingredient)
        second_ingredient = database.available_ingredients()[1]
        burger.add_ingredient(second_ingredient)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == second_ingredient and burger.ingredients[1] == first_ingredient

    """Проверяем получение цены. Успех."""
    def test_get_price_success(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[4])
        assert burger.get_price() == 500.0


    """Проверяем получение чека. Успех."""
    def test_get_receipt_success(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[4])
        expected_receipt = "(==== black bun ====)\n"\
                           "= sauce hot sauce =\n"\
                           "= filling dinosaur =\n"\
                           "(==== black bun ====)\n\n"\
                           "Price: 500"

        assert expected_receipt == burger.get_receipt()
