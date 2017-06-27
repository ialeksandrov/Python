import csv

with open('file.txt', 'r') as my_file:
    output = csv.reader(my_file)
    for row in output:
        print(' '.join(row))
