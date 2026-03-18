from personagens.heroi import Heroi
from inimigos.orc import Orc
class Combate:

    def iniciar(self, heroi, inimigo):

        print("⚔️ Combate iniciado!")

        while heroi.vida > 0 and inimigo.vida > 0:

            heroi.atacar(inimigo)

            if inimigo.vida <= 0:
                print(f"{inimigo.nome} foi derrotado!")
                heroi.subir_nivel()
                break

            inimigo.atacar(heroi)

            if heroi.vida <= 0:
                print("O herói foi derrotado!")
                
# Apenas o nome, pois vida e nível já estão definidos na classe!
meu_heroi = Heroi("Aragorn")
meu_inimigo = Orc()

# O resto do código de combate continua igual
combate = Combate()
combate.iniciar(meu_heroi, meu_inimigo)