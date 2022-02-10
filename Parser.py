import urllib.request
import urllib.parse
import json

with open('groups.txt', 'r') as input_file, open('results.txt', 'w') as output_file:
    line = input_file.readline()
    while line != "":
        append = urllib.parse.quote(line, safe='')
        url = 'https://autocomplete.clearbit.com/v1/companies/suggest?query=' + append
        with urllib.request.urlopen(url) as response:
            html = json.loads(response.read())  # The URL request returns data in JSON format, which is read here
            if html:
                output_file.write(html[0]['domain'] + "\n")  # The JSON data is converted to a list of dicts, and the first result is written to the output file
        line = input_file.readline()

print("JOB DONE")  # So I know it's actully finished
