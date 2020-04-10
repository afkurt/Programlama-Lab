import csv, sys 
from datetime import datetime

arg1 = sys.argv[1]
path = arg1 + "\\input_hw_2.csv"
arg2 = sys.argv[2]
receiver = arg2 + "\\170401002_hw_02_output.txt"

with open(path, 'r', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    main_data = [word for word in [row for row in csv_reader]]
    aa_dates = [main_data[index][3] for index in range(len(main_data))]
    for index in range(len(aa_dates)):
        aa_dates[index] = datetime.strptime(
            aa_dates[index], "%Y-%m-%d %H:%M:%S.%f")
    months = [aa_dates[index].month for index in range(len(aa_dates))]

def Listmedian(inlist):
    newInlist = sorted(inlist)
    n = len(newInlist)
    if n % 2 == 1:
        middle = int(n/2)+1
        median = newInlist[middle - 1]
    else:
        middle_1 = int(n/2) - 1
        middle_2 = middle_1 + 1
        median = (newInlist[middle_1] + newInlist[middle_2]) / 2
    return median


def Histogram(inlist):
    month_dict = dict()
    for index in range(len(inlist)):
        if inlist[index] in month_dict:
            month_dict[inlist[index]] += 1
        else:
            month_dict[inlist[index]] = 1
    return month_dict




def Listmean(inlist):
    x = 0
    count = len(inlist)
    for index in inlist:
        x += index
    mean = x / count
    return mean


months_dict = Histogram(months)
valueList = values = [*months_dict.values()]
median = Listmedian(valueList)
mean = int(Listmean(valueList))
output_list = ["Medyan", str(median), "Ortalama", str(mean)]

with open(receiver, "w", encoding="utf-8") as file:
    for i in range(0,len(output_list),2):
        file.write(output_list[i] + " " + output_list[i+1] + "\n")
