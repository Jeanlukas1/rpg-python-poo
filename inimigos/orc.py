from ..personagens import Inimigo
class Orc(Inimigo):

    def __init__(self):
        super().__init__("Orc", vida=200, nivel=2)