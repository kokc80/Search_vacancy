import pytest
from src.cl_vacancy import Vacancy

@pytest.fixture
def VAC1():
    return Vacancy(33, "Data Analyst Intern / Стажер-аналитик данных", "https://hh.ru/vacancy/128081806",
                   "Компания рога и копыта", "Начинающий специалист", "Полный день",
                   "RUR", 100, "200", "Программирование", "Локация",
                   "Описание")

def test_Vacancy(VAC1):
    assert VAC1.idd == 33
    assert VAC1.name == "Data Analyst Intern / Стажер-аналитик данных"
    assert VAC1.url == "https://hh.ru/vacancy/128081806"
    assert VAC1.company == "Компания рога и копыта"