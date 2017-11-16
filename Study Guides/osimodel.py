""" OSI model quiz written in Python 2.7
    
    Copyright Alex Clark November 2017
    Let me know if you have any questions.
    
    imporovements: remove repetition of numbers in random
                print if score is low you need to improve, is score is high congratulations.
    """
from random import randint

guessed_array = []
woof = 0
score = 0
array = ["physical", "data link", "network", "transport", "session", "presentation", "application" ]
while woof <= 6:
    number = (randint(0,6) + 1)
    answer = number - 1 
    correct_answer = array[answer]
    if number == 1:
        print "What is the 1st layer of the OSI model?"
    elif number == 2:
        print "What is the 2nd layer of the OSI model?"
    elif number == 3:
    	  print "What is the 3rd later of the OSI model?"
    else:
        print "What is the", number, "th layer of the OSI model?"
    user_input = raw_input()
    if user_input == array[answer]:
    	score = score + 1
    	print "congratulations!"
    else:
    	print "learn your stuff!"
    woof = woof + 1

print "Your score is", score, "out of a possible 7."
