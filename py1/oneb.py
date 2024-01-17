x = input()
xr = x[::-1]

numbers = ['one', 'two', 'three','four', 'five', 'six', 'seven', 'eight', 'nine','zero']
ints = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
emptyArray = []

def find_code(string, integers, numbers, emptyArray):
    inp  = str(string)
    ints = integers
    nums = numbers
    array = emptyArray
    for i in range (len(inp)):
        if (inp[i] in ints):
            array.append(inp[i])
            #return ints[i]

        else:
            if inp[i] == 'o':
                if (inp[i:i+3] in nums):
                    #return 1
                    array.append('1')
            elif inp[i] == 't':
                if (inp[i:i+3] in nums):
                    #return 2
                    array.append('2')
                elif (inp[i:i+5] in nums):
                    #return 3
                    array.append('3')
            elif inp[i] == 'f':
                if (inp[i:i+4] in nums) and (inp[i+1] == 'o'):
                    #return 4
                    array.append('4')
                elif (inp[i:i+5] in nums):
                    array.append('5')
                    #return 5
            elif inp[i] == 's':
                if (inp[i,i+3] in nums):
                    #return 6
                    array.append('6')
                elif (inp[i:i+5] in nums):
                    #return 7
                    array.append('7')
            elif inp[i] == 'e':
                if (inp[i:i+5] in nums):
                    #return 8
                    array.append('8')
            elif inp[i] == 'n':
                if (inp[i:i+4] in nums):
                    #return 9
                    array.append('9')
            elif inp[i] == 'z':
                if (str(inp[i:i+4]) in nums):
                    #return 0
                    array.append('0')

    return(array)


answer = find_code(x,ints,numbers, emptyArray)
print(answer)
code = answer[0] + answer[(len(answer)-1)]
print (code)