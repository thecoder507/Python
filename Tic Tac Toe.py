import Players 
class Tic_Tac_Toe:
    
    def draw_board(self, player1, player2):
        spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9" }
        tracking_spots = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " " }
        
        for i in range(1,11):

            board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
                    f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
                    f"|{spots[7]}|{spots[8]}|{spots[9]}|\n")
            print(board)

            results = self.winner_cheker(spots, player1, player2)
            if results == True:
                break

            if i == 10:
                print("El juego a quedado en un empate")
                print(board)

            elif i % 2 == 0:

                try:
                    box = int(player1.choose_box())
                except ValueError:
                    print("upss, ese valor no se presenta en la tabla")
                    box = int(player2.choose_box())

                while box not in spots.keys():
                    print("Te fuiste, ese valor no esta en la tabla")
                    box = int(player1.choose_box())


                while tracking_spots[box] != " ":
                    print("This spot is already taken, choose a empty one")
                    box = int(player1.choose_box())
                    
                spots[box] = player1.team
                tracking_spots[box] = player1.team

            else:

                try:
                    box = int(player2.choose_box())
                except ValueError:
                    print("upss, ese valor no se presenta en la tabla")
                    box = int(player2.choose_box())

                while box not in spots.keys():
                    print("Te fuiste, ese valor no esta en la tabla")
                    box = int(player2.choose_box())

                while tracking_spots[box] != " ":
                    print("This spot is already taken, choose a empty one")
                    box = int(player2.choose_box())

                spots[box] = player2.team
                tracking_spots[box] = player2.team

                



    def winner_cheker(self, board, player1, player2):
        
        for i in range(1, 8, 3):
             
            if board[i] == board[i+1] == board[i+2]:
                if player1.team == board[1]:
                    print(f"{player1.name} es el ganador!!!")
                    return True
                
                elif player2.team == board[1]:
                    print(f"{player2.name} es el ganador!!!!")
                    return True
                
                else:
                    return False
                 
        for i in range(1, 4):

             if board[i] == board[i+3] == board[i+6]:
             
                if player1.team == board[1]:
                    print(f"{player1.name} es el ganador!!!")
                    return True
                
                elif player2.team == board[1]:
                    print(f"{player2.name} es el ganador!!!")
                    return True 
                
                else: 
                    return False
                
        
        if board[1] == board[5] == board[9] or board[3] == board[5] == board[7]:

            if player1.team == board[1]:
                print(f"{player1.name} es el ganador!!!")
                return True

            elif player2.team == board[1]:
                print(f"{player2.name} es el ganador!!!")
                return True
            
            else:
                return False


game_1 = Tic_Tac_Toe()
game_1.draw_board(Players.player1, Players.player2)





