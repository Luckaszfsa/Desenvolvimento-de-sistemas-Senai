import math
class Quadrado:
    def __init__(self, lado: int) -> None:
        self.lado = lado
        
    def calcular_area(self) -> int:
        return self.lado ** 2


def calcular_area(forma):
    return forma.calcular_area()
def area(self):
    return math.pi * self.raio ** 2
       
class QuadradoParaRaio:
    def __init__(self, quadrado):
        self.raio = quadrado.lado * math.sqrt(2) / 2

quadrado = Quadrado(10)
quadrado_para_raio = QuadradoParaRaio(quadrado)
print(f"Resultado do calculo da Area: {calcular_area:(quadrado_para_raio)}")