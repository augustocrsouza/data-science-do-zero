# Os dados são a bas de decisões para crescimento e evolução das empresas.
# O autor cita diversos exemplos de variações na colet de dados. Por exmplo o ifood não é feito somente para saber oque você QUER comer,
# ele quer saber o porque você come e quando você come, aonde você mais come e qual em sido o alimento mais vendido.
# São diversas variações que os dados podem criar, então, é com isso que podemos trabalhar e ser valorizados.

#Motivação hipotética
# Ele traz um cenário fictício do começo da roina de um data scienster e a primeira coisa é quando o vice presidente apresenta um data dump para ele
# Oque é um data dump? Um conjunto de informações de vários usuários, cada usuário é representando em um "Dict" que é oque representa o usuário. Por exemplo:

# Dados dos usuários (mock do livro)
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

# Pares de amizades
friendship_pairs = [
    (0, 1), (0, 2), (1, 2), (1, 3),
    (2, 3), (3, 4), (4, 5), (5, 6),
    (5, 7), (6, 8), (7, 8), (8, 9)
]

# Criar um dicionário de amizades (dict com listas)
friendships = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

# Função para contar quantos amigos um usuário tem
def number_of_friends(user):
    """Quantos amigos tem o _user_"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

# Total de conexões
total_connections = sum(number_of_friends(user) for user in users)

# Número médio de conexões
num_users = len(users)
avg_connections = total_connections / num_users

# Lista de (user_id, número de amigos)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# Ordenar por número de amigos (do maior pro menor)
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)

# Exibir os resultados
print("Total de conexões:", total_connections)
print("Média de conexões por usuário:", avg_connections)
print("Usuários com mais amigos:")
print(num_friends_by_id)