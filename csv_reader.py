import csv
file = open('csv_data.csv', 'r')
csv_file = csv.reader(file)
next(csv_file)
for row in csv_file:
   print(row)
file.close()