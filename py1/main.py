array1 = []
array2 = []
array3 = []

students = []

house1 = []

# house 1 has 10 people
house1.append(students[0]) 
t=0

for i in range (10): 
    if students[t] != "-":
        house1.append(students[t][1])
        for j in students:
            if (students[j] == students[t][1]):
                t = j

    else:
        t += 1
    students[t]== "-"