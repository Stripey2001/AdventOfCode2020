file = open("inputDay10.txt","r")

lines = file.readlines()

oneUp = 0
threeUp = 1

for k in range(0,len(lines)):
    lines[k] = int(lines[k])

lines.sort()

if lines[0] == 1:
    oneUp = 1
elif lines[0] == 3:
    threeUp += 1

for i in range(0,len(lines)-1):
    if lines[i] == (lines[i+1] - 1):
        oneUp += 1
    elif lines[i] == (lines[i+1] - 3):
        threeUp += 1

print(oneUp,threeUp)
print(oneUp * threeUp)

#part2
Routes = 0
#print(lines[1] - 3)
if lines[0] > (lines[2] - 3):
    if lines[0] > (lines[3] - 3):
        Routes = 3
    else:
        Routes = 2
else:
    Routes = 1
i = 1
while i <= len(lines):
    #print(i)
    try:
        if lines[i] >= (lines[i+2] - 3):
            if lines[i] >= (lines[i+3] - 3):
                if Routes == 1:
                    Routes = 3
                else:
                    Routes = 3 ** Routes
                i=i+2
                #print("3")
            if Routes == 1:
                Routes = 2
            else:
                Routes = 2 ** Routes
            i=i+1
            #print("2")
        print(Routes)
    except:
        print("Too Close")
    i+=1
print(Routes)
        
    
        
    
