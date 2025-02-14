from praktikum.bun import Bun


class TestBun:

    """ Получаем наименование булки. Успех. """
    def test_get_name_success(self):
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_name() == 'Краторная булка N-200i'

    """ Получаем стоимость булки. Успех. """
    def test_get_price_success(self):
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_price() == 1255
