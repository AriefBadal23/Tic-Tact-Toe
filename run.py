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
    # Gets the connected players
    player = tic_tact_toe_network.get_players()

    # Add the player to playerslist
    joined_player = app.set_player(player)

    # Gets the joined player with the connection that has been made
    app.get_player(joined_player)

    # # Retrieve the players positions
    positions = app.player_positions
    app.get_positions(joined_player,positions)   
    app.run()
