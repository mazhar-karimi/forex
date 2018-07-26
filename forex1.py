
import matplotlib.pyplot as plt
import datetime

values_arr = []
labels_arr = []

with open('dollar_1995_20180726_raw.txt') as file_object:
    for line in file_object:
        if line.startswith('&values='):
            values_str = line[8:-2]
            values_arr = [round(float(x),2) for x in values_str.split(',')]
            values_arr = values_arr[:]
        if line.startswith('&x_labels='):
            labels_str = line[10:-2]
            labels_arr = [datetime.datetime.strptime(x.replace('%2F', '/'), "%d/%m/%Y").date()  for x in labels_str.split(',')]
            labels_arr = labels_arr[:]

values_arr_com = []
labels_arr_com = []
prev = values_arr[0]

for x in range(0,len(labels_arr)):
    if values_arr[x] != prev:
          values_arr_com.append(values_arr[x])
          labels_arr_com.append(labels_arr[x])
    prev = values_arr[x]

#print(values_arr_com)
plt.title('Dollar Rate from 1995-2018')
plt.xlabel('Date')
plt.ylabel('Rs')
#plt.axis([1995, 2018, 25, 140])
x = [i for i in range(1,len(labels_arr_com)+1)]
plt.plot(labels_arr_com, values_arr_com)
plt.show()
