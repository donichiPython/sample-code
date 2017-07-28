import csv
file = open('csv_data.csv', 'r')
csv_file = csv.reader(file)
print(next(csv_file))
print(next(csv_file))
file.close()