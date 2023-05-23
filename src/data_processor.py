import csv
import json


def proces_csv_data(file_location):
    with open(file_location, mode='r') as csv_file:
        data = [line for line in csv.DictReader(csv_file)]
        for row in data:
            try:
                row['FirstName'] = str(row['FirstName'])
                row['LastName'] = str(row['LastName'])
                row['Age'] = int(row['Age'])
            except Exception as exp:
                raise ValueError('Invalid input: ' + str(exp))

        return data


def json_reader(file_location):
    with open(file_location) as f:
        return json.load(f)
