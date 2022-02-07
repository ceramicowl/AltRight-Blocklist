import urllib.request
import json

input_file = open('groups.txt', 'r')  # This file generated with data from the SLPC
output_file = open('results.txt', 'w')

line = input_file.readline()
while line != "":
    url = 'https://autocomplete.clearbit.com/v1/companies/suggest?query=' + line
    url = url.replace(" ", "_")
    with urllib.request.urlopen(url) as response:
        html = json.loads(response.read())
        if html:
            output_file.write(html[0]['domain'] + "\n")
    line = input_file.readline()

input_file.close()
output_file.close()
print("JOB DONE")
