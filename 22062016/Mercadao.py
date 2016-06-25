'''
Trabalho de conclusão do curso de Programação Orientada a Objetos
Faculdades Integradas de Diamantino
Prof. Esp. Thiago Serra Ferreira de Carvalho
-----------------------------------------------------------------
(se você fez algo com estas funções, passou!!) ;'-)
(achando algum bug, corrija!)
'''

import sys

'''
Classe Produto

    id:              código do produto
    valor:           valor do produto
    estoque:         quantidade de produto em estoque
    qtdvendida:      quantidade vendida do produto

    def __init__:   construtor da classe

    def setId:      guarda o id do produto
    def getId:      retorna o id do produto
    def setValor: 	define o valor do produto
    def getValor: 	retorna o valor do produto
    def setEstoque: 	define a quantidade de produtos em estoque (não permite negativo)
    def getEstoque: 	retorna a quantidade de produtos em estoque
    def checaEstoque: 	(bool) se quantidade vendida é maior que quantidade em estoque
    def getQtdVendida: 	retorna quantidade de produtos vendidos
    def estiqueta: 	mostra dados do produto gravado
    def etiquetaVendidos: 	mostra dados dos produtos vendidos
    def vender: 	atualiza quantidade vendida e estoque
    def _diminuirEstoque: 	atualiza quantidade de produtos no estoque
'''
class Produto:
    _id = 0
    _valor = 0.0
    _estoque = 0
    _qtdVendida = 0

    def __init__(self, ident, valor, estoque):
        self.setId(ident)
        self.setValor(valor)
        self.setEstoque(estoque)
        self.etiqueta()
 
    def setId(self, ident):
        self._id = ident

    def getId(self):
        return self._id

    def setValor(self, valor):
        self._valor = valor

    def getValor(self):
        return self._valor

    def setEstoque(self, qtd):
        if qtd > 0:
            self._estoque = qtd
            if self._estoque <= 5:
                print("[*] Estoque baixo! Produto nº %d  -> estoque de %d unidades!" % ( self.getId(), self.getEstoque()))
        else:
            print("[*] Estoque não pode ser negativo")

    def checaEstoque(self, qtd):
        if qtd <= self._estoque:
            return True
        else:
            return False
        
    def getEstoque(self):
        return self._estoque
    
    def getQtdVendida(self):
        return self._qtdVendida

    def _diminuirEstoque(self, qtd):
        self._estoque -= qtd
        if self._estoque <= 5:
            print("[*] Estoque baixo! Produto nº %d  -> estoque de %d unidades!" % ( self.getId(), self.getEstoque()))

    def etiqueta(self):
        print("-"*80)
        print("Produto Nº: %d | Estoque: %d | Valor unitário: %10.2f" % (self.getId(), self.getEstoque(), self.getValor()))
        print("-"*80)

    def etiquetaVendidos(self):
        print("-"*80)
        print("Produto Nº: %d | Qtd.Comprada: %d | Valor Total: %10.2f" % (self.getId(), self.getQtdVendida(), self.getValor()*self.getQtdVendida()))
        print("-"*80)
    
    def vender(self, qtd):
        if qtd <= self.getEstoque():
            self._qtdVendida += qtd
            self._diminuirEstoque(qtd)
        else:
            print("[*] Quantidade não disponível para venda! Estoque atual: %d" % self.getEstoque())

