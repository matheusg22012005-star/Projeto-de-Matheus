jogadores = {}

for i in range(3):
    nome = input("Digite o nome do jogador: ")
    pontuacao = int(input("Digite a quantidade de pontos iniciais: "))
    jogadores[nome] = pontuacao

print("\nTabela inicial de pontos:")
for jogador, pontuacao in jogadores.items():
    print(f"{jogador} | {pontuacao}")

for i in range(3):
    nome = input("\nDigite o nome do jogador: ")
    pontuacao = int(input("Digite a quantidade de pontos conquistados: "))

if nome in jogadores:
    jogadores[nome] = jogadores[nome] + pontuacao
    print("Pontuação atualizada com sucesso!")
else:
    print("Jogador não encontrado!")

print("\nTabela atualizada:")
for jogador, pontuacao in jogadores.items():
    print(f"{jogador} | {pontuacao}")



