from animalabc import Animal

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca = raca

    def setRaca(self, raca):
        self.__raca = raca

    def getRaca(self):
        return self.__raca

    def mostrar(self):
        return f"O nome do Gato é: {self.getNome()}, Idade: {self.getIdade()}, e raça: {self.getRaca()}"
