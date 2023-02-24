from abc import ABC 

class Jogo(ABC):
    def __init__(self, quantidade_de_jogadores) -> None:
        self.quantidade_de_jogadores = quantidade_de_jogadores
        self.jogador_corrente = 0
        
    def comecar_rodada(self) -> None:
        self.iniciar_jogo()
        while not self.tem_vencedor():
            self.alternar()
        print(f"Jogador {self.jogador_vencedor()} venceu!")
        
    def iniciar_jogo(self):
        pass
    
    def tem_vencedor(self) -> bool:
        pass
    
    def alternar(self) -> None:
        pass
    
    def jogador_vencedor(self) -> int:
        pass
        
    
    