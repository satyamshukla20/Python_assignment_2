import csv

#list
first_name=[]
last_name=[]
roll=[]

#set
first_name_set=set()

#dictionary
dict={}



with open('first_task.csv',mode='r') as file:
    file1=csv.reader(file)

    for row in file1:
        if row[0]!='first_name':
            first_name.append(row[0])
            first_name_set.add(row[0])
            dict[row[0]+" "+row[1]]=row[2]

        if row[1]!='last_name':
            last_name.append(row[1])

        if row[2]!='roll':
            roll.append(row[2])

print(first_name)
print(last_name)
print(roll)
print(first_name_set)
print(dict)


