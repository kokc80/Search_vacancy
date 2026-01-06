#  Классы
import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Класс Parser является абстрактным родительским классом
    """
    @abstractmethod
    def load_vacancies(self, keyword):
        pass

    @abstractmethod
    def connect_to_api(self):
        pass


class HeadHunterAPI(Parser):
    """Класс для получения вакансий с API HeadHunter"""
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def connect_to_api(self):
        """Метод подключения к API"""
        # print ("connect")
        response = requests.get(self.url, headers=self.headers, params=self.params)
        status = response.status_code
        if status == 200:
            print("connect 200")
            return response
        else:
            return 'Ошибка при обращении к API - error'

    def load_vacancies(self, keyword):
        """Получение списка вакансий"""
        self.params['text'] = keyword
        while self.params.get('page') != 2:
            print("PAGE", self.params.get('page'))
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies_items = response.json()['items']
            print("VAC\n", vacancies_items)
            self.vacancies.extend(vacancies_items)
            self.params['page'] += 1
            return vacancies_items

# класс представляет одну вакансию
# аттрибуты класса - части вакансии из разметки
class Vacancy:
    url: str
    company: str
    companyAbout: str
    title: str
    salary: str
    requiredSkills: str
    locationAndTypeOfEmployment: str
    description: str

    
if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    hh_api.connect_to_api()
    api_vacantions = hh_api.load_vacancies("Python")
    print("REZ VACANTIONS", api_vacantions)
