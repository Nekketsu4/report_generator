import pytest

from factory import create_factory_report
from report import EmployeeReport

def test_factory_can_create_report_instance():
    create_factory = create_factory_report('performance')
    assert isinstance(create_factory, EmployeeReport)

def test_factory_cannot_create_wrong_report_instance():
    with pytest.raises(ValueError, match='Данный отчет не найден: wrong'):
        create_factory_report('wrong')
