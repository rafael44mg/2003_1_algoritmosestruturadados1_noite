from Pessoa import Pessoa
#from Juridica import Juridica

class Fisica( Pessoa ):

    def __init__(self, nome, fone, cidade, cpf= None, empresa = None ):
        super().__init__( nome, fone, cidade)
        self.cpf = cpf
        self.empresa = empresa

    def imprimir(self):
        super().imprimir()
        print("CPF: ", self.cpf)
        print("Empresa: ", self.empresa.nome)

    def __str__(self):
        texto = "Empresa: " + self.nome
        texto += "\nFone: " + self.fone
        texto += "\nCNPJ: " + self.cnpj
        return texto
