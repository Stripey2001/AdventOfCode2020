file = open("inputDay7.txt","r")

lines = file.readlines()

def CreateColour(Adj,Colour):
    Colour = Adj + " " + Colour
    return Colour

#Part1
Rules = []

def CheckColour(Colour,Rules):
    Able = []
    for Rule in Rules:
        if len(Rule) == 2:
            for Bag in Rule[1]:
                if Bag == Colour:
                    Able.append(Rule[0])
    return Able

for line in lines:
    Rule = []
    Contains = []
    Master  = ""
    Words = line.split()
    Master = CreateColour(Words[0],Words[1])
    Rule.append(Master)
    Words = Words[4:]
    if len(Words) == 3:
        Empty = 0
    else:
        for i in range(0,int(len(Words)/4)):
            Contains.append(CreateColour(Words[i*4 + 1],Words[i*4 + 2]))
        Rule.append(Contains)
    Rules.append(Rule)

Able = CheckColour("shiny gold",Rules)
i = 0
while i < len(Able):
    Check = CheckColour(Able[i],Rules)
    for Colour in Check:
        Able.append(Colour)
    i+=1
Able = list(dict.fromkeys(Able))
print(len(Able))

#Part 2

Rules = []

def CheckBag(Colour,Rules):
    Contains = []
    for Rule in Rules:
        if Rule[0] == Colour:
            if len(Rule) == 1:
                return -1
            else:
                for Bag in Rule[1]:
                    for i in range(0,int(Bag[0])):
                        Contains.append(Bag[1])
                return Contains
            

for line in lines:
    Rule = []
    Contains = []
    Master  = ""
    Words = line.split()
    Master = CreateColour(Words[0],Words[1])
    Rule.append(Master)
    Words = Words[4:]
    if len(Words) == 3:
        Empty = 0
    else:
        for i in range(0,int(len(Words)/4)):
            Colour = CreateColour(Words[i*4 + 1],Words[i*4 + 2])
            Colour = [Words[i*4],Colour]
            Contains.append(Colour)
        Rule.append(Contains)
    Rules.append(Rule)

Contains = CheckBag("shiny gold", Rules)
i = 0
while i < len(Contains):
    Check = CheckBag(Contains[i],Rules)
    if Check == -1:
        i += 1
    else:
        for Bag in Check:
            Contains.append(Bag)
        i+=1
print(len(Contains))
