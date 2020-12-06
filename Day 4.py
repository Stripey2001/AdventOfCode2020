file = open("inputDay4.txt","r")

lines = file.readlines()

#Part1
Passport =[]
PassportContents=[]
Contents = []
Valid = 0
byr,iyr,eyr,hgt,hcl,ecl,pid = 0,0,0,0,0,0,0
for line in lines:
    
    if line == "\n":
        if 'byr' not in Passport or 'iyr' not in Passport or 'eyr' not in Passport or 'hgt' not in Passport or 'hcl' not in Passport or 'ecl' not in Passport or 'pid' not in Passport:
            print("Invalid")
        else:
            byr = Passport.index('byr')
            iyr = Passport.index('iyr')
            eyr = Passport.index('eyr')
            hgt = Passport.index('hgt')
            hcl = Passport.index('hcl')
            ecl = Passport.index('ecl')
            pid = Passport.index('pid')
            if len(PassportContents[byr]) != 4 or int(PassportContents[byr]) > 2002 or int(PassportContents[byr]) < 1920:
                print("Invalid")
            elif len(PassportContents[iyr]) != 4 or int(PassportContents[iyr]) > 2020 or int(PassportContents[byr]) < 2010:
                print("Invalid")
            elif len(PassportContents[eyr]) != 4 or int(PassportContents[eyr]) > 2030 or int(PassportContents[eyr]) < 2020:
                print("Invalid")
            elif PassportContents[hcl][:1] != '#' or len(PassportContents[hcl]) != 7:
                try:
                    
                print("Invalid")
            print(PassportContents)
            print(Passport)
            print("Valid")
            Valid += 1
        Passport =[]
        PassportContents=[]
        byr,iyr,eyr,hgt,hcl,ecl,pid = 0,0,0,0,0,0,0
    else:
        Contents = line.split()
        for Content in Contents:
            PassportContents.append(Content[4:])
            Passport.append(Content[:3])

if 'byr' not in Passport or 'iyr' not in Passport or 'eyr' not in Passport or 'hgt' not in Passport or 'hcl' not in Passport or 'ecl' not in Passport or 'pid' not in Passport:
    print("Invalid")
else:
    print(PassportContents)
    print(Passport)
    print("Valid")
    Valid += 1
Passport =[]

print(Valid)

#Does Not Work
