import json
from abc import ABC, abstractmethod
from typing import Dict, List
from src.cl_vacancy import Vacancy


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
        self.__filename = filename

    def add_vacancy(self, vacancy: list[Vacancy]) -> None:
        """добавление вакансии в файл json"""
        with open(self.__filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(data)
        with open(self.__filename, 'w', encoding='utf-8') as file:
            # print("VV\n",Vacancy)
            data.append(vacancy.to_dict())
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> List[Dict]:
        with open(self.__filename, 'r') as file:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data

    def delete_vacancy(self, id: int) -> bool:
        with open(self.__filename, 'r+') as file:
            data = json.load(file)
            try:
                del data[id]
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                return True
            except KeyError:
                return False
