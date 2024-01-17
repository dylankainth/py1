import re 
games = input()

red = []
blue = []
green = []
bad = []
successes = []

counter = 0
new_counter = 0
success_counter = 0


sublist1 = re.split(': | |; |, ',games)


for i in range (len(sublist1)):
    if sublist1[i] == "Game":
        counter +=1
    if sublist1[i] == 'blue':
        blue.append('Game')
        blue.append(counter)
        blue.append(sublist1[i-1])
    if sublist1[i] == 'green':
        green.append('Game')
        green.append(counter)
        green.append(sublist1[i-1])
    if sublist1[i] == 'red':
        red.append('Game')
        red.append(counter)
        red.append(sublist1[i-1])

def succeed(x,y,z,a):
    colour =x
    max = y
    successes = z
    bad = a

    for i in range (len(colour)):
        if colour[i] == "Game":
            if int(colour[i+2]) <= max:
                if (int(colour[i+1]) not in successes)  and (int(colour[i+1]) not in bad):
                    successes.append(int(colour[i+1]))
            else:
                if int(colour[i+1]) in successes:
                    successes.remove(int(colour[i+1]))
                bad.append(int(colour[i+1]))

    return successes 

successes2 = succeed(green,13,successes,bad)
successes3 = succeed(red,12,successes2,bad)
successes4 = succeed(blue,14,successes3,bad)

for i in successes4:
    success_counter = success_counter + int(i) 

print(successes4)
print(success_counter)


