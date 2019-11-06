from random import randint


def quantidade(q):
    lPessoas = []
    for i in range(0, q):
        pessoa = input(f"Digite pessoa {i + 1} :")
        lPessoas.append(pessoa)

    return lPessoas


def escolha(lista):
    print("")
    print("--- O que deseja fazer ? ---")
    print(" 1 - Para listar os participantes aleatoriamente:")
    print(" 2 - Para separar em grupos:")
    print(" 3 - Para sortear 1 ou mais:")
    print(" 4 - Para ver quem é o mais sortudo:")
    print(" Diferente - Para finalizar:")
    escolha = 0
    while True:
        escolha = input("Digite a sua escolha: ")
        if escolha.isnumeric():
            escolha = int(escolha)
            break
        else:
            print("Digite um número otario: ")

    if escolha == 1:
        listaAleatoria(lista)
    elif escolha == 2:
        separarGrupos(lista)
    elif escolha == 3:
        sortear(lista)
    elif escolha == 4:
        maisSortudo(lista)
    else:
        print("--- FINALIZADO ---")


def listaAleatoria(lista, chama=True):
    if chama:
        print("--- A ordem do sorteio foi : ---")
    listaDeN = []
    novaLista = []
    vezes = 0
    while True:
        if vezes >= len(lista):
            break
        n = randint(0, len(lista) - 1)

        if n not in listaDeN:
            if chama:
                print(f"{vezes + 1} {lista[n]}")
            novaLista.append(lista[n])
            vezes += 1
        listaDeN.append(n)
    if chama:
        escolha(lista)
    return novaLista


def separarGrupos(lista):
    qGrupo = 0
    while True:
        qGrupo = input(f"Digite a quantidade de grupos: Menor que {len(lista)} :")
        if qGrupo.isnumeric():
            qGrupo = int(qGrupo)
            break
        else:
            print("Digite um número otario: ")

    lista = listaAleatoria(lista, False)
    qPGrupo = len(lista) // qGrupo
    print(f"--- Quantidade por grupo vai ser de {qPGrupo} ---")
    q = 1
    g = 1
    for i in lista:
        print(f"grupo{g} {i}")
        q += 1
        if q > qPGrupo:
            q = 1
            g += 1

    escolha(lista)


def maisSortudo(lista):
    sortudo = randint(0, len(lista))
    lista = listaAleatoria(lista, False)
    print(f"O mais sortudo é o(a) {lista[sortudo]}")
    escolha(lista)


def sortear(lista):
    quantidade = 0
    while True:
        quantidade = input("Digite a quantidade de pessoas para sortear: ")
        if quantidade.isnumeric():
            quantidade = int(quantidade)
            break
        else:
            print("Digite um número otario: ")

    lista = listaAleatoria(lista, False)
    i = 0
    while i < quantidade:
        print(f"O {i + 1} é {lista[i]}")
        i += 1

    escolha(lista)
