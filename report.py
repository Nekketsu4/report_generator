import csv
from abc import ABC
from typing import List, TypeVar, Dict, Any

import model

T = TypeVar("T")

class AbstractReport(ABC):
    def load(self, file_paths: List[T]) -> None:
        """
        Загружаем файлы списком для дальнейшей обработки
        """
        raise NotImplementedError

    def create_report(self) -> List[Dict[str, Any]]:
        """
        Формируем отчет из входнных данных
        """
        raise NotImplementedError


class EmployeeReport(AbstractReport):
    def __init__(self):
        self.employees: List[model.Employee] = []

    def load(self, file_paths: List[T]) -> None:
        for path in file_paths:
            try:
                with open(path, encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        employee = model.Employee(**row)
                        self.employees.append(employee)
            except FileNotFoundError:
                raise FileNotFoundError(f"Файл не найден: {path}")
            except Exception as e:
                raise Exception(f"Невозможно прочитать файл: {path}")

    def create_report(self) -> List[Dict[str, Any]]:
        if not self.employees:
            return []

        position_dict = {}

        for employee in self.employees:
            if employee.position not in position_dict:
                position_dict[employee.position] = {
                    'performance_sum': 0,
                    'count': 0
                }

            position_dict[employee.position]['count'] += 1
            position_dict[employee.position]['performance_sum'] += float(employee.performance)

        report = []
        for position, value in position_dict.items():
            avg_performance = value['performance_sum'] / value['count']
            report.append({
                'position': position,
                'avg_performance': round(avg_performance, 2),
            })

        report.sort(key=lambda x: x['avg_performance'], reverse=True)

        return report
