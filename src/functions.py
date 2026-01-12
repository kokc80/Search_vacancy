import json
import logging
import os

from src.cl_vacancy import Vacancy

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_logger = logging.getLogger()
file_log = f"{ROOT_DIR}\\Logs\\search_vacancy.log"
# print(file_log)
# очистка файла лога
with open(file_log, "w"):
    app_logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(file_log)
    file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    file_handler.setFormatter(file_formatter)
    app_logger.addHandler(file_handler)
    app_logger.setLevel(logging.DEBUG)
    app_logger.debug("Debug message")


def read_json(filename=None) -> list[dict]:
    """чтение файла json"""
    try:
        if os.path.isfile(filename):
            # Открываем файл и читаем строки
            with open(filename, encoding="utf-8") as f:
                json_list = json.load(f)
                if type(json_list) is list:
                    app_logger.info(" Удачный запуск")
                    return json_list
                else:
                    app_logger.error("Не удачный запуск")
                    return []
        else:
            return []
    except FileNotFoundError:
        # print("Файл не найден")
        app_logger.error("Файл не найден")
    except json.JSONDecodeError as e:
        # print(f"Сообщение об ошибке: {e.msg} Строка: {e.lineno}, колонка: {e.colno}")
        app_logger.error(f"Сообщение об ошибке: {e.msg} Строка: {e.lineno}, колонка: {e.colno}")
    except Exception as e:
        # print(e)
        app_logger.error(e)


def print_vacancies(vacancies: list):
    """Печать вакансий"""
    for vacancy in vacancies:
        print("idd:", vacancy.idd, " url:", vacancy.url, " вакансия:", vacancy.name,
              "Валюта", vacancy.salary_cur, "от", vacancy.salary_from, "до", vacancy.salary_to,
              "\nНавыки", vacancy.required_skills)


def vacancy_class_load(vacancies_list: list) -> list[Vacancy]:
    """Заполнение списка класса вакансий"""
    vacancy_class_list = []
    idd = 0
    for vacancy_item in vacancies_list:
        vacancy_class = Vacancy(0, "", "", "", "", "", "",
                                0, 0, "", "", "")
        idd = idd + 1
        vacancy_class.idd = idd
        vacancy_class.name = vacancy_item["name"]
        vacancy_class.url = vacancy_item["alternate_url"]
        vacancy_class.company = vacancy_item["employer"]["name"]
        vacancy_class.title = vacancy_item["name"]
        vacancy_class.employment_form = (vacancy_item["employment_form"]["id"]
                                         + " - " + vacancy_item["employment_form"]["name"])
        if vacancy_item["salary"] is not None:
            if vacancy_item["salary"]["currency"] is not None:
                vacancy_class.salary_cur = vacancy_item["salary"]["currency"]
            else:
                vacancy_class.salary_cur = "не определено"
            if vacancy_item["salary"]["from"] is not None:
                vacancy_class.salary_from = vacancy_item["salary"]["from"]
            else:
                vacancy_class.salary_from = 0
            if vacancy_item["salary"]["to"] is not None:
                vacancy_class.salary_to = vacancy_item["salary"]["to"]
            else:
                vacancy_class.salary_to = 0
        vacancy_class.required_skills = vacancy_item.get("snippet", {}.get("requirement", "None"))
        vacancy_class.description = vacancy_item["snippet"]["responsibility"]
        vacancy_class.location = vacancy_item.get("address", {}.get("raw", "Not Found"))
        vacancy_class_list.append(vacancy_class)
    return vacancy_class_list


def filter_vacancies(vacancies_list: list[Vacancy], filter_words: list):
    """Функция фильтрации вакансий по навыкам"""
    filtered_list: list = []
    i = 0
    while i < len(filter_words):
        j = 0
        filter_word = filter_words[i]
        while j < len(vacancies_list):
            if vacancies_list[j].required_skills.get("requirement") is None:
                reqSkils = "None"
            else:
                reqSkils = vacancies_list[j].required_skills.get("requirement")
            if (filter_word in reqSkils and reqSkils != "None"):
                filtered_list.append(vacancies_list[j])
            j = j + 1
        i += 1
    return filtered_list


def get_vacancies_by_salary(filtered_vacancies: list[Vacancy], salary_range):
    """Функция фильтрации вакансий по зарплате"""
    vacancies_by_salary: list = []
    salary = salary_range.split(sep=" - ", maxsplit=2)  # Пример: 10000 - 150000
    salary_min = salary[0]
    salary_max = salary[1]
    for dict_item in filtered_vacancies:
        if dict_item.salary_from in range(int(salary_min), int(salary_max)):
            vacancies_by_salary.append(dict_item)
    return vacancies_by_salary


def sort_vacancies(ranged_vacancies: list[Vacancy]) -> list[Vacancy]:
    """Функция сортировки для вакансий по убыванию"""
    return sorted(ranged_vacancies, key=lambda p: p.idd, reverse=True)


def get_top_vacancies(sorted_vacancies: list[Vacancy], top_n):
    return sorted_vacancies[:top_n]
