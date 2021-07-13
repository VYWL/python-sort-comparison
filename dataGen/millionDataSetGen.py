import csv
import random
import copy

millionSet = list(range(1, 1000001))

normalList = copy.deepcopy(millionSet); millionSet.reverse()
randomList = copy.deepcopy(millionSet); random.shuffle(randomList)
reversedList = copy.deepcopy(millionSet)

f1 = open('normalMillionSet.csv', 'w', newline='')
f2 = open('randomMillionSet.csv', 'w', newline='')
f3 = open('reversedMillionSet.csv', 'w', newline='')

wr = csv.writer(f1)
wr.writerow(normalList)
wr = csv.writer(f2)
wr.writerow(randomList)
wr = csv.writer(f3)
wr.writerow(reversedList)