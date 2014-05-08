#!/usr/bin/python

import sys
import os

array = []
with open(sys.argv[1], 'r') as fp:
	for line in fp:
		array.append(int(line))

print array

misplaced = 0
for i in range(len(array)):
	if array[i] != i +1:
		misplaced += 1

print misplaced