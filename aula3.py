class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularArea(self):
        return self.largura * self.altura

    def imprimir(self):
        print("largura: ", self.largura)
        print("altura: ", self.altura)
        print("area: ", self.calculararea() )
