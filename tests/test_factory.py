import pytest

from src.factory import create_factory_report
from src.report import EmployeeReport

def test_factory_can_create_report_instance():
    """
    Тест что переданные данные возвращают нужный класс для создания генератора отчетов
    """
    create_factory = create_factory_report('performance')
    assert isinstance(create_factory, EmployeeReport)

def test_factory_cannot_create_wrong_report_instance():
    """
    Тест вызывающий исключение если во входные данные передан аргумент, который
    не находит ни один из классов генераторов отчета в фабрике
    """
    with pytest.raises(ValueError, match='Данный отчет не найден: wrong'):
        create_factory_report('wrong')
