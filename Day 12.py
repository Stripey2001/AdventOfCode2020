file = open("inputDay12.txt","r")

lines = file.readlines()

#Part1

x,y,Direction = 0,0,90

for line in lines:
    if line[0] == "N":
        y+=int(line[1:])
    elif line[0] == "E":
        x+=int(line[1:])
    elif line[0] == "S":
        y+=-int(line[1:])
    elif line[0] == "W":
        x+=-int(line[1:])
    elif line[0] == "R":
        Direction += int(line[1:])
        if Direction >= 360:
            Direction -= 360
    elif line[0] == "L":
        Direction += -int(line[1:])
        if Direction < 0:
            Direction += 360
    elif line[0] == "F":
        if Direction == 0:
            y+=int(line[1:])
        elif Direction == 90:
            x+=int(line[1:])
        elif Direction == 180:
            y+=-int(line[1:])
        elif Direction == 270:
            x+=-int(line[1:])
    #print(x,y)
print(abs(x)+abs(y))

x = y = 0
Waypoint = [10,1]
PlaceHolder = 0

for line in lines:
    if line[0] == "N":
        Waypoint[1] += int(line[1:])
    elif line[0] == "S":
        Waypoint[1] -= int(line[1:])
    elif line[0] == "E":
        Waypoint[0] += int(line[1:])
    elif line[0] == "W":
        Waypoint[0] -= int(line[1:])
    elif line[0] == "F":
        x += Waypoint[0] * int(line[1:])
        y += Waypoint[1] * int(line[1:])
    elif line[0] == "L":
        if int(line[1:]) == 180:
            Waypoint[0] = -Waypoint[0]
            Waypoint[1] = -Waypoint[1]
        elif int(line[1:]) == 90:
            PlaceHolder = Waypoint[1]
            Waypoint[1] = Waypoint[0]
            Waypoint[0] = -PlaceHolder
        elif int(line[1:]) == 270:
            PlaceHolder = Waypoint[1]
            Waypoint[1] = -Waypoint[0]
            Waypoint[0] = PlaceHolder
    elif line[0] == "R":
        if int(line[1:]) == 180:
            Waypoint[0] = -Waypoint[0]
            Waypoint[1] = -Waypoint[1]
        elif int(line[1:]) == 90:
            PlaceHolder = Waypoint[1]
            Waypoint[1] = -Waypoint[0]
            Waypoint[0] = PlaceHolder
        elif int(line[1:]) == 270:
            PlaceHolder = Waypoint[1]
            Waypoint[1] = Waypoint[0]
            Waypoint[0] = -PlaceHolder
    #print(x,y)
    #print(Waypoint)
print(abs(x) + abs(y))
        



