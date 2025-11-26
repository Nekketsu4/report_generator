import model


def test_to_dict_employee():
    """
    Тест извлечения данных из csv в формате словаря
    и присваивая классу Employee
    """

    data = {
        'name': 'Olga Kuznetsova',
        'position': 'Frontend Developer',
        'completed_tasks': 42,
        'performance': 4.6,
        'skills': ['Vue.js', 'JavaScript', 'Webpack', 'Sass'],
        'team': 'Web Team',
        'experience_years': 3
    }

    employee = model.Employee(**data)

    assert employee.name == 'Olga Kuznetsova'
    assert employee.position == 'Frontend Developer'
    assert employee.completed_tasks == 42
    assert employee.performance == 4.6
    assert employee.skills == ['Vue.js', 'JavaScript', 'Webpack', 'Sass']
    assert employee.team == 'Web Team'
    assert employee.experience_years == 3