import re
import csv

with open('onelinefile.txt', 'r') as f:
    contents = f.read().strip()

pattern = r'(\d+)([A-Za-z]+)(\d+\.\d+)([A-Za-z]+)'

matches = re.findall(pattern, contents)

with open('Filename2.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['ID', 'Name', 'Score', 'Subject'])

    for i, match in enumerate(matches):
        row = [i+1, match[1], float(match[2]), match[3]]
        writer.writerow(row)

