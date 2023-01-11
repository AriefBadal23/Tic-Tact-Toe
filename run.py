""" Main file for the entire Game
    It is required to install pygame to run the game.
    Only if this script is used the game will run
 """
# from Network import Network
from game import Game
if __name__ == "__main__":
    app = Game()
    app.run()