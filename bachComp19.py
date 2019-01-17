"""Testingself."""

maxPoints = 238

# build contestants dictonary
contestantsRead = open("contestants.txt", "r")
contestants = {}
count = 1
for x in contestantsRead:
    contestants[count] = x.rstrip('\n')
    count += 1
print(contestants)

# build bracket joe
joeRead = open("joseph.txt", "r")
joeBracket = {}
for line in joeRead:
    list = []
    for x in line.split(": "):
        list.append(x.rstrip('\n'))
    joeBracket[list[0]] = list[1]
print(joeBracket)

# build bracket rachel
rachelRead = open("joseph.txt", "r")
rachelBracket = {}
for line in rachelRead:
    list = []
    for x in line.split(": "):
        list.append(x.rstrip('\n'))
    rachelBracket[list[0]] = list[1]
print(rachelBracket)

# put each elimination by week in dictonary
eliminationRead = open("elimination.txt", "r")
elimination = {}
for line in eliminationRead:
    list = []
    for x in line.split(": "):
        list.append(x.rstrip('\n'))
    elimination[list[0]] = list[1]
print(elimination)

gone = elimination["Wk1"]
for x in gone.split(" "):
    print(x)
