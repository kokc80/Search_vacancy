def filter_vacancies(vacancies_list: list, filter_words: list):
    """Функция фильтрации вакансий по """
     # def filter_by_state(banking_operations: List[Dict[str, str]], state: str = "EXECUTED") -> List:
    filtered_list: list = []
    for dict_item in vacancies_list:
        if dict_item.get(filter_words) == state:
            filtered_list.append(dict_item)
    return filtered_list


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Функция фильтрации вакансий по зарплате"""
    vacancies_by_salary: list = []
    for dict_item in filtered_vacancies:
        if dict_item.get("salary") in salary_range:
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
