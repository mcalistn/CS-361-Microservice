import time
import csv
import numpy as np

inputFilePath = '../txt/input.txt'
outputFilePath = '../txt/output.csv'
print("Listening for sort category and file path in '" + inputFilePath + "' text file...")
while True:
    time.sleep(1)
    if open(inputFilePath, 'r').read() != '#':
        with open(inputFilePath, 'r') as inputFile:
            sortNum = inputFile.readline().strip()
            if sortNum.isdigit():
                sortNum = int(sortNum) - 1
                filePath = inputFile.readline().strip()
            inputFile.close()
            open(inputFilePath, 'w').close()      # Erases content of text file.
            open(inputFilePath, 'w').write('#')
            inputFile.close()
            print("\nSorting the file '" + filePath + "' by column number " + str(sortNum + 1) + "...\n")
        with open('./search_results.csv', newline='') as csvfile:
            csv_input = csv.reader(csvfile, delimiter=',', quotechar='"')
            count = 0
            for row in csv_input:
                arrayLine = np.array(row)
                if count == 0:
                    sortArr = np.array(arrayLine)
                    count = 1
                else:
                    sortArr = np.vstack([sortArr, arrayLine])
        csvfile.close()
        while True:
            swappedRow = False
            for i in range(2, len(sortArr)):
                firstSort = sortArr[i - 1][sortNum]
                secondSort = sortArr[i][sortNum]
                if secondSort > firstSort:
                    sortArr[[i - 1, i]] = sortArr[[i, i - 1]]
                    swappedRow = True
            if not swappedRow:
                break
        open(outputFilePath, 'w').close()  # Erases content of text file.
        rowLen = sortArr.shape[1]
        with open(outputFilePath, 'w') as output:
            for row in sortArr:
                for i in range(rowLen):
                    if i != 1:
                        output.write(str(row[i]))
                    else:
                        output.write('"')
                        output.write(str(row[i]))
                        output.write('"')
                    output.write(',')
                output.write('\n')
            







