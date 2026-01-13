import json
import os

from pprint import pprint
from src.cl_parser import HeadHunterAPI
from src.cl_storage import JsonVacancyStorage
from src.functions import (filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies, read_json,
                           sort_vacancies, vacancy_class_load)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def user_interaction() -> None:
    # Функция для взаимодействия с пользователем
    platforms = HeadHunterAPI()
    # search_query = input("Введите поисковый запрос: ") # Python
    search_query = "Python"
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split() # currency = "RUR", area = "131"
    filter_words = ("разработка", "SQL")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    top_n = 5
    # salary_range = input("Введите диапазон зарплат: ") # 10000 - 200000
    salary_range = "80000 - 500000"
    vacancies_list = platforms.load_vacancies(search_query)
    with open(ROOT_DIR + '\\data\\vacations.json', 'w', encoding='utf-8') as f:
        json.dump(vacancies_list, f, indent=4, sort_keys=True, ensure_ascii=False)
    vacancies_list = read_json(ROOT_DIR + '\\data\\vacations.json')
    vac_item = vacancy_class_load(vacancies_list)
    filtered_vacancies = filter_vacancies(vac_item, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print("ТОП:", top_n, "ВАКАНСИЙ Количество отфильтрованных вакансий по словам "
          f"{filter_words} - {len(ranged_vacancies)} шт. с ЗП ({salary_range})")
    print_vacancies(top_vacancies)

    storage = JsonVacancyStorage(ROOT_DIR+"\\data\\vacancies.json")
    storage.add_vacancy(top_vacancies)  # добавить из класса вакансий

if __name__ == "__main__":
    user_interaction()