'''
Classe Caixa

	lstEstoque: 	guarda o estoque informado pelo usuário
	lstCarrinho: 	carrinho de compras
	valorTotal: 	soma total de valores vendidos

	def __init__: 		construtor da classe Caixa
	def menuInicial: 	monta o menu da primeira tela de opções
	def menuEstoque: 	monta o menu da tela de estoque
	def menuCaixa: 		monta menu da tela caixa

	def gravaEstoque: 	insere o item informado pelo usuario no estoque
	def imprimirEstoque: 	lista os produtos cadastrados no estoque
	def imprimirCarrinho: 	mostra produtos no carrinho de compras
	def encerrarVenda: 	finaliza a venda atual - limpa o carrinho de compras
	def venderItens: 	alimenta o carrinho de compras com produtos escolhidos pelo usuario

	def carregarEstoqueInicial: 	entra com um estoque base
'''
class Caixa:
    lstEstoque = []
    lstCarrinho = []
    valorTotal = 0.0

    def __init__(self):
        self.carregaEstoqueInicial()
        self.menuInicial()

    def menuInicial(self):
        a = Menu()
        a.addOpcao("Estoque", self.menuEstoque)
        a.addOpcao("Caixa", self.menuCaixa)
        a.executar()
        
    def menuEstoque(self):
        a = Menu()
        a.addOpcao("[<] Voltar", self.menuInicial)
        a.addOpcao("Incluir Produto", self.gravaEstoque)
        a.addOpcao("Listar Estoque", self.imprimirEstoque)
        a.addOpcao("Lista Vendas", self.imprimirCarrinho)
        a.executar()

    def menuCaixa(self):
        if len(self.lstEstoque) > 0:
            a = Menu()
            a.addOpcao("[<] Voltar", self.menuInicial)
            a.addOpcao("Vender Item", self.venderItens)
            a.addOpcao("Encerrar Venda", self.encerrarVenda)
            a.executar()
        else:
            print("[*] Não existem produtos cadastrados!")
            
    def gravaEstoque(self):
        ident = int(input("Informe o nº do produto: "))
        valor = float(input("Informe o valor: "))
        estoque = int(input("Informe a quantidade em estoque: "))
        prod = Produto(ident, valor, estoque)
        self.lstEstoque.append(prod)

    def imprimirEstoque(self):
        if len(self.lstEstoque) > 0:
            print("\n")
            print("---> Lista de produtos em estoque <--- ")
            for prod in self.lstEstoque:
                prod.etiqueta()
        else:
            print("[*] Não existem produtos cadastrados!")

    def imprimirCarrinho(self):
        totalValor = 0
        totalQtd = 0
        if len(self.lstCarrinho) > 0:
            print("\n")
            print("-"*80)
            print("---> Carrinho de compras - Posição Atual <--- ")
            for prod in self.lstCarrinho:
                prod.etiquetaVendidos()
                totalValor += prod.getQtdVendida()*prod.getValor()
                totalQtd += prod.getQtdVendida()
            print("---> Quantidade:          %d" % totalQtd)
            print("---> Subtotal:       %10.2f" % totalValor)
            print("-"*80)
        else:
            print("[*] Carrinho vazio!")            


    def encerrarVenda(self):
        totalValor = 0
        totalQtd = 0
        if len(self.lstCarrinho) > 0:
            print("\n")
            print("-"*80)
            print("---> Carrinho de compras - Venda Finalizada <--- ")
            for prod in self.lstCarrinho:
                prod.etiquetaVendidos()
                totalValor += prod.getQtdVendida()*prod.getValor()
                totalQtd += prod.getQtdVendida()
            print("---> Qtd.Total:           %d" % totalQtd)
            print("---> Valor Total:     %10.2f" % totalValor)
            print("-"*80)
            self.lstCarrinho = []
        else:
            print("[*] Carrinho vazio!")

            
    def venderItens(self):
        self.imprimirEstoque()
        item = int(input("Informe o nº do produto que deseja comprar: "))
        achou = False
        for p in self.lstEstoque:
            if p.getId() == item:
                achou = True
                itemComprado = p
                qtd = int(input("Informe a quantidade vendida: "))
                if itemComprado.checaEstoque(qtd) == True:
                    itemComprado.vender(qtd)
                    self.lstCarrinho.append(itemComprado)
                else:
                    print("[*] Quantidade vendida maior que estoque disponível!")
                    
        if achou == False:
            print("[*] Produto não encontrado!")
        else:
            self.imprimirCarrinho()

    def carregaEstoqueInicial(self):
        print("[*] Carregando estoque inicial....")
        prod = Produto(1, 2.99, 20)
        self.lstEstoque.append(prod)
        prod1 = Produto(2, 5.75, 10)
        self.lstEstoque.append(prod1)
        prod2 = Produto(3, 9.12, 6)
        self.lstEstoque.append(prod2)
        prod3 = Produto(4, 0.99, 80)
        self.lstEstoque.append(prod3)

'''
Classe Menu:
	
	def __init__: 	construtor da classe (define a opção padrão)
	def addOpcao: 	adciona opção no menu
	def exibir: 	mostra menu para o usuario
	def executar: 	aguarda opção a ser informada pelo usuário
	def sair: 	sai do sistema
'''
class Menu:
    def __init__(self):
        print("\n"*5)
        print("Programação Orientada a Objeto com Python!")
        print("Prof. Esp. Thiago Serra F Carvalho")
        print("Programa exemplo - Trabalho Final!!!!!")
        print("------------------------------------------")
        self.opcao = [ [" Sair [>] ", self.sair]]

    def addOpcao(self, op, funcao):
        self.opcao.append([op, funcao])

    def exibir(self):
        print("\n"*1)
        print("-"*15)
        print("Mercadão - Menu")
        print("-"*15)
        for i, op in enumerate(self.opcao):
            print("[{0}] - {1}".format(i, op[0]))
        print()

    def executar(self):
        while True:
            self.exibir()
            escolha = int(input("Escolha uma opção: "))
            if escolha == 99:
                break
            self.opcao[escolha][1]()

    def sair(self):
        print("\n"*100)
        print("Programação Orientada a Objeto com Python!")
        print("Prof. Esp. Thiago Serra F Carvalho")
        print("Programa exemplo - Trabalho Final!!!!!")
        print("------------------------------------------")
        print ('''
        Obrigado por usar nosso sistema!
        SerraConsultoria.com.br
            ''')
        print("------------------------------------------")
        sys.exit(0)

n = Caixa()
