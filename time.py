import datetime

d1 = datetime.date(2017, 7, 1)
d2 = d1-datetime.timedelta(days=1)
print(d1,'の1日前は',d2,'です')
d3 = d1+datetime.timedelta(days=1)
print(d1,'の1日後は',d3,'です')
