import socket
import pickle
class Server():
    def __init__(self):
        self.PORT = 12345
        self.IP_ADDRESS = socket.gethostbyname(socket.gethostname())
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def broadcast(self, payload):
        """ Sends a message to all the connected clients """
        for socket in self.connected_clients:
            socket.send(payload.encode("utf-8"))
    
    def get_post(self):
        pass
    
    def listen_to_connection(self):
        players = []
        self.server_socket.bind((self.IP_ADDRESS, self.PORT))
        self.server_socket.listen(2)
        print("Server is listening for connections.....")


        amount_connections = 0
        connected_clients = []
        while True:
            # Accept any new conenctions that has been made
            client_socket, client_address = self.server_socket.accept()
            connected_clients.append(client_socket)
            # increment amount of connections
            amount_connections +=1

            # add to players list
            players.append(amount_connections)

            # Let the client know how many plays joined the game
            client_socket.send(f"{client_address} has joined.")
            send_players = pickle.dumps(players)
            client_socket.send(send_players)

    
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
            
            
