import csv
from array import *
import re


# DATA SETS
mentors = []
mentees = []

# QUESTION ARRAY
questions = {}
questionText = {}

mentorHeaders = []
menteeHeaders = []

# SCORE MATRIX
scores = []

with open('./input/A.csv') as mentor_file:
    mentor_reader = csv.reader(mentor_file, delimiter=',', quotechar='"')
    rowIndex = 0
    labels = []
    questionsFull = []
    for row in mentor_reader:
        if (rowIndex == 0):
            labels = row
            rowIndex += 1
        elif (rowIndex <= 2):
            questionsFull = row
            rowIndex += 1
        else:
            break

    labelIndex = 0
    for label in labels:
        if (label and "TEXT" not in label):
            questions[label] = []
            questionText[label] = questionsFull[labelIndex]
        labelIndex += 1

with open('./input/A.csv') as mentor_file:
    mentor_reader = csv.reader(mentor_file, delimiter=',', quotechar='"')
    rowIndex = 0
    for row in mentor_reader:
        if (rowIndex == 0):
            mentorHeaders = row
        if (rowIndex < 2):
            rowIndex += 1
        elif (row != []):
            answerIndex = 0
            for answer in row:
                if (mentorHeaders[answerIndex] and "TEXT" not in mentorHeaders[answerIndex]):
                    if (mentorHeaders[answerIndex] == "Q3"):
                        newAnswerArray = []
                        tempLanguageArray = re.split(
                            ",|&| and |some |/|;|n/a", answer)
                        for lang in tempLanguageArray:
                            tempProcessedLang = lang.strip().lower()
                            if (tempProcessedLang):
                                if ("mandarin" in tempProcessedLang):
                                    newAnswerArray.append("mandarin")
                                    questions[mentorHeaders[answerIndex]].append(
                                        "mandarin")
                                elif ("filipino" in tempProcessedLang):
                                    newAnswerArray.append("filipino")
                                    questions[mentorHeaders[answerIndex]].append(
                                        "filipino")
                                elif ("french" in tempProcessedLang):
                                    newAnswerArray.append("french")
                                    questions[mentorHeaders[answerIndex]].append(
                                        "french")
                                elif ("farsi" in tempProcessedLang):
                                    newAnswerArray.append("farsi")
                                    questions[mentorHeaders[answerIndex]].append(
                                        "farsi")
                                elif ("japanese" in tempProcessedLang):
                                    newAnswerArray.append("japanese")
                                    questions[mentorHeaders[answerIndex]].append(
                                        "japanese")
                                else:
                                    newAnswerArray.append(tempProcessedLang)
                                    questions[mentorHeaders[answerIndex]].append(
                                        tempProcessedLang)
                        row[answerIndex] = newAnswerArray
                    elif (mentorHeaders[answerIndex] == "Q16" or mentorHeaders[answerIndex] == "Q13" or mentorHeaders[answerIndex] == "Q14" or mentorHeaders[answerIndex] == "Q15"):
                        newAnswerArray = []
                        tempFieldArray = re.split(
                            ",", answer)

                        for field in tempFieldArray:
                            tempProssesedField = field.strip()
                            if (tempProssesedField and tempProssesedField[0] == tempProssesedField[0].upper()):
                                if ("(" in tempProssesedField):
                                    tempProssesedField = tempProssesedField[:tempProssesedField.index(
                                        "(")]
                                questions[mentorHeaders[answerIndex]].append(
                                    tempProssesedField.strip().lower())
                                newAnswerArray.append(
                                    tempProssesedField.strip().lower())
                        row[answerIndex] = newAnswerArray
                    elif (answer):
                        questions[mentorHeaders[answerIndex]].append(answer)

                    questions[mentorHeaders[answerIndex]] = list(
                        dict.fromkeys(questions[mentorHeaders[answerIndex]]))

                answerIndex += 1
            mentors.append(row)
            rowIndex += 1


