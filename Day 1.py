file = open('inputDay1.txt','r')

lines = file.readlines()

#Part 2
for line1 in lines:
    for line2 in lines:
        for line3 in lines:
            if int(line1) + int(line2) + int(line3) == 2020:
                print(int(line1)*int(line2)*int(line3))

#Part 1
for line1 in lines:
    for line2 in lines:
        if int(line1) + int(line2) == 2020:
                print(int(line1)*int(line2))
