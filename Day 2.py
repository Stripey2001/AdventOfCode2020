file  = open("inputDay2.txt.","r")

lines = file.readlines()


#Part1
Valid = 0

for line in lines:
    line = line.split()
    Range = line[0].split("-")
    count = 0
    for char in line[2]:
        if char == line[1][0]:
            count += 1
    if count >= int(Range[0]) and count <= int(Range[1]):
        Valid += 1


print(Valid)

#Part2

Valid = 0

for line in lines:
    line = line.split()
    Positions = line[0].split("-")
    Positions[0] = int(Positions[0]) - 1
    Positions[1] = int(Positions[1]) - 1
    if line[2][Positions[0]] == line[1][0]:
        if line[2][Positions[1]] != line[1][0]:
            Valid += 1
    elif line[2][Positions[1]] == line[1][0]:
        Valid += 1
print(Valid)
