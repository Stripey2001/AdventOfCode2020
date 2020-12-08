file = open("inputDay8.txt","r")

lines = file.readlines()

Executed = [False] * len(lines)
Accumulator = 0
i = 0
while i < len(lines):
    if Executed[i] == True:
        break
    Executed[i] = True
    if lines[i][:3] == 'acc':
        Accumulator += int(lines[i][4:])
        i += 1
    elif lines[i][:3] == 'jmp':
        i += int(lines[i][4:])
    elif lines[i][:3] == 'nop':
        i+=1
print(Accumulator)
    
    
