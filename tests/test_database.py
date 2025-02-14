from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDataBase:

    """Получение доступных булок. Успех."""
    def test_available_buns_sccess(self):
        data_bun = Database()
        available_buns = data_bun.available_buns()
        assert len(available_buns) == 3

    """Получение доступных ингредиентов. Успех."""
    def test_available_ingredients_success(self):
        data_ingredients = Database()
        available_ingredients = data_ingredients.available_ingredients()
        assert len(available_ingredients) == 6

    """Получение доступных соусов. Успех."""
    def test_available_ingredients_sauces_success(self):
        quantity_ingredients = Database()
        ingredients = quantity_ingredients.available_ingredients()
        type_sauce = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(type_sauce) == 3

    """Получение доступных начинок. Успех."""
    def test_available_ingredients_fillings_success(self):
        quantity_ingredients = Database()
        ingredients = quantity_ingredients.available_ingredients()
        type_fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(type_fillings) == 3

    """Получение стоимости ингредиентов. Успех."""
    def test_get_available_ingredients_prices(self):
        data_price = Database()
        ingredients = data_price.available_ingredients()
        price = {i.get_name(): i.get_price() for i in ingredients}
        assert price['chili sauce'] == 300