import csv


def parse(file_path: str) -> list:
    with open(file_path, 'rt') as csv_file:
        csv_data = list(csv.DictReader(csv_file))

    return csv_data
