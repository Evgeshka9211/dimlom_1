# Задание 1: "Юнит-тесты" курс ЯндексПрактикум | Diplom_1
Для тестирования был выбран сервис [Stella Burgers](https://stellarburgers.nomoreparties.site/) и часть его функционала, которая помогает заказать/собрать бургер. 


### Реализованные сценарии
Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

### Структура проекта

- [practikum](praktikum) - пакет, содержащий код программы
- [tests](tests) - пакет, содержит тесты, тесты разделенные и названы по классам. 

### Установка зависимостей
```shell
pip install -r requirements.txt
```
### Запустить все тесты
```shell
pytest -v 
```
### Оценка покрытия
```shell
pytest --cov=praktikum
```
### Подробная оценка покрытия, после запуска смотреть файл [index.html](htmlcov/index.html)
```shell
pytest --cov=praktikum --cov-report=html
```
