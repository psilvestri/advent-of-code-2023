"""--- Day 2: Cube Conundrum ---"""
# import re

# gameValues = []
# viableGameSum = 0
# viableGameCount = 0

# with open("Day2_Input.txt") as file:
#     for line in file:

#         idMatches = re.search("(?<=Game )\d+(?=:)", line)
#         gameId = idMatches.group(0)

#         redMatches = re.findall("(?<=\s)\d+(?= red)", line)
#         redInts = [int(i) for i in redMatches]
#         maxReds = int(max(redInts))

#         greenMatches = re.findall("(?<=\s)\d+(?= green)", line)
#         greenInts = [int(i) for i in greenMatches]
#         maxGreens = int(max(greenInts))


#         blueMatches = re.findall("(?<=\s)\d+(?= blue)", line)
#         blueInts = [int(i) for i in blueMatches]
#         maxBlues = int(max(blueInts))

#         gameValues.append({"id": gameId, "greens": maxGreens, "reds": maxReds, "blues": maxBlues})

# for game in gameValues:
#     if ((game["reds"] <= 12) and (game["greens"] <= 13) and (game["blues"] <= 14)):
#         viableGameSum += int(game["id"])
#         viableGameCount += 1

# print(viableGameSum)


"""--- Part Two ---"""

import re

gameValues = []
totalPower = 0


with open("Day2_Input.txt") as file:
    for line in file:

        idMatches = re.search("(?<=Game )\d+(?=:)", line)
        gameId = idMatches.group(0)

        redMatches = re.findall("(?<=\s)\d+(?= red)", line)
        redInts = [int(i) for i in redMatches]
        maxReds = int(max(redInts))

        greenMatches = re.findall("(?<=\s)\d+(?= green)", line)
        greenInts = [int(i) for i in greenMatches]
        maxGreens = int(max(greenInts))


        blueMatches = re.findall("(?<=\s)\d+(?= blue)", line)
        blueInts = [int(i) for i in blueMatches]
        maxBlues = int(max(blueInts))

        gameValues.append({"id": gameId, "greens": maxGreens, "reds": maxReds, "blues": maxBlues})

for game in gameValues:
    totalPower += game["reds"] * game["greens"] * game["blues"]

print(totalPower)