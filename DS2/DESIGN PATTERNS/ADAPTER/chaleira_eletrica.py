class ChaleiraEletrica:
    def __init__(self, socket) -> None:
        self.socket = socket
        
    def ferver(self):
        if (self.socket.voltagem() > 110):
            print("Chaleira explodiu")
        else:
            if(self.socket.fase() == 1 and self.socket.neutro() == -1):
                print("Chá das 17")
            else:
                print("Chaleira não liga")