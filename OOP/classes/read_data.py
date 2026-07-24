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

    def is_comfortable(self):
        return self.max_temp - self.min_temp > 10


class CountyDataWithSunDays(CountryData): # дочерний класс CountyData
    def __init__(self, file_path):
        super().__init__(file_path)
        self.sunny_days = self.file_data['sunny_days']


    def is_comfortable(self):
        return self.max_temp - self.min_temp + self.sunny_days > 10

egypt = CountryData('data/egypt.json')
print(egypt.file_data)
print(egypt.country)
print(egypt.max_temp)
print(egypt.min_temp)
print(egypt.is_comfortable())

sweden = CountyDataWithSunDays('data/sweden.json')
print(sweden.file_data)
print(sweden.country)
print(sweden.max_temp)
print(sweden.min_temp)
print(sweden.sunny_days)
print(sweden.is_comfortable())