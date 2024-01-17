import re
schematic = input()
sublist1 = re.split(': | |\n |, ',schematic)
print(sublist1)

lines = len(sublist1)
length = len(sublist1[0])

valid = []

for i in range (lines):

    separated = re.split('|. ',sublist1[i])
    print(separated)

    for j in range (length):
        if separated[j] != '.':
            if separated[j] is int:
                if (separated[j+1] != '.') or (separated[j-1] != '.'):
                    valid.append(separated[j+1])
            else:
                temp= separated[j+1]
                numlength = len(separated[j+1])
                separated = re.split('|. ',sublist1[i])
                