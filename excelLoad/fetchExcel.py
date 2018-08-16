import xlrd


def filter_time(atime_list):
    latest_temp = '00:00'
    earliest_temp = '24:00'
    for time in atime_list:
        if time > latest_temp:
            latest_temp = time
        if time < earliest_temp:
            earliest_temp = time
    return earliest_temp, latest_temp


data = xlrd.open_workbook('./6yue.xls')
table = data.sheet_by_index(0)
nrows = table.nrows

ear_list = []
lat_list = []

for i in range(1, nrows):
    row_list = table.row_values(i)
    time_str = row_list[4]
    time_list = time_str.split()
    t_tuple = filter_time(time_list)
    ear_list.append(t_tuple[0])
    lat_list.append(t_tuple[1])

for value_1 in ear_list:
    print(value_1)
print('\n\n\n')
for value_2 in lat_list:
    print(value_2)
