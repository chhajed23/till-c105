import random
print("Number Guessing Game")
chance=0
number=random.randint(1,9)
while chance<=5 :
    g1=int(input(("Guess a number between (1 to 9) : ")))

    if number==g1:
       print("You Have Won")
       break
    elif g1>number:
        print("Your guess was too high: guess a lower number than: ",g1) 
    else:
        print("Your guess was too low: guess a higher number than: ",g1)
    chance+=1
if chance>=5 :
    print("You lost the Game. The number was: ",number)




