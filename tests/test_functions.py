import os
import unittest
from unittest.mock import mock_open, patch
from src.functions import read_json, filter_vacancies, vacancy_class_load
from src.cl_vacancy import Vacancy

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path_data = f"{ROOT_DIR}\\data\\vacations_test.json"


trans_test_value = [
    {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {"amount": "92688.46", "currency": {"name": "USD", "code": "USD"}},
        "description": "Открытие вклада",
        "to": "Счет 35737585785074382265",
    },
    {
        "id": 957763565,
        "state": "EXECUTED",
        "date": "2019-01-05T00:52:30.108534",
        "operationAmount": {"amount": "87941.37", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 46363668439560358409",
        "to": "Счет 18889008294666828266",
    },
    {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612",
    }
]


@patch("src.functions.read_json")
def test_read_json(mock_file):
    mock_file.return_value.json.return_value = trans_test_value
    assert read_json(mock_file) == trans_test_value


def test_read_json_err():
    result = read_json("no_file.json")
    assert result == []


class TestReadJson(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_file_not_found_error(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        result = read_json("non_existent_file.json")
        self.assertEqual(result, [])


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


def test_vacancy_class_load():
    load_vacancy = vacancy_class_load(vacancies)
    assert load_vacancy[0].idd == 1
    assert load_vacancy[1].idd == 2
    assert load_vacancy[2].idd == 3


def test_filter_vacancies():
    filtered_vac = filter_vacancies(vacancies, ("Програм-е3", "Програм-е2"))
    assert len(filtered_vac) == 2


if __name__ == "__main__":
    unittest.main()
