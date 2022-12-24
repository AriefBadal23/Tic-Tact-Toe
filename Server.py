import socket
import os


class Server():
    def __init__(self):
        self.PORT = 12345
        self.IP_ADDRESS = socket.gethostbyname(socket.gethostname())
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected_clients = []
        self.players = []


    def broadcast(self, payload):
        for socket in self.connected_clients:
            socket.send(payload.encode("utf-8"))
    
    def get_post(self):
        pass
    
    def listen_to_connection(self):
        self.server_socket.bind((self.IP_ADDRESS, self.PORT))
        self.server_socket.listen(2)
        print("Server is listening for connections.....")


        amount_connections = 0
        while True:
            client_socket, client_address = self.server_socket.accept()
            amount_connections +=1

            client_socket.send(f"{client_address} has joined. \n {amount_connections} players has connected to the game".encode("utf-8"))
 
    
    def send_pos(self):
        pass


    def threaded_client(self, id):
        """ When an session of the game is created start a new thread """
        pass


    def run_server(self):
        try:
            self.listen_to_connection()
        except:
            print("Failed to strart the server")


game_server = Server()
game_server.run_server()
            
            
