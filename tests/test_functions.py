import os, json
from src.functions import read_json, filter_vacancies, vacancy_class_load
from src.cl_vacancy import Vacancy
import unittest
from unittest.mock import mock_open, patch

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path_data = f"{ROOT_DIR}\\data\\test.json"

# 1. Задаём тестовые данные
trans_test_value = [
    {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {"amount": "92688.46", "currency": {"name": "USD", "code": "USD"}},
        "description": "Открытие вклада",
        "to": "Счет 35737585785074382265"
    },
    {
        "id": 957763565,
        "state": "EXECUTED",
        "date": "2019-01-05T00:52:30.108534",
        "operationAmount": {"amount": "87941.37", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 46363668439560358409",
        "to": "Счет 18889008294666828266"
    },
    {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    }
]


class TestReadJson(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps(trans_test_value))
    def test_read_json(self, mock_file):
        # Вызываем реальную функцию, но с мокированным open
        result = read_json(file_path_data)
        # Проверяем, что результат совпадает с тестовыми данными
        self.assertEqual(result, trans_test_value)
        # Дополнительно: проверяем, что open был вызван с нужным путём
        mock_file.assert_called_with(file_path_data, 'r', encoding='utf-8')


VAC1 = Vacancy(1, "Name 1", "url1", "Company1", "title1", "EForm1",
               "RUR", 100, 200,
               {'requirement': "Програм-е1", 'test': "test"}, "Локация1", "Описание1")
VAC2 = Vacancy(2, "Name 1", "url1", "Company1", "title1", "EForm1",
               "RUR", 100, 200,
               {'requirement': "Програм-е2", 'test': "test"}, "Локация1", "Описание1")
VAC3 = Vacancy(3, "Name 1", "url1", "Company1", "title1", "EForm1",
               "RUR", 100, 200,
               {'requirement': "Програм-е3", 'test': "test"}, "Локация1", "Описание1")
vacancies = [VAC1, VAC2, VAC3]



def test_filter_vacancies():
    filtered_vac = filter_vacancies(vacancies, ("Програм-е3", "Програм-е2"))
    assert len(filtered_vac) == 2


if __name__ == "__main__":
    unittest.main()

# def test_vacancy_class_load():
#     load_vacancy = vacancy_class_load(vacancies)
#     assert load_vacancy[0].idd == 1
#     assert load_vacancy[1].idd == 2
#     assert load_vacancy[2].idd == 3