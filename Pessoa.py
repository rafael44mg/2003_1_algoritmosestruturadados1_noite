class Pessoa:
    def __init__(self, codigo, nome, end, fone):
        self.codigo = codigo
        self.nome = nome
        self.edereco = end
        self.fone = fone

    def imprimir(self):
        print("Nome: ", self.nome)
        print("End: ", self.edereco)
