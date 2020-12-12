import csv
import json
import os


class Utility:

    def get_browser(self):
        try:
            return os.environ['BROWSER']
        except KeyError:
            return 'ff'


    def read_csv(self, fileName):
        data = []
        with open(fileName, 'r') as  csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            for row in reader:
                data.append(row)
            return data

    def read_json(self, fileName):
        data = []
        with open(fileName, 'r') as  jsonfile:
            reader = json.load(jsonfile)
            for row in reader:
                data.append(row)
            return data