with open('./input/B.csv') as mentee_file:
    mentee_reader = csv.reader(mentee_file, delimiter=',', quotechar='"')
    rowIndex = 0
    for row in mentee_reader:
        if (rowIndex == 0):
            menteeHeaders = row
        if (rowIndex < 2):
            rowIndex += 1
        elif (row != []):
            answerIndex = 0
            for answer in row:
                if (menteeHeaders[answerIndex] and "TEXT" not in menteeHeaders[answerIndex]):
                    if (menteeHeaders[answerIndex] == "Q3"):
                        newAnswerArray = []
                        tempLanguageArray = re.split(
                            ",|&| and |some |/|;|n/a", answer)
                        for lang in tempLanguageArray:
                            tempProcessedLang = lang.strip().lower()
                            if (tempProcessedLang):
                                if ("mandarin" in tempProcessedLang):
                                    newAnswerArray.append("mandarin")
                                    questions[menteeHeaders[answerIndex]].append(
                                        "mandarin")
                                elif ("filipino" in tempProcessedLang):
                                    newAnswerArray.append("filipino")
                                    questions[menteeHeaders[answerIndex]].append(
                                        "filipino")
                                elif ("french" in tempProcessedLang):
                                    newAnswerArray.append("french")
                                    questions[menteeHeaders[answerIndex]].append(
                                        "french")
                                elif ("farsi" in tempProcessedLang):
                                    newAnswerArray.append("farsi")
                                    questions[menteeHeaders[answerIndex]].append(
                                        "farsi")
                                elif ("japanese" in tempProcessedLang):
                                    newAnswerArray.append("japanese")
                                    questions[menteeHeaders[answerIndex]].append(
                                        "japanese")
                                else:
                                    newAnswerArray.append(tempProcessedLang)
                                    questions[menteeHeaders[answerIndex]].append(
                                        tempProcessedLang)
                        row[answerIndex] = newAnswerArray
                    elif (menteeHeaders[answerIndex] == "Q13" or menteeHeaders[answerIndex] == "Q15" or menteeHeaders[answerIndex] == "Q16" or menteeHeaders[answerIndex] == "Q14"):
                        newAnswerArray = []
                        tempFieldArray = re.split(
                            ",", answer)

                        for field in tempFieldArray:
                            tempProssesedField = field.strip()
                            if (tempProssesedField and tempProssesedField[0] == tempProssesedField[0].upper()):
                                if ("(" in tempProssesedField):
                                    tempProssesedField = tempProssesedField[:tempProssesedField.index(
                                        "(")]
                                newAnswerArray.append(
                                    tempProssesedField.strip().lower())
                                questions[menteeHeaders[answerIndex]].append(
                                    tempProssesedField.strip().lower())
                        row[answerIndex] = newAnswerArray
                    elif (answer and menteeHeaders[answerIndex] in questions):
                        questions[menteeHeaders[answerIndex]].append(answer)

                    if (menteeHeaders[answerIndex] in questions):
                        questions[menteeHeaders[answerIndex]] = list(
                            dict.fromkeys(questions[menteeHeaders[answerIndex]]))

                answerIndex += 1
            mentees.append(row)


# mentees = mentees[:5]
# mentors = mentors[:6]

scoreHeader = [""]
for mentee in mentees:
    scoreHeader.append(mentee[0])
scores.append(scoreHeader)

