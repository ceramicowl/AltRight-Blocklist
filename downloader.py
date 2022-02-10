import requests
import csv
from datetime import date

url_base = 'https://www.splcenter.org/hate-map/csv/'

this_year = date.today().year
for year in range(this_year, 2000, -1):
    url = url_base+str(year)
    response = requests.get(url)
    if not response.links: break  # If response has links, it's not a valid year

encoded_csv = csv.reader(response.text.splitlines())
names = [row[0] for row in encoded_csv]
print(names)
