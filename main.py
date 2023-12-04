arr2d = []
numberArr = []

def findDigits(line):
    x = 0
    while x < len(line):
        if line[x].isdigit():
            digitStart = x
            while x < len(line) and line[x].isdigit():
                x = x + 1
            digitEnd = x
            numberArr.append(line[digitStart:digitEnd]) # add check for symbols
        x = x + 1

# read file into arr
with open('input.txt') as file:
    for line in file:
        line = line.strip()
        arr2d.append(line)
        findDigits(line)
    
    print(numberArr)






# if number is found:
    # read until no more number
    # save locations
    # check -1 x
    # check +1 x
    # check -1 y in all number locations
    # check +1 y in all number locations
    # check -1 x -1 y 
    # check +1 x +1 y
    # check -1 x +1 y
    # check +1 x -1 y
# if any location checked != . && number then its a part number