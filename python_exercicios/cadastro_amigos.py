# lista com pares de amizades
amizades = [(0,1), (0,2), (1,2), (1,3), (2,3)]

# Dicionário de usuários
usuarios = [
    {"id": 0, "nome": "Alice"},
    {"id": 1, "nome": "Bob"},
    {"id": 2, "nome": "Carol"},
    {"id": 3, "nome": "David"}
]

# Criar um dicionário de amizades vazias
conexoes = {usuario["id"]: [] for usuario in usuarios}

# preencher as conexões
for i, j in amizades:
    conexoes[i].append(j)
    conexoes[j].append(i)

# função para contar amigos
def numero_de_amigos(usuario):
    return len(conexoes[usuario["id"]])

# Mostrar quantidade de amigos de cada um
for usuario in usuarios:
    print(f'{usuario["nome"]} tem {numero_de_amigos(usuario)} amigos.')

# Calcular total de conexões
total = sum(numero_de_amigos(usuario) for usuario in usuarios)
media = total / len(usuarios)

print("\nTotal de conexões:", total)
print("Média de conexões por pessoa:", media)