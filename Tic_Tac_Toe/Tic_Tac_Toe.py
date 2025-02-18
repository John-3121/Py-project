import math 
import random
import time

class Player:
    def __init__(self,letter):
        #letter is X or O
        self.letter = letter 
    
    def get_move(self,game):
        pass
        

class randomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        square  = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        valid_square =False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s  turn. input move  (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("invalid square")
                
                        
        return val       
                
        
      
class Tic_tac_toe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner= None
    
    def print_board(self):
        #this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(" | " + " | ".join(row) + " | ")
        
        
    @staticmethod
    def print_board_nums():
       number_board = [[Str(i) for i in range (j*3 ,  (j+1)*3)] for j in range(3)]
       for row in number_board:
           print(" | " + " | ".join(row) + " | ")
           
    def available_moves(self):
       return [i for i ,spot in enumerate(self.board) if spot == " "]
   
    def empty_squares(self):
       return " " in self.board     
       
    def num_empty_squares(self):
       return self.board.count(" ")
   
    def make_move(self,square,letter):
       if self.board[square] == " ":
           self.board[square] = letter
           if self.winner(square,letter):
             self.current_winner  = letter
           return True
       return False
     
    def winner(self,square,letter):
        row_ind = square // 3
        row =  self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
            
            
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False    
            
        
        
        
def play(game,x_player,o_player,print_game = True):
    if print_game:
        game.print_board_nums
     
    letter = "X"   
    
    while game.empty_squares():
        if letter  == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        
        if game.make_move(square,letter):
            if print_game:
                print(letter + f"make a move to square {square}")
                game.print_board()
                print("")
            if game.current_winner:
                if print_game:
                    print(letter + "wins");
                return letter
                    
            letter = "O" if letter =="X" else "X"
        time.sleep(0.8)   
    if print_game:
            print("its a tie");
                


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = randomComputerPlayer('O')
    t = Tic_tac_toe()
    play(t, x_player, o_player, print_game=True)
