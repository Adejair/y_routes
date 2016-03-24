# -*- coding: iso-8859-15 -*-
import os
import re
import fileinput
import sys


PATH_YSI = raw_input('➜ Write Path to YSI: ')
GET_PREFIX_NAME = 0

# Container with Paths of rootYSI / filesYSI
container = []
# PATH generate of files
rootYSI = []
filesYSI = []
# Variable that will receive regex 
regexS = -666
# Container with files and memory trash of files
containerSubS = []
# Container with PATH cleaned of containerSub | ROUTE: \ 
containerOriginal = []
# Container Modified to Route /
containerModifiedSubS = []


# This function remove from http://stackoverflow.com/questions/7780331/python-replace-value-in-text-at-random
def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)
# Path Get Data
for root, dirs, files in os.walk(PATH_YSI):
	rootYSI.append(root)
	filesYSI.append(files)

# Set Data 'trashed' to container
for i in range(0, len(filesYSI)):
	for j in range(0, len(filesYSI[i])):
		container.append(str(rootYSI[i] + '/' + str(filesYSI[i][j])))

# Regex in all files of data in container, save this data on containerSubS
for i in container:
	file = open(i, 'a+')
	regexS = re.findall(r'(#include(   | ){1,}(\"|<)(\.\.|\\){0,}\w+(\\|\w+){1,}(@?|.?){1,}(\"|>))', file.read())	
	
	if(regexS):
		containerSubS.append(regexS)
	file.close()

# Data to list.
for i in range(0, len(containerSubS)):
	for j in range(0, len(containerSubS[i])):
		containerOriginal.append(str(containerSubS[i][j][GET_PREFIX_NAME]))
		containerModifiedSubS.append(re.sub(r'\\', '/', str(containerSubS[i][j][GET_PREFIX_NAME])))

# Replace values on YSI
for i in container:
	for j in range(0, len(containerOriginal)):
		print(i, containerOriginal[j], containerModifiedSubS[j])
		replaceAll(i, containerOriginal[j], containerModifiedSubS[j])

print('➜ Finished !! Thanks for using y_routes, If you liked favorite in github ')