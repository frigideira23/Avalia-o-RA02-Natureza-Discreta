print("Avaliação 3.1\n")
print("Nomes do grupo12:")
print("João Pedro Frigeri de Oliveira")
print("Hiago Bernardo da Silva\n")

##Questão 1A
print("Questão 1A\n")


def umA(n):
    print(f"Chamando umA({n})")
    if n == 1:
        print(f"umA({n}) retornou 10")
        return 10
    else:
        resultado = umA(n - 1) + 10
        print(f"umA({n}) retornou {resultado}")
        return resultado


print(umA(5))

##Questão 1B
print("Questão 1B\n")


def umB(n):
    print(f"Chamando umB({n})")
    if n == 1:
        print(f"umB({n}) retornou 2")
        return 2
    else:
        resultado = umB(n - 1) - 1
        print(f"umB({n}) retornou {resultado}")
        return resultado


print(umB(5))

##Questão 1C
print("Questão 1C\n")


def umC(n):
    print(f"Chamando umC({n})")
    if n == 1:
        print(f"umC({n}) retornou 1")
        return 1
    else:
        resultado = umC(n - 1) + n**2
        print(f"umC({n}) retornou {resultado}")
    return resultado


print(umC(5))

##Questão 1D
print("Questão 1D\n")


def umD(n):
    print(f"Chamando umD({n})")
    if n == 1:
        print(f"umD({n}) retornou 1")
        return 1
    else:
        resultado = n**2 * umD(n - 1) + n - 1
        print(f"umD({n}) retornou {resultado}")
        return resultado


print(umD(5))

##Questão 1E
print("Questão 1E\n")


def umE(n):
    print(f"Chamando umE({n})")
    if n == 1:
        print(f"umE({n}) retornou 3")
        return 3
    elif n == 2:
        print(f"umE({n}) retornou 5")
        return 5
    else:
        resultado = (n - 1) * umE(n - 1) + (n - 2) * umE(n - 2)
        print(f"umE({n}) retornou {resultado}")
        return resultado


print(umE(5))

##Questão 1F
print("Questão 1F\n")


def umF(n):
    print(f"Chamando umF({n})")
    if n == 1:
        print(f"umF({n}) retornou 2")
        return 2
    elif n == 2:
        print(f"umF({n}) retornou 5")
        return 5
    else:
        resultado = umF(n - 1) * umF(n - 2)
        print(f"umF({n}) retornou {resultado}")
        return resultado


print(umF(5))

##Questão 1G
print("Questão 1G\n")


def umG(n):
    print(f"Chamando umG({n})")
    if n == 1:
        print(f"umG({n}) retornou 1")
        return 1
    elif n == 2:
        print(f"umG({n}) retornou 2")
        return 2
    elif n == 3:
        print(f"umG({n}) retornou 3")
        return 3
    else:
        resultado = umG(n - 1) + 2 * umG(n - 2) + 3 * umG(n - 3)
        print(f"umG({n}) retornou {resultado}")
        return resultado


print(umG(5))