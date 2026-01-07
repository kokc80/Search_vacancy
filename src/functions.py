import json, os, logging
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


def filter_vacancies(vacancies_list: list, filter_words: list):
    """Функция фильтрации вакансий по"""
    filtered_list: list = []
    i = 0
    while i < len(filter_words):
        for dict_item in vacancies_list:
            # print(filter_words, dict_item)
            if filter_words[i] ==  dict_item:
                filtered_list.extend(dict_item)
        i += 1
    return filtered_list


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Функция фильтрации вакансий по зарплате"""
    vacancies_by_salary: list = []
    salary = salary_range.split(sep=" - ", maxsplit=2)  # Пример: 10000 - 150000
    for dict_item in filtered_vacancies:
        if dict_item.get("salary") in range(int(salary[0]),int(salary[1])):
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


def print_vacancies(top_vacancies):
    pass
