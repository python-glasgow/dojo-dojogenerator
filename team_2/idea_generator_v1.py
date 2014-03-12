import random

list1 = ["zombie", "vampire", "pirate", "vigalante", "superhero", "ninja", "samurai", "programmer", "warhero"]
list2 = ["hangman", "sudoku", "tic tac toe", "battleship", "crossword", "checkers", "ludo"]
list3 = ["with dice", "in 3D", "with cards", "for money", "using python"]

output = []

output.append(random.choice(list1))
output.append(random.choice(list2))
output.append(random.choice(list3))

print "You should make %s %s %s" % (output[0], output[1], output[2])
