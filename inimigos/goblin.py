from ..personagens import Inimigo 

class Goblin(Inimigo):

    def __init__(self):
        super().__init__("Goblin", vida=80, nivel=1)