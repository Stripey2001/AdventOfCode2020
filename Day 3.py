file = open("inputDay3.txt","r")

lines = file.readlines()
#Part1
Trees, xPos, yPos = 0 , 0 , 0



for i in range(0,len(lines)):
    lines[i] = list(lines[i])
    del lines[i][-1]


while yPos < len(lines):
    if xPos > len(lines[0]) - 1:
        xPos = xPos - len(lines[0])
    if lines[yPos][xPos] == '#':
        Trees += 1
    xPos += 3
    yPos += 1

print(Trees)
#Part2

TreeValues = [0,0,0,0,0]

def slopeTest(xAngle,yAngle):
    Trees, xPos, yPos = 0 , 0 , 0
    while yPos < len(lines):
        if xPos > len(lines[0]) - 1:
            xPos = xPos - len(lines[0])
        if lines[yPos][xPos] == '#':
            Trees += 1
        xPos += xAngle
        yPos += yAngle
    return Trees

TreeValues[0] = slopeTest(1,1)
TreeValues[1] = slopeTest(3,1)
TreeValues[2] = slopeTest(5,1)
TreeValues[3] = slopeTest(7,1)
TreeValues[4] = slopeTest(1,2)
print(TreeValues)
print(TreeValues[0]*TreeValues[1]*TreeValues[2]*TreeValues[3]*TreeValues[4])
