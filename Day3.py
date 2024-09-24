"""--- Day 3: Gear Ratios ---"""
import re

matrix = []
totalSum = 0
currentNumber = ""
checkedIndices = []
symbolRegex = r'[^0-9\s\.]'

with open("Day3_Input.txt") as file:
        for line in file:
            matrix.append(list(line))

for i, list in enumerate(matrix):
    for j, character in enumerate(list):
        if character.isdigit():
            checkedIndices.append(j)
            currentNumber += character
        else:
            if checkedIndices != []:
                # Add +1/-1 to index list to account for adjacent spots above and below
                if j != 0:
                    checkedIndices.insert(0, checkedIndices[0] - 1) 
                if j != len(list):
                    checkedIndices.append(checkedIndices[-1] + 1)

                for checkedIndex in checkedIndices:
                    # If first item in list, don't look for line above
                    if i == 0:
                        if re.findall(symbolRegex, matrix[i+1][checkedIndex]) or re.findall(symbolRegex, matrix[i][checkedIndex]):
                            totalSum += int(currentNumber)
                    # If last item in list, don't look for line below
                    elif i == 139:
                        if re.findall(symbolRegex, matrix[i-1][checkedIndex]) or re.findall(symbolRegex, matrix[i][checkedIndex]):
                            totalSum += int(currentNumber)
                    # Otherwise, check both
                    else: 
                        if re.findall(symbolRegex, matrix[i-1][checkedIndex]) or re.findall(symbolRegex, matrix[i+1][checkedIndex]) or re.findall(symbolRegex, matrix[i][checkedIndex]):
                            totalSum += int(currentNumber)

                checkedIndices = []
            currentNumber = ""
print(totalSum)                   
