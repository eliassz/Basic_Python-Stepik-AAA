import csv
from typing import Any, Dict, List, Set


PATH = './Corp_Summary.csv'

MAIN_MENU = """
    1. Вывести иерархию команд
    2. Вывести сводный отчёт по департаментам
    3. Сохранить отчёт
    4. Выйти из программы
    Введите номер пункта:
    """
SIDE_MENU = """
    Сохранить csv файл:
    1. Да
    2. Нет/Выйти
    Введите номер пункта:
    """


def read_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Reads the contents of a CSV file specified by file_path.

    Parameters:
    - file_path (str): The path to the CSV file to be read.

    Returns:
    - List[Dict[str, Any]]: A list of dictionaries where each
    dictionary represents a row in the CSV file, with keys being
    the column headers and values being the row entries.
    """
    data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            data.append(row)

    return data


def make_hierarchy(data: List[Dict[str, Any]]) -> Dict[str, Set[str]]:
    """
    Constructs a hierarchy mapping from a list
    of data where each element is a dictionary
    containing department and branch information.

    Parameters:
    - data (List[Dict[str, Any]]): A list of dictionaries where
    each dictionary contains department and branch data with keys
    'Департамент' and 'Отдел'.

    Returns:
    - Dict[str, Set[str]]: A dictionary where keys are department names
    and values are sets of branches within those departments.
    """
    departments = set([el['Департамент'] for el in data])
    hierarchy = {dept: set() for dept in departments}

    for el in data:
        branch = el['Отдел']
        department = el['Департамент']
        if branch not in department:
            hierarchy[department].add(branch)
    return hierarchy


def print_hierarchy(hierarchy: Dict[str, Set[str]]) -> None:
    """
    Prints out the hierarchy of departments and their branches in a readable
    format.

    Parameters:
    - hierarchy (Dict[str, Set[str]]): The hierarchy to be printed,
    represented as a dictionary where the key is a department
    and the value is a set of branches.
    """
    for department, branches in hierarchy.items():
        print(department + ':')
        for branch in branches:
            print(f'    {branch}')
        print()


def make_salary_report(
        data: List[Dict[str, Any]]
        ) -> Dict[str, Dict[str, float]]:
    """
    Generates a salary report from a list of dictionaries containing
    salary data.

    Parameters:
    - data (List[Dict[str, Any]]): A list of dictionaries, where each
    dictionary contains salary information for an employee
    with keys 'Департамент' and 'Оклад'.

    Returns:
    - Dict[str, Dict[str, float]]: A dictionary where the key is a department
    and the value is another dictionary containing 'count', 'min', 'max',
    and 'average' salary data.
    """
    report = {}
    for el in data:
        department = el['Департамент']
        salary = float(el['Оклад'])

        if department not in report:
            report[department] = {
                'count': 0,
                'min': float('inf'),
                'max': -float('inf'),
                'total': 0,
            }

        report[department]['count'] += 1
        if salary < report[department]['min']:
            report[department]['min'] = salary
        if salary > report[department]['max']:
            report[department]['max'] = salary
        report[department]['total'] += salary

    for dept, _ in report.items():
        report[dept]['average'] = round(
            report[dept]['total'] / report[dept]['count'], 0
        )
        del report[dept]['total']

    return report


def print_salary_report(report: Dict[str, Dict[str, float]]) -> None:
    """
    Prints a formatted salary report for each department.

    Parameters:
    - report (Dict[str, Dict[str, float]]): A dictionary representing the
    salary report for each department, where the key is the department name
    and the value is a dictionary with salary statistics.
    """
    header_format = "{:<20} | {:>5} | {:>8} | {:>10} | {:>10}"
    row_format = "{:<20} | {:>5} | {:>8} | {:>10} | {:>10.2f}"
    print(header_format.format('Department', 'Count', 'Min', 'Max', 'Average'))
    print('-' * 60)  # Adjusted to match the number of characters in the header
    for department, info in report.items():
        print(row_format.format(
            department,
            info['count'],
            info['min'],
            info['max'],
            info['average']
        ))


def save_salary_report(report: Dict[str, Dict[str, float]]) -> None:
    """
    Saves the salary report data to a CSV file named 'report.csv'.

    Parameters:
    - report (Dict[str, Dict[str, float]]): A dictionary representing
    the salary report for each department that will be saved to the file.

    Side Effects:
    - A file 'report.csv' is created or overwritten in the current working
    directory with the salary report data.
    """
    for k, v in report.items():
        v.update({'Department': k})

    final_report = list(report.values())
    header = ['Department', 'count', 'min', 'max', 'average']
    name_file = 'report.csv'
    with open(f'{name_file}', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(final_report)
    print(f'\nОтчёт сохранён: {name_file}')


if __name__ == '__main__':
    data = read_file(PATH)
    while True:
        print(MAIN_MENU)

        choice = input()

        if choice == '1':
            hierarchy = make_hierarchy(data)
            print_hierarchy(hierarchy)

        elif choice == '2':
            report = make_salary_report(data)
            print_salary_report(report)
            while True:
                print(SIDE_MENU)

                choice = input()

                if choice == '1':
                    save_salary_report(report)

                elif choice == '2':
                    break

                else:
                    print("""
                          Неверный ввод!
                          Неверный ввод! Пожалуйста,
                          введите номер от 1 до 2.
                        """)

        elif choice == '3':
            report = make_salary_report(data)
            save_salary_report(report)

        elif choice == '4':
            print('\nВыход из программы...')
            break

        else:
            print('\nНеверный ввод! Пожалуйста, введите номер от 1 до 4.')
