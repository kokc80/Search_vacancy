# Классы
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
    """
    Класс для получения вакансий с API HeadHunter
    """
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
            # print ("connect 200")
            return response
        else:
            return 'Ошибка при обращении к API - error'

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

if __name__ == "__main__":
      hh_api = HeadHunterAPI()
      hh_api.connect_to_api()
      api_vacans = hh_api.load_vacancies("Python")
      print(api_vacans)