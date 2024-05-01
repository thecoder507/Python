import Players 
class Tic_Tac_Toe:

    def draw_board(self, player1, player2):
        spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9" }
        tracking_spots = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " " }
        
        for i in range(1,10):
            board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
            f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
            f"|{spots[7]}|{spots[8]}|{spots[9]}|\n")
            print(board)
            if i % 2 == 0:
                box = int(player1.choose_box())
                while tracking_spots[box] != " ":
                    print("This spot is already taken, choose a empty one")
                    box = int(player1.choose_box())
                spots[box] = player1.team
                tracking_spots[box] = player1.team
            else:
                box = int(player2.choose_box())
                while tracking_spots[box] != " ":
                    print("This spot is already taken, choose a empty one")
                    box = int(player2.choose_box())
                spots[box] = player2.team
                tracking_spots[box] = player2.team
                print(board)


game_1 = Tic_Tac_Toe()
game_1.draw_board(Players.player1, Players.player2)





