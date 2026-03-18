class Personagem:

    def __init__(self, nome: str, vida: int, nivel: int):
        self._nome = nome
        self._vida = vida
        self._nivel = nivel

    @property
    def nome(self):
        return self._nome

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        else:
            self._vida = valor

    @property
    def nivel(self):
        return self._nivel

    def atacar(self, alvo):
        dano = self._nivel * 10
        alvo.vida -= dano

        print(f"{self.nome} atacou {alvo.nome}")
        print(f"Dano causado: {dano}")