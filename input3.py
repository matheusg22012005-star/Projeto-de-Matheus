estoque = {
    "camisa" : 50,
    "calça" : 70,
    "boné" : 25,
    "tênis nike" :200,
}

print("Estoque atual: ")
for produto, quantidade in estoque.items():
     print(f"{produto} : {quantidade}")
     nome_produto = input("\nInforme o nome do produto vendido: ")
     quantidade_vendido = int(input("\nInforme a quantidade vendida: "))
if nome_produto in estoque:
 if quantidade_vendido <= estoque[nome_produto]:
      estoque[nome_produto] = estoque[nome_produto] - quantidade_vendido
 print("venda realizada com sucesso!||camisa")
               
else:
 print("Produto não encontrado")

for produto, quantidade in estoque.items():
               print(f"{produto} | {quantidade}")
