from src.report import AbstractReport, EmployeeReport

def create_factory_report(report_type: str) -> AbstractReport:
    """
    Фабрика которая создает генератор отчетов исходя из входных данных
    :param report_type:
    :return: AbstractReport | ValueError
    """
    if report_type == 'performance':
        return EmployeeReport()
    else:
        raise ValueError(f'Данный отчет не найден: {report_type}')

