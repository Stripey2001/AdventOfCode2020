file = open("inputDay8.txt","r")

lines = file.readlines()



for i in range(0,len(lines)):
    Found = True
    Executed = [False] * len(lines)
    Accumulator = 0
    j = 0
    if lines[i][:3] == 'jmp':
        lines[i] = 'nop ' + lines[i][4:]
    elif lines[i][:3] == 'nop':
        lines[i] = 'jmp ' + lines[i][4:]
    while j < len(lines):
        if Executed[j] == True:
            Found = False
            break
        Executed[j] = True
        if lines[j][:3] == 'acc':
            Accumulator += int(lines[j][4:])
            j += 1
        elif lines[j][:3] == 'jmp':
            j += int(lines[j][4:])
        elif lines[j][:3] == 'nop':
            j+=1
    if Found:
        print(Accumulator)
    if lines[i][:3] == 'jmp':
        lines[i] = 'nop ' + lines[i][4:]
    elif lines[i][:3] == 'nop':
        lines[i] = 'jmp ' + lines[i][4:]
    
