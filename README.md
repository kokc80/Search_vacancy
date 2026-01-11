# Search_vacancy
Поиск вакансий на платформе hh.ru

# Проект "Поиск вакансий"

## Описание:

программа Получает информацию о вакансиях с платформы hh.ru в России, 
сохраняет ее в файл и позволять удобно работать с ней: добавлять, фильтровать, удалять.


## Установка:
1. Клонируйте репозиторий:
git clone  https://github.com/kokc80/HW.11.1
2. Установите зависимости
poetry install

## модуль cl_parser.py
class Parser(ABC): Класс Parser является абстрактным родительским классом
class HeadHunterAPI(Parser): Класс для получения вакансий с API HeadHunter

## модуль cl_vacancy.py
class Vacancy - класс представляет одну вакансию аттрибуты класса - части вакансии из разметки

## модуль cl_storage.py
class VacancyStorage(ABC): класс для работы с вакансиями
class JsonVacancyStorage(VacancyStorage): класс для работы с json

## модуль functions.py
def filter_vacancies(vacancies_list: list, filter_words: list): фильтр вакансий
def get_vacancies_by_salary(filtered_vacancies, salary_range): вакансии по зарплате1
def sort_vacancies(ranged_vacancies): сортировка вакансий
def get_top_vacancies(sorted_vacancies, top_n):  топ вакансий
def print_vacancies(top_vacancies): печать вакансий
