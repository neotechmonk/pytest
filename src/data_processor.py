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


import json


def proces_json_data(file_location):
    with open(file_location) as json_file:
        data = json.load(json_file)
        for item in data:
            try:
                item["FirstName"] = str(item["FirstName"])
                item["LastName"] = str(item["LastName"])
                item["Age"] = int(item["Age"])
            except Exception as exp:
                raise ValueError('Invalid input: ' + str(exp))

        return data

