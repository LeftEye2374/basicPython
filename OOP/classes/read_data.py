import json

with open('data/egypt.json', 'r') as country_file:
    file_data = json.load(country_file)


class CountryData:

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = self.read_data()
        self.country = self.file_data['country']
        self.max_temp = self.file_data['max_temp']
        self.min_temp = self.file_data['min_temp']


    def read_data(self):
        with open(self.file_path, 'r') as country_file:
            return json.load(country_file)




egypt = CountryData('data/egypt.json')
print(egypt.file_data)
print(egypt.country)
print(egypt.max_temp)
print(egypt.min_temp)
