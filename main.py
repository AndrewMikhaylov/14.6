import sys

def recursion(list, start, lengthOfList, sumOfAllElements, biggestFraction):
    listOfAnswers = []
    if start<0:
        return
    lengthOfList = lengthOfList+1
    listOfAnswers.append(lengthOfList)

    sumOfAllElements = sumOfAllElements+list[start]
    listOfAnswers.append(sumOfAllElements)

    biggestFraction = recursiveFraction(list[start], list, 0, biggestFraction)
    listOfAnswers.append(biggestFraction)

    if list[start] == list[-1]:
        return listOfAnswers
    else:
        return(recursion(list, start+1, lengthOfList, sumOfAllElements, biggestFraction))

def recursiveFraction(number, list, start, highestFraction):
    if start<0:
        return
    currentFraction = number/list[start]
    highestFraction = max(currentFraction, highestFraction)
    if list[start] == list[-1]:
        return highestFraction
    else:
        return recursiveFraction(number, list, start+1, highestFraction)
list = [1, 12, 73, 4, 5, 99, 23]
result = recursion(list, 0, 0, 0, -sys.maxsize)
print("Довжина списку: ")
print(str(result[0]))
print("Сума всіх елементів: ")
print(str(result[1]))
print("Найбільша частка: ")
print(result[2])

