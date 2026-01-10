#  Классы
class Vacancy:
    """ класс представляет одну вакансию аттрибуты класса - части вакансии из разметки"""
    idd: int
    name: str
    url: str
    company: str
    title: str
    employment_form: str
    salary_currency: str
    salary_from: float
    salary_to: float
    requiredskills: str
    location: str
    description: str
