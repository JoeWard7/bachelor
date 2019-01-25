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
rachelRead = open("rachel.txt", "r")
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

# divide week 1 losers to a list
week = elimination["1"]
contest = []
for x in week.split(" "):
    contest.append(x)
print("hi")
print(contest)

# divide week 1 picks to a list
joeWeek1 = joeBracket["1"]
joePicks = []
for x in joeWeek1.split(" "):
    joePicks.append(x)
print(joePicks)

# remove the loser form picks
for loser in contest:
    for pick in joePicks:
        if loser == pick:
            joePicks.remove(pick)
print(joePicks)

# get total points for week
joePt = 0
joePt = len(joePicks)
print(joePt)

# gets total potential points based on who is still in
joeTotal = 0
joePicks = []
for week in joeBracket:
    joePicks = []
    for x in joeBracket[week].split(" "):
        joePicks.append(x)
    print(joePicks)
    for loser in contest:
        for pick in joePicks:
            if loser == pick:
                joePicks.remove(pick)
    joeTotal += len(joePicks)
print(joeTotal)

# new looping way
joeTotal = 0
joePicks = []
loser = []
for elimWk in elimination.split(" "):
    loser.append(elimWk)
    joePicks = []
    for week in joeBracket.split(" "):
        if elimWk >= week:
            joePicks.append(week)
            print(joePicks)
        for lose in loser:
            for pick in joePicks:
                if lose == pick:
                    joePick.remove(pick)
    j
