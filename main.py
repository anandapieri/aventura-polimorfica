from Inimigo import Inimigo
from Personagem import Personagem

jogador1 = Personagem('Arthur', 50, 10)
jogador2 = Inimigo('Goblin', 50, 10)

print()
print('Bem vindo ao Jogo de Turnos!')

while jogador1.vida > 0 and jogador2.vida > 0:
    print()
    print('--- Turno do Jogador ---')
    print("\nEscolha uma ação:")
    print("1. Atacar")
    print("2. Defender")
    print("3. Usar Habilidade Especial")
    print("4. Encerrar Jogo")

    choice = input("Digite o número da sua ação: ")

    if choice == "1":
        dano = jogador1.atacar()
        jogador2.receber_dano(dano)

    elif choice == "2":
        jogador1.defender()

    elif choice == "3":
        dano = jogador1.usar_habilidade_especial()
        jogador2.receber_dano(dano)

    elif choice == "4":
        print("Jogo encerrado.")
        break

    else:
        print("Opção inválida!")
        continue

    if jogador2.vida <= 0:
        break

    print()
    print('--- Turno do Inimigo ---')

    jogada_escolhida = jogador2.agir()
    print(f"Jogada escolhida: {jogada_escolhida}")

    if jogada_escolhida == 'atacar':
        dano = jogador2.atacar()
        jogador1.receber_dano(dano)

    elif jogada_escolhida == 'defender':
        jogador2.defender()
    
    elif jogada_escolhida == 'usar_habilidade_especial':
        dano = jogador2.usar_habilidade_especial()
        jogador1.receber_dano(dano)
    
print("\n--- Fim do Jogo ---")

if jogador1.vida > jogador2.vida:
    print(f"{jogador1.nome} venceu!")
else:
    print(f"{jogador2.nome} venceu!")