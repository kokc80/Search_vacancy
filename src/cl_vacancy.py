#  Классы
from typing import Dict, List, Optional

class Vacancy:
    """ класс представляет одну вакансию аттрибуты класса - части вакансии из разметки"""
    __slots__ = ['idd', 'name', 'url', 'company', 'title', 'employment_form', 'salary_cur', 'salary_from', 'salary_to',
                 'required_skills', 'location', 'description']
    idd: int
    name: str
    url: str
    company: str
    title: str
    employment_form: str
    sal_cur: str
    sal_from: float
    sal_to: float
    required_skills: str
    location: str
    description: str

    def __init__(self, idd, name, url, company, title, employment_form, salary_currency, salary_from, salary_to,
                 required_skills, location, description):
        self.idd = idd
        self.name = name
        self.url = url
        self.company = company
        self.title = title
        self.employment_form = employment_form
        self.salary_from = salary_from
        self.salary_cur = salary_currency
        self.salary_to = salary_to
        self.required_skills = required_skills
        self.location = location
        self.description = description

