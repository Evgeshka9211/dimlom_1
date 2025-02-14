import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *

class TestIngredient:

    """Получение стоимости ингредиента. Успех."""
    def test_get_price_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_price() == 88

    """Получение наименования ингредиента. Успех."""
    def test_get_name_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_name() == 'Соус с шипами Антарианского плоскоходца'

    """Получение типа ингредиента. Успех."""
    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000, 'FILLING']
        ]
    )
    def test_get_type_correct_type(self, type, name, price, expected_ingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient
