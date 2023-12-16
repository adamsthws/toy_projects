#!/usr/bin/env python

# Simple pet project to become more familiar with Python. 
# Imitates the classic Magic 8 Ball.
# Randomly provides an answer to some arbitrary question. 

import random

#name = input("What is your name? : ")
name = "Adam"
#question = input("Hi "+ name + ", what is your question?")
question = "Will I win the lotto?"

random_number = random.randint(1, 9)

if random_number == 0:
  answer = "Yes - definitely."
elif random_number == 1:
  answer = "It is decidedly so."
elif random_number == 2:
  answer = "Without a doubt."
elif random_number == 3:
  answer = "Reply hazy, try again."
elif random_number == 4:
  answer = "Ask again later."
elif random_number == 5:
  answer = "Better not tell you now."
elif random_number == 6:
  answer = "My sources say no."
elif random_number == 7:
  answer = "Outlook not so good."
elif random_number == 8:
  answer = "Very doubtful."
else:
  answer = "Error"

print(name + " asks: " + question)
print("Magic 80Ball's answer: " + answer)
