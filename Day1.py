"""--- Day 1: Trebuchet?! ---"""

# import re

# calibrationTotal = 0

# with open("Day1_Input.txt") as file:
#     for line in file:
#         lineInts = re.sub("[^\d\.]", "", line)
#         calibrationStr = lineInts[0] + lineInts[-1]
#         calibrationInt = int(calibrationStr)
#         calibrationTotal += calibrationInt

# print(calibrationTotal)

"""--- Part Two ---""" 

import re

calibrationTotal = 0

def replace_strings(string, dict):
    for i, j in dict.items():
        string = string.replace(i, j)
    return string

replacements = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open("Day1_Input.txt") as file:
    for line in file:
        matches = re.finditer(r"(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))", line)
        matchGroup = [match.group(1) for match in matches]
        matchInts =  [replace_strings(i, replacements) for i in matchGroup]
        calibrationStr = matchInts[0] + matchInts[(len(matchInts) - 1)]
        calibrationInt = int(calibrationStr)
        calibrationTotal += calibrationInt

print(calibrationTotal)