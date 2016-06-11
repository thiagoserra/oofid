class Carro:
    _cor = ''
    _potenciaMotor = ''
    _qtdPortas = 0

    def setCor(self, cor):
        self._cor = cor

    def setPotenciaMotor(self, potenciaMotor):
        self._potenciaMotor = potenciaMotor

    def setQtdPortas(self, qtdPortas):
        self._qtdPortas = qtdPortas

    def getCor(self):
        return self._cor

    def getPotenciaMotor(self):
        return self._potenciaMotor

    def getQtdPortas(self):
        return self._qtdPortas


class CarrosEsportivos(Carro):
    _motorTurbo = 0

    def setMotorTurbo(self):
        motorTurbo = int(input("Tem motor turbo? 1=sim ou 0=não: "))
        if motorTurbo != 0:
            motorTurbo = 1
        self._motorTurbo = motorTurbo

    def getMotorTurbo(self):
        return self._motorTurbo



class Caminhonetes(Carro):
    _cabineDupla = 0

    def setCabineDupla(self):
        cabineDupla = int(input("Tem cabine dupla? 1=sim ou 0=não: "))
        if cabineDupla != 0:
            cabineDupla = 1
        self._cabineDupla = cabineDupla

    def getCabineDupla(self):
        self._cabineDupla
        

class Calça:
    _tam = 0
    _cor = ''
    _tipoTecido = ''
    _estoque = 0

    def setTamanho(self, tam):
        self._tam = tam

    def getTamanho(self):
        return self._tam
    
    def setCor(self, cor):
        self._cor = cor

    def getCor(self):
        return self._cor

    def setTipoTecido(self, tt):
        self.tipoTecido = tt

    def getTipoTecido(self):
        return self._tipoTecido

    def vender(self, qtdVendida):
        if self._estoque - qtdVendida >= 0:
            self._estoque = self._estoque - qtdVendida
        else:
            print("Não é possível efetuar a venda! Quantidade em estoque é: ", str(self._estoque))

    def setEstoque(self, estoque):
        if estoque > 0:
            self._estoque = estoque
        else:
            print("O estoque não pode ser negativo!")
            
    def getEstoque(self):
        return self._estoque

class CalçaFemina(Calça):
    _elastano = 0

    def setTemElastano(self):
        e = 0
        e = int(input("Tem elastano? 1=sim ou 0=não: "))
        if e != 0:
            e = 1
        self._elastano = e

    def getElastano(self):
        return self._elastano
    

class CalçaMasculina(Calça):

    def setTamanho(self):
        t = int(input("Qual o tamanho da calça? "))
        if t < 38:
            print("O tamanho da calça deve ser maior ou igual a 38")
        else:
            self._tam = t


class Aluno:
    _matricula = 0
    _nota = 0.0

    def setMatricula(self, m):
        self._matricula = m

    def getMatricula (self):
        return self._matricula

    def setNota(self, n):
        self._nota = n

    def getNota(self):
        return self._nota



class Diario:
    _listaAlunos = []
    
    def incluirAluno(self, aluno):
        self._listaAlunos.append(aluno)

    def calcularMedia(self):
        nota = 0
        media = 0.0
        for b in self._listaAlunos:
            nota = nota + b.getNota()
        media = nota / len(self._listaAlunos)
        print("A media da turma é: ", media)


variavelControle = 99
d = Diario()
while variavelControle == 99:
    a = Aluno()
    matricula = int(input("informe o matricula do aluno: "))
    nota = float(input("informe a nota do aluno : "))
    a.setMatricula(matricula)
    a.setNota(nota)
    d.incluirAluno(a)
    variavelControle = int(input("Para continuar digite 99: "))

d.calcularMedia()








    
