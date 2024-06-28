import random
import pytest

from unit_tests.hw_4 import Utilities


@pytest.fixture
def get_list():
    # функция возвращает список из 10ти случайных чисел в диапазоне от 30 до 90
    return [random.randint(30, 90) for item in range(10)]


# тест должен быть выполнен третим по очередности
# должен получать сгенерированный список из фикстуры
# должен проверить с помощью оператора assert действительно ли самое большое число полученное
# из метода find_largest_number класса Utilities находится в диапозоне от 30 до 90
@pytest.mark.order(3)
def test_largest_between_thirty_and_ninty(get_list):
    number_list = get_list
    result = Utilities.find_largest_number(number_list)
    assert 30 <= result <= 90



# тест должен быть выполнен четвертым по очередности
# должен получать сгенрированный список из фикстуры
# должен проверить с помощью оператора assert действительно ли самое большое число полученное
# из метода find_largest_number класса Utilities состоит из двух цифр
@pytest.mark.order(4)
def test_largest_consists_of_two_digits(get_list):
    list = get_list
    result = Utilities.find_largest_number(list)
    assert 30 <= result <= 90


# тест должен быть выполнен вторым по очередности
# должен получать сгенрированный список из фикстуры
# должен проверить с помощью оператора assert действительно ли самое большое число полученное
# из метода find_largest_number класса Utilities является целым числом
# подсказка функция type() или isinstance()
@pytest.mark.order(2)
def test_largest_is_integer(get_list):
    list = get_list
    result = Utilities.find_largest_number(list)
    assert 30 <= result <= 90
    assert type(result) == int


# тест должен быть выполнен первым по очередности
# должен проверить с помощью оператора assert действительно ли самое большое число полученное
# из метода find_largest_number класса Utilities,
# которому необходимо в качестве аргумента передать пустой список [],
# не является целым числом
@pytest.mark.order(1)
def test_largest_is_not_integer_with_empty_list():
    result = Utilities.find_largest_number([])
    assert type(result) != int
