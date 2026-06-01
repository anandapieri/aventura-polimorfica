import random
from Entidade import Entidade

class Inimigo(Entidade):
    def agir(self):
        return random.choice(['atacar', 'defender', 'usar_habilidade_especial']) #escolhe aleatório entre atacar, defender ou usar habilidade esp

    def atacar(self):
        dano = random.randint(self.forca - 3, self.forca + 3)
        print(f'{self.nome} ataca furiosamente causando {dano} de dano!')
        return dano
    
    def usar_habilidade_especial(self): #drenagem de vida do Personagem
        dano = random.randint(self.forca, self.forca * 2)

        print(f'{self.nome} drena {dano} pontos de vida!')
        
        self.vida += dano
        print(f'{self.nome} agora tem {self.vida} pontos de vida.')

        return dano