import random 

def guess(x):
    random_num = random.randint(1,x)
    guess =0
    while guess != random_num:
        guess = int(input(f"enter a random num between 1 & {x} "))
        if guess < random_num:
              print("too low")
        elif guess > random_num:
              print("to high")    
        else:
              break
            
    print("you got it" )      
      
        
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


computer_guess(10)



    