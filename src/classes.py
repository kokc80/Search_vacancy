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
            # print("VAC\n", vacancies_items)
            self.vacancies.extend(vacancies_items)
            self.params['page'] += 1
            return vacancies_items


class Vacancy:
    """ класс представляет одну вакансию аттрибуты класса - части вакансии из разметки"""
    idd: int
    url: str
    company: str
    title: str
    employment_form: str
    salary_currency: str
    salary_from: float
    salary_to: float
    requiredSkills: str
    location: str
    description: str

from abc import ABC, abstractmethod
import json
from typing import List, Dict

class VacancyStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Dict) -> None:
        """Добавить вакансию в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Dict = None) -> List[Dict]:
        """Получить вакансии по критериям"""
        pass

    @abstractmethod
    def delete_vacancy(self, id: int) -> bool:
        """Удалить вакансию по ID"""
        pass

class JsonVacancyStorage(VacancyStorage):
    """Класс для записи в json"""
    def __init__(self, filename: str):
        self.filename = filename

    def add_vacancy(self, vacancy: Dict) -> None:
        """добавление вакансии в файл json"""
        with open(self.filename, 'w') as file:
            data = json.load(file)
            data.append(vacancy)
            json.dump(data, file, ensure_ascii=False, indent=4)


    def get_vacancies(self, criteria: Dict = None) -> List[Dict]:
        with open(self.filename, 'r') as file:
            data = json.load(file)
            if criteria:
                return [v for v in data if all(k in v and v[k] == criteria[k] for k in criteria)]
            return data

    def delete_vacancy(self, id: int) -> bool:
        with open(self.filename, 'r+') as file:
            data = json.load(file)
            try:
                del data[id]
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                return True
            except KeyError:
                return False


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    hh_api.connect_to_api()
    api_vacantions = hh_api.load_vacancies("Python")
    print("REZ VACANTIONS", api_vacantions)
