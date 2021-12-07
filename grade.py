subjectNum = 4
countGrade = 0
passGrade = 0
failGrade = 0

for i in range(subjectNum):
    subjectName = str(input("Subject name: "))
    subjectGrade = int(input(subjectName + " grade: "))
    countGrade += subjectGrade

    if subjectGrade < 60:
        failGrade += 1
    else:
        passGrade += 1

averageGrade = countGrade / subjectNum

if passGrade > failGrade:
    print("You PASSED with the average " + str(averageGrade))
else:
    print("You FAILED with the average " + str(averageGrade))
