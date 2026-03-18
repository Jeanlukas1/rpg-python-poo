from personagem import Personagem
class Heroi(Personagem):

    def __init__(self, nome):
        super().__init__(nome, vida=100, nivel=1)

    def subir_nivel(self):
        self._nivel += 1
        self._vida += 20
        print(f"{self.nome} subiu para o nível {self._nivel}!")