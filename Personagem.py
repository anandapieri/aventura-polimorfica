import random
from Entidade import Entidade

class Personagem(Entidade):
    def usar_habilidade_especial(self):
        dano_especial = random.randint(self.forca + 1, self.forca*2)
        print(f'{self.nome} usa sua habilidade especial para causar {dano_especial} de dano!')
        return dano_especial