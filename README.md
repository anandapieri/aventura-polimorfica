# Aventura Polimórfica

Projeto desenvolvido em Python para praticar conceitos de Programação Orientada a Objetos (POO), com foco em herança, polimorfismo, sobrescrita de métodos e reutilização de código.

O jogo consiste em uma batalha por turnos entre um herói e um inimigo controlado pelo computador. Cada personagem possui atributos, habilidades e comportamentos próprios, permitindo explorar conceitos fundamentais de orientação a objetos de forma prática.

## Objetivo do Projeto

Este projeto foi desenvolvido para consolidar conhecimentos em:

* Programação Orientada a Objetos (POO)
* Herança
* Polimorfismo
* Sobrescrita de métodos
* Encapsulamento de comportamentos
* Organização de código em múltiplos arquivos
* Geração de comportamentos aleatórios
* Estruturas condicionais e de repetição

## Tecnologias Utilizadas

* Python 3
* Biblioteca Random
* Git
* GitHub

## Estrutura do Projeto

```text
📁 aventura-polimorfica
│
├── Entidade.py
├── Personagem.py
├── Inimigo.py
├── main.py
└── README.md
```

## Hierarquia de Classes

```text
Entidade
├── Personagem
└── Inimigo
```

A classe `Entidade` concentra os atributos e comportamentos compartilhados entre os participantes da batalha.

As classes `Personagem` e `Inimigo` herdam esses comportamentos e implementam características próprias.

## Mecânicas do Jogo

### Personagem

O jogador pode escolher entre:

* Atacar
* Defender
* Usar habilidade especial
* Encerrar o jogo

### Inimigo

O inimigo escolhe aleatoriamente entre:

* Atacar
* Defender
* Usar habilidade especial

### Sistema de Defesa

Ao se defender, o personagem reduz pela metade o dano recebido no próximo ataque.

### Habilidades Especiais

#### Personagem

Causa dano aumentado com base na força do personagem.

#### Inimigo

Utiliza uma habilidade de drenagem de vida, causando dano ao oponente e recuperando pontos de vida.

## Exemplo de Execução

```text
Bem vindo ao Jogo de Turnos!

--- Turno do Jogador ---

Escolha uma ação:
1. Atacar
2. Defender
3. Usar Habilidade Especial
4. Encerrar Jogo

Digite o número da sua ação:
```

## Conceitos Praticados

### Herança

As classes especializadas reutilizam atributos e métodos da classe base.

### Polimorfismo

Diferentes classes respondem de maneiras distintas a comportamentos semelhantes.

### Sobrescrita de Métodos

O inimigo redefine seu comportamento de ataque para causar dano variável.

### Reutilização de Código

A lógica compartilhada permanece centralizada na classe base, reduzindo duplicação.

## Como Executar

Clone o repositório:

```bash
git clone LINK_DO_REPOSITORIO
```

Acesse a pasta do projeto:

```bash
cd aventura-polimorfica
```

Execute o jogo:

```bash
python main.py
```

## Melhorias Futuras

* Sistema de experiência
* Sistema de níveis
* Novos tipos de inimigos
* Diferentes classes de personagem
* Sistema de inventário
* Itens consumíveis
* Sistema de equipamentos
* Batalhas contra múltiplos inimigos
* Salvamento de progresso
* Interface gráfica

## Aprendizados

Este projeto foi desenvolvido como exercício prático para aprofundar conhecimentos em Programação Orientada a Objetos, especialmente os conceitos de herança e polimorfismo, amplamente utilizados no desenvolvimento de software profissional.

## Autora

Desenvolvido por Ananda Pieri.