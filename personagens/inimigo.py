from personagens.personagem import Personagem
class Inimigo(Personagem):

    def __init__(self, nome, vida, nivel):
        super().__init__(nome, vida, nivel)