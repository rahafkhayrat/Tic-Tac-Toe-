class player:
    def __init__(self):
        self.name=""
        self.symbol=""
    def choose_name(self):
        while True:
          
          name=input("enter your name(letters only):")
          if name.isalpha():
              self.name=name
              break
          print("invaild name . please use letters only.")
    def choose_symbol(self):
        while True:
            symbol=input(f"{self.name},choose your symbol (a single lettre):")
            if symbol.isalpha() and len(symbol)==1:
                self.symbol=symbol.upper()  
                break
            print("invalid symbol , choose single letter")

class menu:
    def display_main_menu(self):
        print("Welcome to my x-o game")
        print("1.start game")
        print("2. quit game")
        choice=input("enter your choice 1 or 2 :")
        return choice
    def display_endgame_menu(self):
        menu_text='''
     Game Over!
     1. restart game
     2. quit game
     Enter your choice 1 or 2'''
        choice=input(menu_text)
        return choice
    
class board:
    def __init__(self):
        self.board=[str(i) for i in range(1,10)]
    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            if i <6:
                print("-"*5)
    def update_board(self,choice,symbol):
        if self.is_valid_move(choice):
            self.board[choice-1]=symbol 
            return True
        return False    
    def is_valid_move(self,choice):
        return self.board[choice-1].isdigit()
    def reset_board(self):
        self.board=[str(i) for i in range(1,10)]

class game:
    def __init__(self):
        self.players=[player(),player()]
        self.board=board()
        self.menu=menu()
        self.current_player_index=0
    def start_game(self):
        choice= self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game() 
        else:
            self.quit_game()
    def setup_players(self):
        for number, player in enumerate (self.players,start=1):
            print(f"player{number},enter your details")
            player.choose_name()
            player.choose_symbol()
            print("-"*20)
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice=self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()   
                    break 
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index=0
        self.play_game()

    def check_win(self):
        win_combinations=[
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
    ]
        for combo in win_combinations:
            if(self.board.board[combo[0]]== self.board.board[combo[1]]==self.board.board[combo[2]] ):
                print("WIN!!!")

                return True
            return False
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)          
    def play_turn(self):
        player=self.players[self.current_player_index] 
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})") 
        while True:          
          try:
            cell_choice=int(input("choose a cell (1-9):"))
            if 1<= cell_choice <=9 and self.board.update_board(cell_choice , player.symbol):
                break
            else:
                print("invalid move , try again")
          except ValueError:
            print("please enter a number between 1 and 9.") 
        self.switch_player()       
    def switch_player(self):
        self.current_player_index= 1 - self.current_player_index
    def quit_game(self):
        print("thank you for playing")   
Game=game() 
Game.start_game()          

              


        
            
        
        



