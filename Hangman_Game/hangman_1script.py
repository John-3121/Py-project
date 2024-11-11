import random 
import string
words = ["dog","cabinet","python","sky","gold","racoon","headphone","shirt"]

lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }
    
def   get_valid_word(words):
    
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word .upper()   

#print(get_valid_word(words))

def hangman():
  
        
   word = get_valid_word(words)
   word_letters = set(word)
   alphabet = set(string.ascii_uppercase)
   used_letters = set()
   tries = 5
   
   while len(word_letters) > 0 and tries> 0:
       
       
    print("this are the letter u have alreday used "  + "-"
    .join(used_letters) )
    
    right_guess = [letter if letter in used_letters else "-" for letter in word]
    print(lives_visual_dict[tries])
    print("Current Word:", " ".join(right_guess))
    
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
                

            else:
                tries = tries - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

            
    elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')
            

    else:
            print('\nThat is not a valid ')
   
   if tries == 0:
       print("Game over you died ):")
       print(lives_visual_dict[tries])
   print("Congrats you guess the word"," ".join(word) )
if __name__ == "__main__"  :
    hangman()
    
    