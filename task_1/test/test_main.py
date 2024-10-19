import pytest

from task_1.main import list_of_numbers
from task_1.main import reverse
from task_1.main import check_email


@pytest.mark.parametrize('n, expected', [
    (1, [1]),
    (3, [1, 2, 3]),
    (10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    (0, []),
    (-3, []),
    (-10, []),
])
def test_list_of_numbers(n, expected):
    assert list_of_numbers(n) == expected


@pytest.mark.parametrize('string, expected', [
    ('Вася Пупкин', 'никпуп ясав'),
    ('ABCDEFG', 'gfedcba'),
    ('@#$%^', '^%$#@'),
    ('-1', '1-'),
    (-1, '-1 не является строкой'),
])
def test_reverse(string, expected):
    assert reverse(string) == expected


@pytest.mark.parametrize('email, expected', [
    ('ivanov@yandex.ru', True),
    ('v@y.ru', True),
    ('v@.ru', False),
    ('v@@ya.ru', False),
    ('vlad@ya..ru', False),
    ('@ya.ru', False),
])
def test_check_email(email, expected):
    assert check_email(email) == expected
