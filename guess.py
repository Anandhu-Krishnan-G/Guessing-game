import random
guessing_number=random.randint(1,100)
count=0
limit=3
print("There are only 3 chances for guessing the number")
print("Plz enter a number between 1 and 100")
while(count<limit):
    num=int(input(f"Enter you {count+1} guessss  "))
    if(num==guessing_number):
        print("Congratz you win the game")
        break
    else:
        print("wrong guess")
    count=count+1
print("Game ended")
