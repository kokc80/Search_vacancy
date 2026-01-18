import json
import os

from src.cl_parser import HeadHunterAPI
from src.cl_storage import JsonVacancyStorage
from src.functions import (filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies, read_json,
                           sort_vacancies, vacancy_class_load)
from src.cl_vacancy import Vacancy
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
#    print("VL",vacancies_list)
    with open(ROOT_DIR + '\\data\\vacantions.json', 'w', encoding='utf-8') as f:
        json.dump(vacancies_list, f, indent=4, sort_keys=True, ensure_ascii=False)

    vacancies_list = read_json(ROOT_DIR + '\\data\\vacantions.json')
    vac_item = vacancy_class_load(vacancies_list)
    filtered_vacancies = filter_vacancies(vac_item, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print("ТОП:", top_n, "ВАКАНСИЙ Количество отфильтрованных вакансий по словам "
          f"{filter_words} - {len(ranged_vacancies)} шт. с ЗП ({salary_range})")
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
    storage = JsonVacancyStorage(ROOT_DIR + '\\data\\vacantions.json')
    vacancy1 = Vacancy(idd="1000", name="Python Developer", url="http://example.com/1", salary_currency="RUR",
                       company="Company1", title="Title1", employment_form="Eform1", required_skills="RS1",
                       location="Loc1", description="Python Test description", salary_from=100000, salary_to=150000)
    storage.add_vacancy(vacancy1)  # добавить из класса вакансий
    storage.get_vacancies()
