""" Main file for the entire Game
    It is required to install pygame to run the game.
    Only if this script is used the game will run
 """
from game import Game
from Network import Network

if __name__ == "__main__":
    tic_tact_toe_network = Network()
    app = Game()
    tic_tact_toe_network.connect_to_server()
    player = tic_tact_toe_network.get_players()
    app.set_player(player)
   
    app.run()
