i = int(input())
j= int(input())
total = 0
counter = 0

def func(end,n, counter):
    if n==end:
        counter=counter+1
        print(i,j,counter)
        return counter
    else:
        if n%2==0:
            n = n/2
        else:
            n = (3*n)+1
        counter=counter+1
        func(end, n,counter)


for index in range(i,j):
    x = func(i,index,counter)
    print(i,j,counter)

print("meow meow")










