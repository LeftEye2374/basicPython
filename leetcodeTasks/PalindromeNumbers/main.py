#x = 121
#x = -121
x = -10
#x = 100021

string = str(x)
if len(string) % 2 == 0:
    firstPart = []
    secondPart = []
    middle = len(string) // 2
    for i in range(0, middle):
        firstPart.append(string[i])
    index = -1
    for i in range(middle, len(string)):
        secondPart.append(string[index])
        index -= 1
    if firstPart == secondPart:
        print(True)
    else:
        print(False)
else:
    chars = []
    for i in range(0, len(string)):
        chars.append(string[i])
    if chars[0] == chars[-1]:
        print(True)
    else:
        print(False)
   