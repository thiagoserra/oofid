# Lista de Exercícios 02  - Exercícios de revisão
# Resolução efetuada em sala - 23.03.2016
# Prof. Esp. Thiago Serra F Carvalho
# Programação Orientada a Objetos
# ------------------------------------------------


# Exercicio 01
# Funcao que converte graus celsius em Fahrenheit
print("Exercicio 01")
def celsiusFahrenheit(x):
    f = ((9/5)*x)+32
    strRes = str(x) + "ºC é igual a " + str(f) + " °F"
    return strRes

print(celsiusFahrenheit(40))
print("-----------------------------------------------")

# Exercicio 02
# Funcao que verifica se um numero é par ou impar
print("Exercicio 02")
def parImpar(numero):
    if numero%2== 0:
        return str(numero) + "  é par!"
    else:
        return str(numero) + " é impar!"

print(parImpar(20))
print(parImpar(21))
print("-----------------------------------------------")

# Exercicio 03
# Verificar a saida dos codigos fornecidos
print("Exercicio 03")
def calculos(x, y):
    x1 = x+y
    x2 = x*y
    return x1-x2

def calculos2(x, y):
    return x**y - x**3

calculos2(3,3)

print("calculos(4,2): " +str(calculos(4,2)))
print("calculos(9,16): " + str(calculos(9,16)))
print("calculos2(3, 2): " + str(calculos2(3, 2)))
print("calculos2(7,4): " + str(calculos2(7,4)))
print("4*calculos(5,3): " + str(4*calculos(5,3)))
print("calculos(8.2,2.3)+calculos2(5.9, 9.01): " + str(calculos(8.2,2.3)+calculos2(5.9, 9.01)))
print("-----------------------------------------------")

# Exercicio 04
# verificar a saida do codigo abaixo
print("Exercicio 04")
x = 4.5
if x>3:
    print("Resposta 1")
if x>4.5:
    print("Resposta 2")
if x>=5:
    print("Resposta 3")
if x<5:
    print("Resposta 4")
print("-----------------------------------------------")

# Exercicio 05
# verificar o maior valor entre a e b
print("Exercicio 05")
def maiorMenor(x, y):
    if x>y:
        return print(x, " é maior que ", y)
    elif y>x:
        return print(y, " é maior que ", x)
    else:
        return print(x, " é igual a ", y)

print("maiorMenor(10.9,11) -> ")
maiorMenor(10.9,11)
print("-----------------------------------------------")

# Exercicio 06
# verificar qual é o maior entre a, b e c
print("Exercicio 06")
def maiorMenorv2(a, b, c):
    if a>b and a>c:
        return print(a, " é o maior")
    elif b>a and b>c:
        return print(b, " é o maior")
    else:
        return print(c, " é o maior")

print("maiorMenorv2(10.9,11, 10.99) -> ")
maiorMenorv2(10.9,11, 10.99)
print("-----------------------------------------------")

# Exercicio 07
# imprimir mensagem na tela n vezes
print("Exercicio 07 - versao 01")
def mensagem(frase, n):
    i = 1
    while i <= n:
        print(frase)
        i = i + 1

mensagem("olá computer!", 10)

print("Exercicio 07 - versao 02")
def mensagemv2():
    texto = str(input("Digite uma frase/palavra qualquer: "))
    n = int(input("Quantas vezes deseja imprimir esse texto na tela: "))
    for ind in range(1, n+1):
        print(texto)

mensagemv2()
print("-----------------------------------------------")

# Exercicio 08
# efetuar a soma dos numeros inteiros até n, com sinal alternado
print("Exercicio 08")
def somarN(n):
    soma = 0
    for ind in range(1, n+1):
        soma = soma - ind * ( (-1) ** ind )
    return soma

print("somarN(8) -> ", somarN(8))
print("-----------------------------------------------")

# Exercicio 09
# calcular o fatorial (usando while)
print("Exercicio 09")
def fatorial(n):
    mult = 1
    for ind in range(1, n+1):
        mult = mult*ind
    return mult


print("fatorial(6) -> ", fatorial(6))
print("-----------------------------------------------")

# Exercicio 10
# Escrever na tela a tabuada de a até b (considerar a menor que b)
print("Exercicio 10")

# Solucao 01 (um intervalo de inteiros)
def tabuada(a, b):
    for i in range(a, b+1):
        print("Tabuada ", i)
        for j in range(1, 11):
            print(str(i) + " x " + str(j) + " = " + str(i*j))


print("tabuada(8, 9) -> ")
tabuada(8, 9)

# Solução 02 (uma por vez)
a = int(input("Qual a tabuada que você deseja imprimir? "))
for b in range(1, 11):
    print (a, ' x ', b, ' = ', a*b)
print("-----------------------------------------------")

# Exercicio 11
# Classificacao de idade do nadador
print("Exercicio 11")
a = int(input("Qual a idade do nadador? "))
if a < 9:
    print("Nadador Mirim")
elif (a >= 9) and (a < 14):
    print("Nadador Infantil")
elif (a >= 14) and (a < 18):
    print("Nadador Juvenil")
else:
    print("Nadador Adulto")
print("-----------------------------------------------")


# Exercicio 12
# Inverter uma palavra (ou frase)
print("Exercicio 12")
def inverter(frase):
    return print(frase[::-1])

print("meu nome é aluno! -> ")
inverter("meu nome é aluno!")

def inverterv2(texto):
    i = len(texto)-1
    inverso = ""
    while i>=0:
        inverso = inverso + texto[i]
        i=i-1
    return inverso

print("meu nome é aluno! -> ", inverterv2("meu nome é aluno!"))
print("-----------------------------------------------")


# Exercicio 13
# Retirar vogais de uma frase
print("Exercicio 13")

# Solucao 01
def remover(frase):
    i = 0
    remove = ""
    while i<len(frase):
        if frase[i] in "aeiou":
            remove = remove + ""
        else:
            remove = remove + frase[i]
        i += 1
    return print("%s" %remove)

print("remover('Ola! meu nome e computador') -> ")
remover('Ola! meu nome e computador')

# Solucao 02
def retiraVogal(texto):
    novoTexto = ""
    ind = 0
    while ind < len(texto):
        if texto[ind] != "a" and texto[ind] != "e" and texto[ind] != "i" and texto[ind] != "o" and texto[ind] != "u":
            novoTexto = novoTexto + texto[ind]
        ind = ind + 1
    return novoTexto

print("retiraVogal('Ola! meu nome e computador') -> ", retiraVogal('Ola! meu nome e computador'))
print("-----------------------------------------------")

# Exercicio 14
# Contar quantas vezes b aparece em a
print("Exercicio 14")
def encontrarLetra(frase, letra):
    contador = 0
    tamanho = len(frase)
    i = 0
    while i < tamanho:
        if frase[i] == letra:
            contador = contador + 1
        i = i + 1

    return contador

print("encontrarLetra('A novidade é que eu vou viajar', 'a')", encontrarLetra('A novidade é que eu vou viajar', 'a'))
print("-----------------------------------------------")



# Exercicio 15
# indices da letra na frase
print("Exercicio 15:")
def posicao_caractere(frase, caractere):
    lista = []
    for i in range(0,len(frase)):
        if frase[i]==caractere:
            lista.append(i)
    return lista

print("posicao_caractere('eu estou na escola!', 'e') -> ", posicao_caractere("eu estou na escola!", "e"))
print("--------------------------")
