import csv
import datetime as dt

data = open("AAPL1+2.csv",newline='')
reader = csv.reader(data, delimiter=',')
header = reader.__next__()

for line in range(10):
    chunk = reader.__next__()[1:5]
    date = chunk[0]
    time = chunk[1]
    price = chunk[2]
    #print(date)
    year = int(date[0:4])
    #print(year)
    month = int(date[4:6])
    #print(month)
    day =  int(date[6:8])
    #print(day)
    hour = int(time[0:1])
    minute = int(time[2:4])
    second = int(time[5:7])
    datetime = dt.datetime(year,month,day,hour,minute,second)
   
    print(datetime)







