import json, os
from src.classes import HeadHunterAPI,Vacancy,JsonVacancyStorage
from src.functions import vacancy_class_load, get_vacancies_by_salary, sort_vacancies, get_top_vacancies
from src.functions import print_vacancies, read_json, vacancy_class_load


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def user_interaction():
    # Функция для взаимодействия с пользователем
    platforms = HeadHunterAPI()
    # search_query = input("Введите поисковый запрос: ") # Python
    search_query = "Python"
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split() # currency = "RUR", area = "131"
    filter_words = "'currency': 'RUR'"
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    top_n = 5
    # salary_range = input("Введите диапазон зарплат: ") # 10000 - 200000
    salary_range = "10000 - 200000"
    vacancies_list = platforms.load_vacancies(search_query)
    with open(ROOT_DIR+'\\data\\vacations.json', 'w', encoding='utf-8') as f:
        json.dump(vacancies_list, f, indent=4, sort_keys=True, ensure_ascii=False)
    vacancies_list = read_json(ROOT_DIR+'\\data\\vacations.json')
    # print("перед vacancy_class_load \n", vacancies_list[1],"\n",vacancies_list[5])
    vac_item = vacancy_class_load(vacancies_list)
    # print("после vacancy_class_load \n",vac_item[1].url, "\n", vac_item[5].url)
    print("ВАКАНСИИ\n")
    print_vacancies(vac_item)
    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
    storage = JsonVacancyStorage('vacancies.json')
    #storage.add_vacancy(vacancy) # добавить из класса вакансий