import csv
file = open('csv_sample.csv', 'w')
csv_file = csv.writer(file)
csv_file.writerow(['商品','在庫','金額'])
csv_file.writerow(['消しゴム','30','100'])
file.close()