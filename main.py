import random
from art import logo



def guessing_number():


    number  = random.randint(0,100)

    return number

def guess():

    
    life = 5
    in_Game = True
    
    while  in_Game:

        answer = guessing_number()

        print(answer)
        
        user_answer = int(input("Please try to guess the number: "))

       
        if answer == user_answer:

            print(f"You win , the number was {answer}")
            break
        
        elif  user_answer > answer:

            print("Too high, try again")
            life -= 1
        
        elif user_answer < answer:

            print("Too low, try again")
            life -= 1
                
            
        if life == 0:

                print(f"Game over! The number was {answer}")
                in_Game = False
        


guess()