for mentor in mentors:
    scoreRow = [mentor[0]] + ([100] * len(mentees)) + \
        ([0] * (len(mentors) - len(mentees)))
    for mentee in mentees:
        for question in questions:
            if (question in menteeHeaders and question in mentorHeaders):
                menteeAnswer = mentee[menteeHeaders.index(question)]
                mentorAnswer = mentor[mentorHeaders.index(question)]
                if (question == "Q5"):
                    if (menteeAnswer == "No" and mentee[menteeHeaders.index("Q4")] == mentor[mentorHeaders.index("Q4")]):
                        scoreRow[scoreHeader.index(mentee[0])] += 5
                    elif (menteeAnswer == "Yes" and mentee[menteeHeaders.index("Q4")] == mentor[mentorHeaders.index("Q4")]):
                        scoreRow[scoreHeader.index(mentee[0])] -= 5

                    if (mentorAnswer == "No" and mentee[menteeHeaders.index("Q4")] == mentor[mentorHeaders.index("Q4")]):
                        scoreRow[scoreHeader.index(mentee[0])] += 5
                    elif (mentorAnswer == "Yes" and mentee[menteeHeaders.index("Q4")] == mentor[mentorHeaders.index("Q4")]):
                        scoreRow[scoreHeader.index(mentee[0])] -= 5

                elif (question == "Q7"):
                    if (menteeAnswer == "No" and mentor[mentorHeaders.index("Q6")] == "Yes"):
                        scoreRow[scoreHeader.index(mentee[0])] += 5
                    elif (menteeAnswer == "Yes" and mentor[mentorHeaders.index("Q6")] == "Yes"):
                        scoreRow[scoreHeader.index(mentee[0])] -= 7

                    if (mentorAnswer == "No" and mentee[menteeHeaders.index("Q6")] == "Yes"):
                        scoreRow[scoreHeader.index(mentee[0])] += 5
                    elif (mentorAnswer == "Yes" and mentee[menteeHeaders.index("Q6")] == "Yes"):
                        scoreRow[scoreHeader.index(mentee[0])] -= 7

                elif (question == "Q9"):
                    if (menteeAnswer == "No" and mentor[mentorHeaders.index("Q8")] == "Yes"):
                        scoreRow[scoreHeader.index(mentee[0])] += 5
                    elif (menteeAnswer == "Yes" and mentor[mentorHeaders.index("Q8")] == "Yes"):
                        scoreRow[scoreHeader.index(mentee[0])] -= 7

                    if (mentorAnswer == "No" and mentee[menteeHeaders.index("Q8")] == "Yes"):
                        scoreRow[scoreHeader.index(mentee[0])] += 5
                    elif (mentorAnswer == "Yes" and mentee[menteeHeaders.index("Q8")] == "Yes"):
                        scoreRow[scoreHeader.index(mentee[0])] -= 7

                elif (question == "Q11"):
                    if (menteeAnswer == "No" and mentor[mentorHeaders.index("Q10")] == "Yes"):
                        scoreRow[scoreHeader.index(mentee[0])] += 10
                    elif (menteeAnswer == "Yes" and mentor[mentorHeaders.index("Q10")] == "Yes"):
                        scoreRow[scoreHeader.index(mentee[0])] -= 8

                    if (mentorAnswer == "No" and mentee[menteeHeaders.index("Q10")] == "Yes"):
                        scoreRow[scoreHeader.index(mentee[0])] += 10
                    elif (mentorAnswer == "Yes" and mentee[menteeHeaders.index("Q10")] == "Yes"):
                        scoreRow[scoreHeader.index(mentee[0])] -= 8

                elif (question == "Q13" or question == "Q14" or question == "Q15" or question == "Q16"):
                    for answer in mentorAnswer:
                        if (answer in menteeAnswer):
                            scoreRow[scoreHeader.index(mentee[0])] -= 3
                elif (question == "Q3"):
                    for answer in mentorAnswer:
                        if (answer in menteeAnswer):
                            scoreRow[scoreHeader.index(mentee[0])] -= 8
                elif (menteeAnswer == mentorAnswer):
                    scoreRow[scoreHeader.index(mentee[0])] -= 3

    scores.append(scoreRow)


# Hungarian Algorithm Begins

# Calculate column minima
columnMinima = [''] + [200] * (len(scores)-1)

for scoreRow in scores:
    if (not scoreRow[0]):
        continue
    scoreIndex = 0
    for score in scoreRow:
        if (scoreIndex == 0):
            scoreIndex += 1
            continue
        if (columnMinima[scoreIndex] > score):
            columnMinima[scoreIndex] = score
        scoreIndex += 1

print("subtracting local minima")
# Subtract column minima
rowIndex = 0
for scoreRow in scores:
    if (rowIndex == 0):
        rowIndex += 1
        continue
    scoreIndex = 0
    for score in scoreRow:
        if (scoreIndex == 0):
            scoreIndex += 1
            continue
        scores[rowIndex][scoreIndex] -= columnMinima[scoreIndex]
        scoreIndex += 1
    rowIndex += 1


for scoreRow in scores:
    string = ""
    for item in scoreRow:
        string += "\t"+str(item)
    print(string)


