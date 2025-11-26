import tempfile

import pytest

from report import EmployeeReport, ReadFileError

csv_file1 = """name,position,completed_tasks,performance,skills,team,experience_years
David Chen,Mobile Developer,36,4.6,"Swift, Kotlin, React Native, iOS",Mobile Team,3
Elena Popova,Backend Developer,43,4.8,"Java, Spring Boot, MySQL, Redis",API Team,4"""

csv_file2 = """name,position,completed_tasks,performance,skills,team,experience_years
Alex Ivanov,Backend Developer,45,4.8,"Python, Django, PostgreSQL, Docker",API Team,5
Maria Petrova,Frontend Developer,38,4.7,"React, TypeScript, Redux, CSS",Web Team,4
John Smith,Data Scientist,29,4.6,"Python, ML, SQL, Pandas",AI Team,3
Anna Lee,DevOps Engineer,52,4.9,"AWS, Kubernetes, Terraform, Ansible",Infrastructure Team,6
Mike Brown,QA Engineer,41,4.5,"Selenium, Jest, Cypress, Postman",Testing Team,4
Sarah Johnson,Fullstack Developer,47,4.7,"JavaScript, Node.js, React, MongoDB",Web Team,5"""

cant_be_read = """name,position,completed_tasks,performance,skills,team,experience_years
Alex Ivanov,Backend Developer,45,4.8,"Python, Django, PostgreSQL, Docker",API Team,5
Maria Petrova,Frontend Developer,38,4.7,"React, Redux, CSS",Web Team,4"""


def test_can_load_data():
    report = EmployeeReport()

    report.load(['employees1.csv', ])
    created_report = report.create_report()

    assert len(report.employees) == 2
    assert len(report.create_report()) == 2

    assert created_report[0]['position'] == 'Backend Developer'
    assert created_report[0]['avg_performance'] == 4.8
    assert created_report[1]['position'] == 'Mobile Developer'
    assert created_report[1]['avg_performance'] == 4.6


def test_can_load_list_data():
    report = EmployeeReport()

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as file:
        file.write(csv_file1)
        csv1 = file.name

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as file:
        file.write(csv_file2)
        csv2 = file.name

    report.load([csv1, csv2])
    created_report = report.create_report()

    assert len(report.employees) == 8
    assert len(report.create_report()) == 7
    assert created_report[1]['position'] == 'Backend Developer'
    assert created_report[1]['avg_performance'] == 4.8

def test_return_empty_list():
    report = EmployeeReport()

    report.load([])

    assert len(report.employees) == 0
    assert len(report.create_report()) == 0

def test_error_not_found_file():
    report = EmployeeReport()

    with pytest.raises(FileNotFoundError, match='Файл не найден: not_found.csv'):
        report.load(['not_found.csv'])
