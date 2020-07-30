import random

rand_num = random.randint(0, 10)
ques = int(input("Guess: "))

while ques != rand_num:
  if ques > rand_num:
    print("Too High")
    ques = int(input("Guess: "))
  elif ques < rand_num:
    print("Too Low")
    ques = int(input("Guess: "))
else:
  print("You got it correct!")