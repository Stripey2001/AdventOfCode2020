file = open("inputDay6.txt","r")

lines = file.readlines()

def CheckUnique(Answers, Orig, Conv):
    Unique = [Orig] * 26
    for Answer in Answers:
        if Answer == 'a':
            Unique[0] = Conv
        elif Answer == 'b':
            Unique[1] = Conv
        elif Answer == 'c':
            Unique[2] = Conv
        elif Answer == 'd':
            Unique[3] = Conv
        elif Answer == 'e':
            Unique[4] = Conv
        elif Answer == 'f':
            Unique[5] = Conv
        elif Answer == 'g':
            Unique[6] = Conv
        elif Answer == 'h':
            Unique[7] = Conv
        elif Answer == 'i':
            Unique[8] = Conv
        elif Answer == 'j':
            Unique[9] = Conv
        elif Answer == 'k':
            Unique[10] = Conv
        elif Answer == 'l':
            Unique[11] = Conv
        elif Answer == 'm':
            Unique[12] = Conv
        elif Answer == 'n':
            Unique[13] = Conv
        elif Answer == 'o':
            Unique[14] = Conv
        elif Answer == 'p':
            Unique[15] = Conv
        elif Answer == 'q':
            Unique[16] = Conv
        elif Answer == 'r':
            Unique[17] = Conv
        elif Answer == 's':
            Unique[18] = Conv
        elif Answer == 't':
            Unique[19] = Conv
        elif Answer == 'u':
            Unique[20] = Conv
        elif Answer == 'v':
            Unique[21] = Conv
        elif Answer == 'w':
            Unique[22] = Conv
        elif Answer == 'x':
            Unique[23] = Conv
        elif Answer == 'y':
            Unique[24] = Conv
        elif Answer == 'z':
            Unique[25] = Conv
    return Unique


Count = 0
Answers=[]
for line in lines:
    if line == '\n':
        #print(Answers)
        Unique = CheckUnique(Answers,False,True)
        Count += Unique.count(True)
        #print(Count)
        Answers=[]
        Unique = [False] * 25
    else:
        Contents = line.split()
        for Content in Contents:
            for Character in Content:
                Answers.append(Character)

#print(Answers)
Unique = CheckUnique(Answers,False,True)
Count += Unique.count(True)
print(Count)

#Part2
UniqueArray = []
Answers = []
All = [True]*26
Count= 0
for line in lines:
    if line == '\n':
        #print(Answers)
        for i in range (0,len(Answers)):
            UniqueArray.append(CheckUnique(Answers[i],False,True))
        #print(UniqueArray)
        for Array in UniqueArray:
            for i in range(0,26):
                if Array[i] == False:
                    All[i] = False
        #print(All)
        Count += All.count(True)
        #print(Count)
        All = [True]*26
        UniqueArray = []
        Answers = []
    else:
        Characters = []
        for Character in line.strip('\n'):
            Characters.append(Character)
        Answers.append(Characters)
#print(Answers)
for i in range (0,len(Answers)):
    UniqueArray.append(CheckUnique(Answers[i],False,True))
#print(UniqueArray)
for Array in UniqueArray:
    for i in range(0,26):
        if Array[i] == False:
            All[i] = False
#print(All)
Count += All.count(True)
print(Count)
