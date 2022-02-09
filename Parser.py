import urllib.request
import json

input_file = open('groups.txt', 'r')  # This file manually generated with data from the SPLC
output_file = open('results.txt', 'w')

line = input_file.readline()
while line != "":
    append = line.replace(" ", "_") # Lines 9 & 10 change the organization name to proper HTML format
    append = line.replace("/", "&sol;")
    url = 'https://autocomplete.clearbit.com/v1/companies/suggest?query=' + append
    with urllib.request.urlopen(url) as response:
        html = json.loads(response.read()) # The URL request returns data in JSON format, which is read here
        if html:
            output_file.write(html[0]['domain'] + "\n") # The JSON data is converted to a list of dicts, and the first result is written to the output file
    line = input_file.readline()

input_file.close()
output_file.close()
print("JOB DONE") # So I know it's actully finished
