class Bike:
    _cor = ""
    _marca = ""
    _modelo = ""

    def setCor(self, cor):
        self._cor = cor

    def setMarca(self, marca):
        self._marca = marca


    def setModelo(self, modelo):
        self._modelo = str(modelo)


class Moto(Bike):
    _potencia = 0.0
    _km = 0.0

    def setPotencia(self, potencia):
        self._potencia = potencia

    def setKm(self, km):
        self._km = km


class Filme:
    _duracao = 0
    _categoria = ""
    _ano = 0

    def setDuracao(self, outracoisa):
        self._duracao = outracoisa

    def setCategoria(self, categoria):
        self._categoria = categoria


    def setAno(self, ano):
        self._ano = ano

    def getAno(self):
        return self._ano


class Series(Filme):
    _episodio = 0
    _temporada = 0

    def setEpisodio(self, ep):
        self._episodio = ep

    def setTemporada(self, t):
        self._temporada = t

    def getEpisodio(self):
        return self._episodio
    
class Carro:
    _num = 0
    _valor = 0.0

    def setNum(self, n):
        self._num = n

    def setValor(self, v):
        self._valor = v

    def getNum(self):
        return self._num

    def getValor(self):
        return self._valor


class Venda:
    total = 0.0
    media = 0.0
  
    listaCarros = []

    def carrosVendidos(self, carro):
        self.listaCarros.append(carro)

    def valorTotalVendido(self):
        for car in self.listaCarros:
            self.total = self.total + car.getValor()
        print("Total vendido: ", str(self.total))
            
    def mediaValorVendido(self):
        self.media = self.total / len(self.listaCarros)
        print("Média de valores: ", str(self.media))

    def numeroCarroVendido(self):
        for car in self.listaCarros:
            print("Vendido carro: ", car.getNum())

continuar = 1
caixa = Venda()
while continuar == 1:
    carro1 = Carro()
    num = int(input("Informe o número do carro: "))
    carro1.setNum(num)
    valor = float(input("Informe o valor do carro: "))
    carro1.setValor(valor)
    caixa.carrosVendidos(carro1)
    continuar = int(input("Para continuar informando os carros digite 1: "))

caixa.valorTotalVendido()
caixa.mediaValorVendido()
caixa.numeroCarroVendido()
