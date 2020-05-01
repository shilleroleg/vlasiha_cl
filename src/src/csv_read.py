""""
Читает данные из csv файла
разделители - ;

вход:   file_name - имя файла
        column - количество столбцов
        header_line - количество строк заголовка (не читается)

выход:  список с данными по строкам типа float
"""

import csv


def csv_read(file_name: str, column: int, header_line: int):
    with open(file_name) as csvfile:
        read_csv = csv.reader(csvfile, delimiter=';', skipinitialspace=True)
        v = [[], []]
        for row in read_csv:
            if read_csv.line_num > header_line:

                i = 0
                while i < column:
                    v[i].append(float(row[i]))
                    i += 1

    return v