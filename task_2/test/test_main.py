import pytest

from task_2.main import YADisk
from task_2.config import TOKEN


@pytest.mark.parametrize('folder_name, excepted, text', [
    ('Netology', 201, 'Успешно'),
    ('Netology', 409, 'Папка уже существует'),
    ('', 400, 'Пустое имя папки'),
])
def test_create_new_folder(folder_name, excepted, text):
    assert YADisk(TOKEN).create_new_folder(folder_name) == excepted
    print(text)