while 1:
    print("---------start of while loop---------")

    print("finding and covering zeroes")
    # Find and cover zeroes

    assignedZeroes = [[ False for i in range(len(scores))] for j in range(len(scores))]
    crossedZeroes = [[ False for i in range(len(scores))] for j in range(len(scores))]

    markedRows = [''] + [False] * (len(scores)-1)
    markedColumns = [''] + [False] * (len(scores)-1)

    coveredRows = [''] + [False] * (len(scores)-1)
    coveredColumns = [''] + [False] * (len(scores)-1)

    print("assigning and crossing out zeroes")
    # assigning one row per column OR row, then crossing out the zeroes that share that column or row
    rowIndex = 0
    for scoreRow in scores:
        if (rowIndex == 0):
            rowIndex += 1
            continue
        zeroFound = False
        columnIndex = 0
        for score in scoreRow:
            if (columnIndex == 0):
                columnIndex += 1
                continue
            if (score == 0 and not crossedZeroes[rowIndex][columnIndex]):
                if (not zeroFound):
                    assignedZeroes[rowIndex][columnIndex] = True
                    zeroFound = True
                    tempRowIndex = 0
                    for tempRow in scores:
                        if (tempRowIndex == 0):
                            tempRowIndex += 1
                            continue
                        if (tempRow[columnIndex] == 0):
                            crossedZeroes[tempRowIndex][columnIndex] = True
                        tempRowIndex += 1
                elif (zeroFound):
                    crossedZeroes[rowIndex][columnIndex] = True
            columnIndex += 1
        rowIndex += 1

    def markColumns(ari):
        markedColumnIndex = 1
        while markedColumnIndex < len(markedColumns):
            if (scores[ari][markedColumnIndex] == 0 and not markedColumns[markedColumnIndex]):
                markedColumns[markedColumnIndex] = True
                # marking rows that have assignments in this column
                markedRowIndex = 1
                while markedRowIndex < len(markedRows):
                    if (assignedZeroes[markedRowIndex][markedColumnIndex] and not markedRows[markedRowIndex]):
                        markedRows[markedRowIndex] = True
                        markColumns(markedRowIndex)
                    markedRowIndex += 1
            markedColumnIndex += 1

    print("marking rows and columns")
    # marking each row with no assigned zeroes
    assignedRowIndex = 0
    for assignedRow in assignedZeroes:
        if (assignedRowIndex == 0):
            assignedRowIndex += 1
            continue
        if (True not in assignedRow):
            markedRows[assignedRowIndex] = True
            # marking columns that contain a zero in this row
            markColumns(assignedRowIndex)

        assignedRowIndex += 1

    print("covering rows and columns")
    # covering rows that are not marked, and columns that are
    coverCounter = 0

    markedColumnIndex = 1
    while markedColumnIndex < len(markedColumns):
        if (markedColumns[markedColumnIndex]):
            coveredColumns[markedColumnIndex] = True
            coverCounter += 1
        markedColumnIndex += 1

    markedRowIndex = 1
    while markedRowIndex < len(markedRows):
        if (not markedRows[markedRowIndex]):
            coveredRows[markedRowIndex] = True
            coverCounter += 1
        markedRowIndex += 1

    minUncovered = 999

    scoreRowIndex = 0
    for scoreRow in scores:
        scoreIndex = 0
        for score in scoreRow:
            if (isinstance(score, int) and score < minUncovered and not coveredColumns[scoreIndex] and not coveredRows[scoreRowIndex]):
                minUncovered = score
            scoreIndex += 1
        scoreRowIndex += 1


    scoreRowIndex = 0
    for scoreRow in scores:
        string = ""
        scoreColumnIndex = 0
        for item in scoreRow:
            if (not item and item != 0):
                item = "-"
            isRowCovered = "\033[94m" if coveredRows[scoreRowIndex] else ""
            isColumnCovered = "\033[96m" if coveredColumns[scoreColumnIndex] else ""
            isBothCovered = "\033[92m" if coveredColumns[scoreColumnIndex] and coveredRows[scoreRowIndex] else ""
            string += isRowCovered+isColumnCovered+isBothCovered+str(item)+"\033[0m"+"\t"
            scoreColumnIndex += 1
        print(string[:125]+"...")
        scoreRowIndex += 1

    print("coverCounter")
    print(coverCounter)
    if (coverCounter >= len(scores)-1):
        break

    scoreRowIndex = 0
    for scoreRow in scores:
        string = ""
        scoreColumnIndex = 0
        for item in scoreRow:
            if (isinstance(item, int) and coveredColumns[scoreColumnIndex] and coveredRows[scoreRowIndex]):
                scores[scoreRowIndex][scoreColumnIndex] += minUncovered
            elif (isinstance(item, int) and not coveredColumns[scoreColumnIndex] and not coveredRows[scoreRowIndex]):
                scores[scoreRowIndex][scoreColumnIndex] -= minUncovered
            scoreColumnIndex += 1
        scoreRowIndex += 1
    print("---------end of while loop---------")
    

print("\n---------final---------\n")

pairingString = ""

scoresIndex = 0
for scoreRow in scores:
    string = ""
    isFirst = True
    itemIndex = 0
    for item in scoreRow:
        colour = ""
        if (item == 0 and isFirst):
            isFirst = False
            blastIndex = scoresIndex
            while blastIndex < len(scores):
                scores[blastIndex][itemIndex] = 1
                blastIndex += 1
            colour = "\033[92m"
            if (len(scores[0]) <= itemIndex):
                scores[0].append("NO PARTNER")
            pairingString += scores[scoresIndex][0] + " - " + scores[0][itemIndex] + ", \n"
        elif (item == 0):
            scores[scoresIndex][itemIndex] = 1
        string += colour+str(item)+"\033[0m"+"\t"
        itemIndex += 1
    print(string)
    scoresIndex += 1

print(pairingString)

exit()