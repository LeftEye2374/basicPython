import json

with open('data/egypt.json', 'r') as country_file:
    file_data = json.load(country_file)

print(file_data['country'])