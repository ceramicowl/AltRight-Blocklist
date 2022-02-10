import requests
import csv

url = 'https://www.splcenter.org/hate-map/csv/2020'

response = requests.get(url)
obj = csv.reader(response.text.splitlines())
for row in obj:
    print(row[0])