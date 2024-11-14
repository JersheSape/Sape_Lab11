loop = True
grades = []
gradeamount = 0

while loop == True:
    gradeinput = input("Enter grade or Type(done): ")
    if(gradeinput.isdigit()):
        gradeinput = int(gradeinput)
        if(gradeinput >= 40 and gradeinput <= 100):
            gradeamount += 1
            grades.append(gradeinput)
        else:
            print("Invalid data, please try again")
            break

    elif(gradeinput==str("done").lower()):
        loop = False
    else:
        print("invalid input, please try again")
        break
else:
    sum = sum(grades)
    finalgrade = sum/gradeamount
    passing = 0
    print("Average Grade:", finalgrade)
    for gradeinput in grades:
        if(gradeinput >= 75):
            passing += 1

    print("Passed subjects:", passing)
    print("Passing Percentage:", (passing / len(grades)) * 100,"%")
    print("Grade:", grades)