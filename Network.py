import socket
import threading
import pickle

class Network():
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IP_ADDRESS = socket.gethostbyname(socket.gethostname())
        self.PORT_NUMBER = 12345
        self.client_id = 0

    def connect_to_server(self):
        self.client_socket.connect((self.IP_ADDRESS, self.PORT_NUMBER))
        message = self.client_socket.recv(1024)
        print(message.decode())

    def get_pos(self):
        pass

    def get_players(self):
        player = self.client_socket.recv(1024)
        connected_players = pickle.loads(player)
        # print(len(connected_players))
        return connected_players
        



    def send_pos(self):
        pass

    
