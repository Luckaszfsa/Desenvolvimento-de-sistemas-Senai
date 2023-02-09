from socket_europeu import SocketEuropeu
from socket_brasileiro import SocketBrasileiro
from chaleira_eletrica import ChaleiraEletrica 

socket_europeu = SocketEuropeu()
socket_brasileiro = SocketBrasileiro(socket_europeu)
chaleira_eletrica = ChaleiraEletrica(socket_brasileiro)
chaleira_eletrica.ferver()