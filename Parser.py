import urllib.request
import json

import urllib.parse
import requests
import csv
from datetime import date

this_year = date.today().year
for year in range(this_year, 2000, -1):
    url = 'https://www.splcenter.org/hate-map/csv/'+str(year)
    response = requests.get(url)
    if not response.links: break  # If response has links, it's not a valid year
encoded_csv = csv.reader(response.text.splitlines())
names = [row[0] for row in encoded_csv]

with open('results.txt', 'w') as output_file:
    for name in names:
        append = urllib.parse.quote(name, safe='')  # Encodes line for url
        url = 'https://autocomplete.clearbit.com/v1/companies/suggest?query=' + append
        with urllib.request.urlopen(url) as response:
            html = json.loads(response.read())  # The URL request returns data in JSON format, which is read here
            if html:
                output_file.write(html[0]['domain'] + "\n")  # The JSON data is converted to a list of dicts, and the first result is written to the output file

print("JOB DONE")  # So I know it's actully finished
