pessoa1 = {"abacate","papel","arroz","refrigerante","maça"}
pessoa2 = {"chinelo","arroz","açúcar","camisa","pera"}
pessoa3 = {"azeitona","sal","arroz","cerveja"}
pessoa4 = {"creme","açúcar","arroz","sorvete"}

compras_a = set(pessoa1)
compras_b = set(pessoa2)
compras_c = set(pessoa3)
compras_d = set(pessoa4)

comum = pessoa1.intersection(pessoa1,pessoa2,pessoa3,pessoa4)
print(f"O item em comum é {comum}")

print(f"Lista de compras pessoa1: {pessoa1}")
print(f"Lista de compras pessoa2: {pessoa2}")
print(f"Lista de compras pessoa3: {pessoa3}")
print(f"Lista de compras pessoa4: {pessoa4}")


totalcompras = pessoa1.union(pessoa2,pessoa3,pessoa4)
print(f"Total de compras: {totalcompras}\n")
print(len(totalcompras))



