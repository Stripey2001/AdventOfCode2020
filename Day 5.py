import math
file = open("inputDay5.txt","r")

lines = file.readlines()

#Part 1
MaxID = 0
for line in lines:
    SeatID = 0
    line = line[:-1]
    Row = line[:7]
    Column = line[-3:]
    Upper = 127
    Lower = 0
    for i in range(0,len(Row)):
        if Row[i] == "F":
            Upper = int((Upper - Lower) / 2) + Lower
        elif Row[i] == "B":
            Lower = math.ceil((Upper - Lower) / 2) + Lower
    RowID = Lower
    Upper = 7
    Lower = 0
    for i in range(0,len(Column)):
        if Column[i] == "L":
            Upper = int((Upper - Lower) / 2) + Lower
        elif Column[i] == "R":
            Lower = math.ceil((Upper - Lower) / 2) + Lower
    ColumnID = Lower
    SeatID = RowID * 8 + ColumnID
    if SeatID > MaxID:
        MaxID = SeatID
print(MaxID)

#Part2
IDs = []
for line in lines:
    SeatID = 0
    line = line[:-1]
    Row = line[:7]
    Column = line[-3:]
    Upper = 127
    Lower = 0
    for i in range(0,len(Row)):
        if Row[i] == "F":
            Upper = int((Upper - Lower) / 2) + Lower
        elif Row[i] == "B":
            Lower = math.ceil((Upper - Lower) / 2) + Lower
    RowID = Lower
    Upper = 7
    Lower = 0
    for i in range(0,len(Column)):
        if Column[i] == "L":
            Upper = int((Upper - Lower) / 2) + Lower
        elif Column[i] == "R":
            Lower = math.ceil((Upper - Lower) / 2) + Lower
    ColumnID = Lower
    SeatID = RowID * 8 + ColumnID
    IDs.append(SeatID)
IDs.sort()
myID = 0
for i in range(0,IDs[-1]):
    if i not in IDs:
        if i - 1 in IDs:
            if i + 1 in IDs:
                myID = i
print(myID)
