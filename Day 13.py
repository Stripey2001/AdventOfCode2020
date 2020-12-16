file = open("inputDay13.txt","r")

lines = file.readlines()

EarliestDeparture = lines[0]
Buses = lines[1].split(',')
SoonestBus = 0
Answer = 0
print(Buses)


Time = 0
while Time < int(EarliestDeparture):
    Time += int(Buses[0])
SoonestBus = Time
Answer = (SoonestBus - int(EarliestDeparture)) * int(Buses[0])

for Bus in Buses:
    if Bus != 'x':
        Time = 0
        while Time < int(EarliestDeparture):
            Time += int(Bus)
        if Time < SoonestBus:
            SoonestBus = Time
            Answer = (SoonestBus - int(EarliestDeparture)) * int(Bus)
        print(SoonestBus)

print(Answer)

#Part2

Time = 840493039281080
Found = False
while not Found:
    Time += 1
    for i in range(0,len(Buses)):
        if Buses[i] !='x':
            if (Time + i) % int(Buses[i]) == 0:
                Found = True
                #print(Time)
            else:
                Found = False
                break

print(Time)
