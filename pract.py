#import random
#random_number = random.randint(1,10)
#guess = input("pick a number from 1 to 10: ")
#guess = int(guess)
#if guess == random_number:
    #print("you win!")
#elif guess < random_number:
    #print("Too low!")
#else:
    #print("Too high")
#print(random_number)            


#import random
#random_number = random.randint(1,10)
#guess = None
#while guess != random_number:
    #guess = input("pick a number from 1 to 10: ")
    #guess = int(guess)
    #if guess < random_number:
        #print("Too low!")
    #elif guess > random_number:
        #print("Too high")
    #else:
         #print("you won!!!")   
#print(random_number) 


import random
random_number = random.randint(1,10)
guess = None
while True:
    guess = input("pick a number from 1 to 10: ")
    guess = int(guess)
    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high")
    else:
        print("you won!!!")  
        play_again = input("do you wanna play again?(Y/N") 
        if play_again == "Y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("thank you for playing  U0001f600")
            break    

print(random_number) 