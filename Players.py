class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def choose_box(self):
        position = input(f"{self.name}, seleccione donde desea colocar su {self.team}: ")
        return position

 
def team_selection(player1, player2):
    teams = ["x", "0"]
    selected_teams = {}
    t_player1 = input(f"{n_player1}, Seleccione su equipo{teams}: ")
    while t_player1 not in teams:
            t_player1 = input(f"Seleccione su equipo, que se encuetre aqui: {teams}")
    selected_teams[player1] = t_player1
    teams.remove(t_player1)
    selected_teams[player2] = teams[0] 
    print(f"{n_player1} es {selected_teams[player1]} y {n_player2} es {selected_teams[player2]}" )
    return selected_teams

n_player1 = input("Jugador 1, ingrese su nombre: ")
n_player2 = input("Jugador 2, ingrese su nombre: ")
players_teams = team_selection(n_player1, n_player2)
player1 = Player(n_player1,players_teams[n_player1])
player2 = Player(n_player2,players_teams[n_player2])



