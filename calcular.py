# Crie funções que duplicam, triplicam e quadruplicam
#O número recebido como parâmetro.

def duplicar (numero):
    print(numero *2)
duplicar(5)

def triplicar (numero):
    print(numero *3)
triplicar(5)

def quadruplicar (numero):
    print(numero *4)
quadruplicar(5)

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))