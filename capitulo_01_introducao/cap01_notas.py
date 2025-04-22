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

def foaf_ids_bad(user):
    """"foaf significa "friend of a friend" [amigo de um amigo]"""
    return [foaf_id
    for friend_id in friendships[user["id"]]
    for foaf_id in friendships[friend_id]]

    from collections import Counter  # não é carregado por padrão

    def friends_of_friends(user):
        user_id = user["id"]
        return Counter (
            foaf_id
            for friend_id in friendships[user_id]    # Para cada amigo meu
            for foaf_id in friendships[friend_id]    # encontre os amigos deles
            if foaf_id != user_id                    # que nao sejam eu
            and foaf_id not in friendships[user_id]  # e não sejam meus amigos.
        )

print(friends_of_friends(users[3]))  # type: ignore # Counter({0: 2, 5: 1})

interests = [
    (0, "Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra")
(1, "NoSQL", "MongoDB", "Cassandra", "HBase")
(2, "Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas")
(3, "R", "Python", "statistics", "regression", "probability")
(4, "machine learning", "regression", "decision trees", "libsvm")
(5, "Python", "R", "Java", "C++", "Haskell", "programming languages")
(6, "statistics", "probability", "mathematics", "theory")
(7, "machine learning", "scikit-learn", "Mahout", "neural networks")
(8, "neural networks", "deep learning", "Big Data", "artificial intelligence")
(9, "Hadoop", "Java", "MapReduce", "Big Data")
]

def data_scientists_who_like(target_interest):
    """Encontre os ids dos usuários com o mesmo interesse"""
    return [user_id
    for user_id, user_interest in interests
    if user_interest == target_interest]

    from collections import defaultdict

    # as chaves são interesses, os valores são listas de user_ids com o interesse em questão
    user_ids_interest = defaultdict(list)
    for user_id, interest in interests:
        user_ids_by_interest[interest].append(user_id)
    # as chaves são user_ids, os valores são listas de interesses do user_id em questão
    for user_id, interest in interest:
        user_ids_by_user_id[user_id].append(interest)

    def most_common_interests_with(user):
        return Counter(
            interest_user_id
            for interest in interests_by_user_id[user["id"]]
            for interested_user_id in user_ids_by_interest[interest]
            if interested_user_id is user["id"]
        )
    
    # Salários e experiências

salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)]

#dados plotados
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()}

#buckets de experiência

def tenure_bucket(tenure):
    if tenure <2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

# contas pagas
years_paid_or_unpaid = [
    (0.7, "paid"),
    (1.9, "unpaid"),
    (2.5, "paid"),
    (4.2, "unpaid"),
    (6.0, "unpaid"),
    (6.5, "unpaid"),
    (7.5, "unpaid"),
    (8.1, "unpaid"),
    (8.7, "paid"),
    (10.0, "paid")
]

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"
    
words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
