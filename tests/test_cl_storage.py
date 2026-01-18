import pytest
from src.cl_vacancy import Vacancy
from src.cl_storage import JsonVacancyStorage


@pytest.fixture
def vacancies_fix():
    return [
        Vacancy(idd="1", name="Python Developer", url="http://example.com/1", salary_currency="RUR",
                company="Company1", title="Title1", employment_form="Eform1", required_skills="RS1", location="Loc1",
                description="Python Test description", salary_from=100000, salary_to=150000),
        Vacancy(idd="2", name="Java Developer", url="http://example.com/2", salary_currency="RUR",
                company="Company2", title="Title2", employment_form="Eform2", required_skills="RS2", location="Loc2",
                description="Java Test description", salary_from=120000, salary_to=170000),
    ]


@pytest.fixture
def json_storage(tmp_path):
    return JsonVacancyStorage(filename="test.json")


# def test_add_vacancies(json_storage, vacancies_fix):
#     json_storage.add_vacancy(vacancies_fix)
#     saved_vacancies = json_storage.get_vacancies(vacancies_fix)
#     print("LLLLL",len(saved_vacancies))
#     assert len(saved_vacancies) == 2
#     assert saved_vacancies[0].idd == "1"
#     assert saved_vacancies[1].idd == "2"
#

# def test_get_vacancies_by_keywords(json_storage, vacancies):
#     json_storage.add_vacancy(vacancies_fix)
#     found_vacancies = json_storage.get_vacancies_by_keywords(["Python"])
#     assert len(found_vacancies) == 1
#     assert found_vacancies[0].id == "1"
#
#
# def test_delete_vacancy(json_storage, vacancies_fix):
#     json_storage.add_vacancy(vacancies)
#
#     result = json_storage.delete_vacancy("1")
#     assert result is True
#
#     remaining_vacancies = json_storage.get_vacancies()
#     assert len(remaining_vacancies) == 1
#     assert remaining_vacancies[0].id == "2"
#
#
# def test_delete_vacancy_not_found(json_storage, vacancies):
#     json_storage.add_vacancy(vacancies)
#
#     result = json_storage.delete_vacancy("3")
#     assert result is False
