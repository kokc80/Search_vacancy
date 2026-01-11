import json
import os
import logging


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
    i = 0
    while i < len(vacancies):
        vac_item = vacancies[i]
        print(vac_item.idd, vac_item.name, vac_item.url, vac_item.requiredskills, vac_item.company, vac_item.title,
              vac_item.employment_form, vac_item.salary_to, vac_item.description, vac_item.location)
        i += 1


def vacancy_class_load(vacancies_list: list) -> list[Vacancy]:
    """Заполнение списка класса вакансий"""
    vacancy_class_list = []
    idd = 0
    for vacancy_item in vacancies_list:
        vacancy_class = Vacancy()
        idd = idd + 1
        vacancy_class.idd = idd
        vacancy_class.name = vacancy_item["name"]
        vacancy_class.url = vacancy_item["alternate_url"]
        vacancy_class.company = vacancy_item["employer"]["name"]
        vacancy_class.title = vacancy_item["name"]
        vacancy_class.employment_form = (vacancy_item["employment_form"]["id"]
                                         + " - " + vacancy_item["employment_form"]["name"])
        vacancy_class.salary_currency = vacancy_item.get("salary", {}.get("currency", "None"))
        vacancy_class.salary_to = vacancy_item.get("salary", {}.get("to", "None"))
        vacancy_class.requiredskills = vacancy_item.get("snippet", {}.get("requirement", "None"))
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
            if vacancies_list[j].requiredskills.get("requirement") is None:
                reqSkils = "None"
            else:
                reqSkils = vacancies_list[j].requiredskills.get("requirement")
            if (filter_word in reqSkils and reqSkils != "None"):
                filtered_list.append(vacancies_list[j])
            j = j + 1
        i += 1
    return filtered_list


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Функция фильтрации вакансий по зарплате"""
    vacancies_by_salary: list = []
    salary = salary_range.split(sep=" - ", maxsplit=2)  # Пример: 10000 - 150000
    for dict_item in filtered_vacancies:
        if dict_item.get("salary") in range(int(salary[0]), int(salary[1])):
            vacancies_by_salary.append(dict_item)
    return vacancies_by_salary


def sort_vacancies(ranged_vacancies):
    pass
    # def sort_by_date(data_list: List, reverse1: bool = True) -> List:
    #     """Функия принимает список словарей и необязательный параметр,
    #     задающий порядок сортировки (по умолчанию — убывание). Функция
    #     должна возвращать новый список, отсортированный по дате (date)"""
    #     list_sorted: List = sorted(data_list, key=lambda x: x.get("date"), reverse=reverse1)
    #     return list_sorted


def get_top_vacancies(sorted_vacancies, top_n):
    pass
