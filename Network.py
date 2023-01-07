import socket
import threading
import pickle
from _thread import start_new_thread

class Network():
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IP_ADDRESS = socket.gethostbyname(socket.gethostname())
        self.PORT_NUMBER = 12345
        self.connection_established = False
        self.client_id = 0

    def connect_to_server(self):
        self.client_socket.connect((self.IP_ADDRESS, self.PORT_NUMBER))
        self.connection_established = True
