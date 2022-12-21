import socket


class Server():
    def __init__(self):
        self.PORT = 12345
        self.IP_ADDRESS = socket.gethostbyname(socket.gethostname())
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.IP_ADDRESS, self.PORT))

        self.MAX_PLAYERS = 2
        self.connected_clients = []
    
    def broadcast(self):
        pass
    
    def get_post(self):
        pass

    def listen_to_connection(self):
        self.server_socket.listen()

        while True:
            print("Server is listening for connections.....")
            client_socket, client_address = self.server_socket.accept()
            self.connected_clients.append(client_socket)
            print(self.connected_clients)
            # print(f"You are connected with socket {client_socket}, {client_address}")
            client_socket.send("You are succesfully connected to the server!".encode())

            # self.server_socket.close()

    
    def send_pos(self):
        pass


    def threaded_client(self, id):
        """ When an session of the game is created start a new thread """



    def run_server(self):
        pass


s = Server()
s.listen_to_connection()
            
            
