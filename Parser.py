import urllib.request
import json

import urllib.parse
import requests
import csv
from datetime import date

names = []
this_year = date.today().year
print('Downloading data for each year...')
for year in range(this_year, 1999, -1):
    url = 'https://www.splcenter.org/hate-map/csv/'+str(year)
    response = requests.get(url)
    if response.links: continue  # If response has links, it's not a valid year
    csv_lines = response.text.splitlines()
    encoded_csv = csv.reader(csv_lines)
    print('Got '+str(len(csv_lines))+' names from '+str(year))
    for row in encoded_csv:
        name = row[0]
        if not name in names:
            names.append(name)
print('All data downloaded!')

print('Finding associated websites for each group...')
with open('results.txt', 'w') as output_file:
    for name in names:
        append = urllib.parse.quote(name, safe='')  # Encodes line for url
        url = 'https://autocomplete.clearbit.com/v1/companies/suggest?query=' + append
        with urllib.request.urlopen(url) as response:
            html = json.loads(response.read())  # The URL request returns data in JSON format, which is read here
            if html:
                website = html[0]['domain']
                print(name+': '+website)
                output_file.write(website + "\n")  # The JSON data is converted to a list of dicts, and the first result is written to the output file
            else:
                print('No website found for '+name)

print("JOB DONE")  # So I know it's actully finished
