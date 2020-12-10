file = open("inputDay9.txt","r")

lines = file.readlines()
Preamble = 25
Error = 0

for i in range(Preamble,len(lines)):
    Test = False
    for j in range(1,Preamble+1):
        for k in range(1,Preamble+1):
            if k != j:
                if int(lines[i]) == int(lines[i-j]) + int(lines[i-k]):
                    Test  = True
    if Test is False:
        Error = int(lines[i])

print("Part 1: " ,Error)

#Part2
EncryptionWeakness=[]
for i in range(0,len(lines)):
    Count = 0
    for j in range(i+1,len(lines)):
        Count += int(lines[j])
        if Count > Error:
            break
        elif Count == Error:
            TempCount = 0
            if j-i > 1:
                for k in range(i+1,j+1):
                    EncryptionWeakness.append(int(lines[k]))
                    TempCount += int(lines[k])
EncryptionWeakness.sort()
print("Part 2: " ,EncryptionWeakness[0] + EncryptionWeakness[-1])
