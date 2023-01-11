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
        self.players = []
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
            data = conn.recv(1024)
            if data:
                # print(pickle.loads(data))
                print((f'Received: {str(pickle.loads(data))}'))
                self.broadcast(pickle.dumps(data))
            else:
                self.connections.remove(conn)
                self.server_socket.close()


    def listen_to_connections(self):
        self.server_socket.bind((self.IP_ADDRESS, self.PORT))
        self.server_socket.listen(2)
        print("Server is listening for connections.....")


        while True:
            # Accept any new conenctions that has been made
            client_socket, client_address = self.server_socket.accept()
            print(f'{client_address} has connected')
            start_new_thread(self.receive_data, (client_socket,))
            amount_of_connections += 1
            self.players.append(amount_of_connections)
            print(f'{amount_of_connections} connections has been made')
            client_socket.send(str(self.players).encode())

            if len(self.players) == 1:
                player_1_joined = {
                    "player": self.players[0],
                    "CAN_PLAY": True
                }
                self.players_has_joined.append(player_1_joined)


            elif len(self.players) == 2:
                player_2_joined = {
                    "player": self.players[1],
                    "CAN_PLAY": False
                }
                self.players_has_joined.append(player_2_joined)
            

            start_new_thread(self.threaded_client, (client_socket,))

            print(f'Joined: {self.players_has_joined}')
            client_socket.send(pickle.dumps(self.players_has_joined))
            

game_server = Server()
game_server.listen_to_connections()
            
