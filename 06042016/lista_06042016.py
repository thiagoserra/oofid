'''
    Este programa lê o número de dias, horas, minutos e segundos.
    Calcula a quantidade de segundos que existem nesse intervalo.
'''
print("Este programa lê a quantidade de dias, horas, minutos e segundos e informa quantos segundos existem neles")
dias = int(input("Informe o número de dias: "))
horas = int(input("Informe o número de horas: "))
minutos = int(input("Informe o número de minutos: "))
segundos = int(input("Informe o número de segundos: "))

qtdSegundosDia = dias * 24 * 60 * 60
qtdSegundosHora = horas * 60 * 60
qtdSegundosMinuto = minutos * 60

totalSegundos= qtdSegundosDia + qtdSegundosHora + qtdSegundosMinuto + segundos

print("Existem ", totalSegundos, "s em ", str(dias), "dias ", str(horas), "horas ", str(minutos), "minutos ", str(segundos), "segundos")


'''
    Este programa soma os números pares.
    A entrada define o limite.
'''
print("Este programa soma os números pares.")
print("O número informado define o limite da soma.")
print("*"*48)
limite = int(input("Informe um número: "))
contador = 2
soma = 0
while contador <= limite:
    print(contador)
    contador = contador + 2
    soma = soma + contador-2

print("A soma é: ", str(soma))



'''
    Programa responsavel por calcular o valor do aluguel de um carro
'''
tipoDeCarro = input("Qual a categoria do carro que você alugou? (E para Economico, S para Esportivo, F para Família): " )
dias = int(input("Quantos dias você utilizou o veiculo? " ))
km = float(input("Quantos quilometros você rodou com o carro? "))

if tipoDeCarro[0] in "ESF":
    if tipoDeCarro == "E":
        valor = 60.0*dias + km*0.15
    elif tipoDeCarro == "S":
        valor = 100.0*dias + km*0.20
    elif tipoDeCarro == "F":
        valor = 70.0*dias + km*0.18
    print("Valor a pagar: ", str(valor), "reais")
else:
    print("Categoria não cadastrada!")



'''
    Função responsável por validar o tipo de dado em uma variável
    Necessário informar a varíavel e o tipo de dado que se quer testar (int, float, str...)
    Retorna 1 caso corresponda ao tipo informado ou 0 em caso negativo
'''
def tipoDeDado(variavel, tipoDesejado):
    tipoVariavel = type(variavel)
    if tipoVariavel == tipoDesejado:
        return 1
    else:
        return 0


'''
    Este programa divide dois números,
    porém, utiliza somente soma e subtração.
    Este programa considera dividendo >= divisor
'''
dividendo = int(input("Digite o primeiro número - dividendo: "))
divisor = int(input("Digite o segundo número - divisor: "))

var = 0
quociente = 0
while (var < dividendo) and (dividendo-var >= divisor):
    var = var + divisor
    quociente = quociente + 1

if var == dividendo:
    print("A divisão é inteira. Resultado: ", str(quociente))
else:
    print("A divisão não é inteira. Resultado: ", str(quociente), " e o resto é: ", str(dividendo-var))
    
