import regras as r

print("Inicio do sorteio!!!!")

# declarar quantidade de nomes
qPessoas = 0
while True:
    qPessoas = input("Digite a quantidade de pessoas que vai participar: ")
    if qPessoas.isnumeric():
        qPessoas = int(qPessoas)
        break
    else:
        print("Digite um número otario: ")

lPessoas = r.quantidade(qPessoas)

# escolha
r.escolha(lPessoas)
