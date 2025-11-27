import argparse
from tabulate import tabulate
from src.factory import create_factory_report


def main():
    """
    Настройка скрипты через argparse и формирование таблицы с помощью tabulate
    """
    arg_parser = argparse.ArgumentParser(description="Генератор отчетов")

    arg_parser.add_argument("--files", nargs='+', required=True, help='Путь к файлам')
    arg_parser.add_argument('--report', type=str, required=True, choices=['performance'],
                            help='Указываем какие типы отчетов должны формироваться')
    args = arg_parser.parse_args()

    try:
        new_report = create_factory_report(args.report)

        new_report.load(args.files)

        report = new_report.create_report()

        if report:
            headers = ['Position', 'Average_performance']
            table_data = [[i['position'], i['avg_performance']] for i in report]
            print(tabulate(table_data, headers=headers,
                           showindex=range(1, len(table_data)+1),
                           tablefmt='simple', floatfmt=".2f"))
        else:
            print('Нет данных')

    except Exception as e:
        print(f'Непредвиденная ошибка {str(e)}')
        return 1

    return 0

if __name__ == '__main__':
    exit(main())