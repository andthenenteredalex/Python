""" OSI model quiz written in Python 2.7

    Copyright Alex Clark November 2017
    Let me know if you have any questions.

    future imporovements:
            print if score is low you need to improve, is score is high congratulations.
            allow for error tolerance for fat fingering and different ways of saying it
            require definitions and search the raw input of an answer for keywords indicating it's correct
    """
import random

number = range(1,8)
number = random.sample(number, 7)
score = 0
layers = ["physical", "data link", "network", "transport", "session", "presentation", "application" ]

for item in number:
    if item == 1:
        print "What is the 1st layer of the OSI model?"
    elif item == 2:
        print "What is the 2nd layer of the OSI model?"
    elif item == 3:
    	  print "What is the 3rd later of the OSI model?"
    else:
        print "What is the", item, "th layer of the OSI model?"
    user_input = raw_input()
    answer = item - 1
    if user_input == layers[answer]:
    	score = score + 1
    	print "congratulations!"
    else:
    	print "learn your stuff!"

print "Your score is", score, "out of a possible 7."
