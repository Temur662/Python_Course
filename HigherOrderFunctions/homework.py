#1
from functools import reduce
cel = [0, 32, 1, 2, 3]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, cel ))
print(fahrenheit)

#2
nums = [3, 5, 2, 4, 6, 8]
total = reduce(lambda x, y: x + y, nums)
print(total)

#3
def noVowelsOrSpace(word):
    letters = ["a","e","i","o","u"]
    if word in letters:
        return True
    return False
theString = "Hello this is Temur and Python is cool"
noSpacesOrVowel = filter(noVowelsOrSpace, theString)
completeString = ""
for s in noSpacesOrVowel:
    completeString += s
print(completeString)