#This is a Good Match Program by Sula Mabuza submitted for use by Derivco (Pty) Ltd
import csv
import operator
import time

def sumLists(value_countList):
    #this function does the computation to check if two people are a match or not
    sum = 0
    sumList = []
    global toworkwith
    global goodMatch
    toworkwith = sumList
    global percent_str
    while(len(value_countList)> 1):
        sum = value_countList[0] + value_countList[-1]
        sumList.append(sum)
        #print(sumList)
        if len(sumList) == 3 or len(sumList) == 4:
            toworkwith = sumList

        value_countList.pop(0)
        value_countList.pop(-1)

    if len(value_countList) == 1:
        sumList.append(value_countList[0])
    #print(sumList)
    #print(len(toworkwith))
    if len(toworkwith) == 3:
        answer = toworkwith[0] + toworkwith[2]
        answerList = []
        if answer >= 10:
            for digit in str(answer):
                answerList.append(int(digit))

        else:
            answerList.append(answer)
        answerList.append(toworkwith[1])
        percent_str = str(answerList[0] + answerList[-1]) + str(answerList[1])

        if int(percent_str) > 100:
            dummy_list = []
            for digit in percent_str:
                dummy_list.append(int(digit))
            percent_str = str(dummy_list[0] + dummy_list[-1]) + str(dummy_list[1])

        if int(percent_str) >= 80:
            goodMatch = "Good Match"
            print(f'{name_one} matches {name_two} {percent_str}%, good match')
        else:
            goodMatch = ""
            print(f'{name_one} matches {name_two} {percent_str}%')
    if len(toworkwith) == 4:
        answer = toworkwith[0] + toworkwith[-1]
        answer2 = toworkwith[1] + toworkwith[-2]
        answerList= []
        if answer >= 10:
            for digit in str(answer):
                answerList.append(int(digit))

        else:
            answerList.append(answer)

        if answer2 >= 10:
            for digit in str(answer2):
                answerList.append(int(digit))

        else:
            answerList.append(answer2)

        percent_str = str(answerList[0] + answerList[-1]) + str(answerList[1])

        if int(percent_str) > 100:
            dummy_list = []
            for digit in percent_str:
                dummy_list.append(int(digit))
            percent_str = str(dummy_list[0] + dummy_list[-1]) + str(dummy_list[1])

        if int(percent_str) >= 80:
            goodMatch = "Good Match"
            print(f'{name_one} matches {name_two} {percent_str}%, good match')

        else:
            goodMatch = ''
            print(f'{name_one} matches {name_two} {percent_str}%')


    return sumList

def verify_names(firstname, secondname):
    # this function checks first if the names inserted are alphabets before calling the function for computation
    global name_one
    global name_two
    global name1
    global name2
    name1 = firstname
    name2 = secondname
    name_one = firstname
    name_two = secondname
    bool = 0
    for character in name1 and name2:
        if not character.isalpha():
            print("names are invalid, please check, should be alphabets")
        else:
            bool = 1
    if bool:
        twoStrings()

def twoStrings():
    #this function breaks down the name strings into character lists before doing the cancellation that gives int values
    print(f'Hello {name1} and {name2}')
    default_word = 'matches'.upper()
    name2_word = name2.upper()
    default_wordList = list(default_word)
    default_string = name1 + 'matches' + name2
    toCompareString = default_string.upper()
    name1List = list(name1.upper())
    name2List = list(name2.upper())
    compareList = list(toCompareString.upper())
    value_countList = [0]

    #start with the first string = Jack
    for i in range(0, len(name1List)):
        value_countList.append(toCompareString.count(name1List[i]))
        toCompareString = toCompareString.replace(name1List[i], '')
        default_word = default_word.replace(name1List[i], '')
        name2_word = name2_word.replace(name1List[i], '')
        default_wordList = list(default_word)
        name2List = list(name2_word)

    value_countList.remove(value_countList[0])

    for i in range(0, len(default_wordList)):
        value_countList.append(toCompareString.count(default_wordList[i]))
        toCompareString = toCompareString.replace(default_wordList[i], '')
        name2_word = name2_word.replace(default_wordList[i], '')
        name2List = list(name2_word)

    for i in range(0, len(name2List)-1):
        value_countList.append(toCompareString.count(name2List[i]))
        toCompareString = toCompareString.replace(name2List[i], '')

    sumList = sumLists(value_countList)
    #sumLists(sumList)
    for i in range (0, 1):
        sumLists(sumList)


def create_csvFile():
    #this function creates a csv file containing the names of the people that will be matched
    f = open("people.csv", "w", newline="")
    writer = csv.writer(f)
    first_person = ("Kimberly", "f")
    writer.writerow(first_person)
    second_person = ("Jason", "m")
    writer.writerow(second_person)
    third_person = ("Billy", "m")
    writer.writerow(third_person)
    fourth_person = ("Trini", "f")
    writer.writerow(fourth_person)
    fifth_person = ("Tommy", "m")
    writer.writerow(fifth_person)
    sixth_person = ("Zack", "m")
    writer.writerow(sixth_person)
    seventh_person = ("Billy", "f")
    writer.writerow(seventh_person)
    eighth_person = ("Jason", "m")
    writer.writerow(eighth_person)

    #done writing
    f.close()

def csv_sortFile():
    # this functions and splits the names in the csv file of people according to gender and stores in two lists
    # it then calls the verify function which checks if they are valid before doing computations
    # results are then stored in temporary csv to allow sorting according to percent and alphabetic order
    # results are then produced in an output.txt file
    f = open("people.csv", 'r')
    textfile = open("output_temporary.csv", "w", newline='')
    #new_file = open("")
    global maleList
    global femaleList
    maleList = []
    femaleList = []
    new_csv = csv.reader(f, delimiter=',')
    sort = sorted(new_csv, key=operator.itemgetter(1))
    for eachline in sort:
        if "m" in eachline:
            maleList.append(eachline[0])
        elif "f" in eachline:
            femaleList.append(eachline[0])
    print(maleList)
    print(femaleList)
    for malename in maleList:
        for femalename in femaleList:
            verify_names(malename, femalename)
            textfile.write(f'{malename} matches {femalename}, {percent_str}, {goodMatch}\n')

    f.close()
    textfile.close()

    outputtextfile = open("output_temporary.csv", 'r', newline='')
    new_csv_txt = csv.reader(outputtextfile, delimiter=',')
    sort_txt = sorted(new_csv_txt, key=operator.itemgetter(1, 0), reverse=True)
    outputfile = open("output.txt", "w", newline='')
    for eachline in sort_txt:
        outputfile.write(str(eachline[0]) +','+ str(eachline[1]) + ',' +str(eachline[2]) +'\n')
    outputfile.close()
    outputtextfile.close()
#######################################################Optional Section#################################################
def calculate_executionTime():
    # this stores the execution time in a log.txt file.
    global begin
    global end
    f = open("log.txt", "w")
    f.write(f'Total runtime of the program is {end - begin}')

    f.close()

###################################################End of Optional Section##############################################

if __name__ == '__main__':
    begin = time.time() #start timer for execution time
    create_csvFile()
    verify_names('Jack', 'Jill')
    csv_sortFile()
    end = time.time() #program done, stop timer
    calculate_executionTime()



