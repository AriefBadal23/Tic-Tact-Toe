import socket
import pickle
import threading
from _thread import start_new_thread
class Server():
    def __init__(self):
        self.PORT = 12345
        self.IP_ADDRESS = socket.gethostbyname(socket.gethostname())
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.MAX_PLAYERS = 5
        self.connections = []
        self.amount_of_connections_list = []
        self.players_has_joined = []




    def broadcast(self, payload):
        """ Sends a message to all the connected clients """
        for socket in self.connections:
            if self.server_socket not in self.connections:
                payload = pickle.dumps(payload)
        print(f'Sending again payload: {payload}')
        socket.send(payload)

    def threaded_client(self, conn):
        """ When an session of the game is created start a new thread """
        while True:
            amount_of_connections = 0
            pass
            # create new code to handle received data ONLY
            

    def listen_to_connections(self):
        self.server_socket.bind((self.IP_ADDRESS, self.PORT))
        self.server_socket.listen(2)
        print("Server is listening for connections.....")


        while True:
            # Accept any new conenctions that has been made
            client_socket, client_address = self.server_socket.accept()
            print(f'{client_address} has connected')


            

            start_new_thread(self.threaded_client, (client_socket,))


game_server = Server()
game_server.listen_to_connections()
            
