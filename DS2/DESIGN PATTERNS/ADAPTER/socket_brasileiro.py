from socket_europeu import SocketEuropeu

class SocketBrasileiro:
    def __init__(self, socket_europeu: SocketEuropeu) -> int:
        self.socket_europeu = socket_europeu
     
    def voltagem(self) -> int:
        return 110  
            
    def terra(self) -> int:
        return 0
    
    def neutro(self) -> int:
        return -1
    
    def fase(self) -> int:
        return 1