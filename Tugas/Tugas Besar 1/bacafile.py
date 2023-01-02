import csv


with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print(csv_reader)
    List=[]
    for row in csv_reader:
        List.append(row)

print(List[0])
label = List.pop(0)
print('index 0:', List[0])
print('label', label)


