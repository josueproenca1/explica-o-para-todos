from animalabc import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte = porte

    def setPorte(self, porte):
        self.__porte = porte

    def getPorte(self):
        return self.__porte

    def mostrar(self):
        return f"O nome do cachorro é: {self.getNome()}, Idade: {self.getIdade()}, e porte: {self.getPorte()}"
