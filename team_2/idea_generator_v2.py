import random
import csv

option = raw_input("Would you like to [gen]erate a new idea or [add] to the existing set ?\n")

if option == 'gen':
    output = []
    with open('ideatank.csv', 'rb') as csvfile:
        ideareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in ideareader:
            output.append(random.choice(row))

    print "\n\n\nYou should make %s %s %s" % (output[0], output[1], output[2])

if option == 'add':
    answer1 = raw_input("Would like to add a game [type] or a game [genre]?\n")
    if answer1 != 'type' and answer1 != 'genre':
        print "Check input"
        exit()
    else:
        answer2 = raw_input("What {0}?\n".format(answer1))

    copy = []
    with open('ideatank.csv', 'rb') as csvfile:
        ideareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in ideareader:
            copy.append(row)

    if answer1 == 'type':
        copy[1].append(answer2)
    else:
        copy[0].append(answer2)

    with open('ideatank.csv', 'wb') as csvfile:
        ideawriter = csv.writer(csvfile, delimiter=',', quotechar='"')
        for row in copy:
            ideawriter.writerow(row)

