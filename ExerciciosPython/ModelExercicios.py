import math

class ModelExercicios:

    #Criar o Metodo Construtor
    def __init__(self):
        self.lista = []
        self.lista2 = []
        self.resultado = 0
        self.soma = 0
        self.numeros = 0
        self.contnega = 0
        self.contador = 0
        self.vetor = []



#============================================================================ E X E R C I C I O S ======================================================================================


    def exercicio1(self):

        num1 = 10
        num2 = 20
        num3 = 0

        num3 = num1
        num1 = num2
        num2 = num3

        return ("O valor de A é : {}\n O valor de B é : {}".format(num1, num2))

    # =================================================================================================================================================================================


    def exercicio2(self):
        num1 = int(input('Informe um número: '))
        print('O antecessor do numero é: {}'.format(num1 - 1))

    # =================================================================================================================================================================================



    def exercicio3(self):

        num1 = int(input('Informe a base do retangulo: '))
        num2 = int(input('Informe a altura do retangulo:'))

        print('A ârea do retangulo é: {}'.format(num1 * num2))

    # =================================================================================================================================================================================



    def exercicio4(self):

        diasAno = 365
        diasMes = 30



        num1 = int(input('Anos: '))
        num2 = int(input('Meses: '))
        num3 = int(input('Dias: '))

        num3 += (num1 * diasAno) + (num2 * diasMes)

        print('A sua idade em dias é: {}'.format(num3))

    # =================================================================================================================================================================================


    def exercicio5(self):

        totalEleitor = 0
        votosBrancos = 0
        votosValidos = 0
        votosNulos = 0
        porcBrancos = 0
        porcNulos = 0
        porcValidos = 0


        totalEleitor = int(input('Escreva o total de eleitores: '))
        votosBrancos = int(input('Escreva o numero de votos brancos: '))
        votosNulos = int(input('Escreva o numero de votos nulos: '))
        votosValidos = int(input('Escreva o numero de votos validos: '))


        porcBrancos = 100 * votosBrancos / totalEleitor
        porcNulos = 100 * votosNulos / totalEleitor
        porcValidos = 100 * votosValidos / totalEleitor


        print('Votos Brancos: {} | Porcentagem: {}%\nVotos Nulos: {} | Porcentagem: {}%\nVotos Validos: {} | Porcentagem: {}%'.format(votosBrancos, porcBrancos, votosNulos, porcNulos, votosValidos, porcValidos))

    # =================================================================================================================================================================================


    def exercicio6(self):

        salario = 0
        reajuste = 0
        novosalario = 0


        salario = int(input('Digite o salario: '))
        reajuste = int(input('Digite o reajuste em percentual: '))


        novosalario = salario * reajuste / 100

        novosalario = round(2)
        print('O novo salario é: {}%'.format(novosalario))

    # =================================================================================================================================================================================


    def exercicio7(self):

        custoFabrica = 0
        imposto = 0
        percDistribuidor = 0
        custoConsumidor = 0

        custoFabrica = int(input('O custo de fabrica é: '))


        percDistribuidor = (custoFabrica * 0.28) + custoFabrica
        imposto = (custoFabrica * 0.45) + custoFabrica
        custoConsumidor = percDistribuidor + imposto + custoFabrica


        print('O valor do automovel é: R${}'.format(custoConsumidor))

    # =================================================================================================================================================================================

    def exercicio8(self):

        nota1 = 0
        nota2 = 0
        nota3 = 0
        media = 0


        nota1 = int(input('Digite a nota 1: '))
        nota2 = int(input('Digite a nota 2: '))
        nota3 = int(input('Digite a nota 3: '))

        media = (nota1 + nota2 + nota3) / 3
        media = round(2)

        print('O sua nota final é: {}'.format(media))

    # =================================================================================================================================================================================


    def exercicio9(self):

        quant = 0


        quant = int(input('Quantas maçãs você quer comprar?'))

        if quant < 12:
            return ('O total é de: R${}'.format(quant * 1.30))
        else:
            return ('O total é de: R${}'.format(quant * 1.00))

    # =================================================================================================================================================================================


    def exercicio11(self):

        salario = 0
        vendas = 0
        a = 0
        b = 0
        c = 0

        salario = int(input('Digite seu salario: '))
        vendas = int(input('Digite o total de vendas: '))

        if vendas > 1500:
            a = vendas * 0.05
            b = salario + a
            return ('Salario total: R${}'.format(b))
        else:
            a = vendas * 0.03
            b = salario + a
            return('O salario total é: R${}'.format(b))


    # =================================================================================================================================================================================


    def exercicio12(self):

        conta = 0
        saldo = 0
        debito = 0
        credito = 0

        conta = int(input('Digite o numero da sua conta: '))
        saldo = int(input('Informe seu saldo: '))
        debito = int(input('informe o debito: '))
        credito = int(input('Informe o credito: '))

        saldo = (saldo - debito) + credito

        if saldo >= 0:
            return ('Saldo Positivo!')
        else:
            return ('Saldo Negativo!')


    # =================================================================================================================================================================================


    def exercicio13(self):


        print('\t ----Tabuada---- ')



        numero = int(input('Informe o numero para ver a tabuada: '))



        print('\n Tabuada de', numero, ':')


        for i in range(1, 11):
            print(numero, 'X', i, '=', (numero * i))



    # =================================================================================================================================================================================


    def exercicio14(self):


        numero = int(input('Informe um numero inteiro: '))

        if numero < 0:
            return('Valor invalido!')
        else:
            for i in range(1,numero):
                print(i)


    # =================================================================================================================================================================================


    def exercicio15(self):
        for i in range(1,10):
            print("Informe um número: ")
            num = int(input())

            if num < 0:
                self.contador = self.contador + 1

        print("Foram digitados {} números negativos".format(self.contador))


    # =================================================================================================================================================================================


    def exercicio16(self):

        while(self.contador < 10):
            self.contador = self.contador + 1
            self.lista.append(float(input("Digite um numero: ")))

        for num in self.lista:
            if num < 40:
                self.contnega = self.contnega + num
        print("Quantidade de Numeros negativos: ", self.contnega)


    # =================================================================================================================================================================================


    def exercicio17(self):

        x = 0
        for i in range(15, 101):
            x = x + i
            print('%d / %d = %5.1f' % (x, i, x / i))


    # =================================================================================================================================================================================


    def exercicio18(self):

        numeros = int(input("digite aqui a quantidade de números que você irá digitar: "))
        lista = []
        digitados = 0
        total = 0
        while digitados < numeros:
            num = int(input("digite aqui o " + str((digitados + 1)) + "°" + " número: "))
            lista.append(num)
            total = total + num
            digitados = digitados + 1

        lista.sort()
        print("a média dos números digitados é: " + str(total / len(lista)))
        print("o maior número é: " + str(lista[len(lista) - 1]))


    # =================================================================================================================================================================================

    def exercicio19(self):

        self.soma = 0
        for i in range(0,19,1):
            print("Digite a nota do ", i+1, "aluno: ")
            self.vetor.append(float(input()))
            self.soma = self.soma + self.vetor[i]

        media = self.soma / 20
        self.cont = 0

        for i in range(0,19,1):
            if self.vetor[i] > media:
                self.cont = self.cont + 1


        print("Média: ", media)
        print(self.cont, " alunos obtiveram nota acima da média.")

    # =================================================================================================================================================================================

    def exercicio20(self):

        self.contador = 0

        numeros = (int(input("Digite a quantidade de habitantes: ")))

        while self.contador < numeros:
            num = int(input("Digite o salario: "))
            num1 = int(input("Digite a quantidade de filhos: "))

            self.contador = self.contador + 1
            self.lista.append(num)
            self.lista2.append(num1)
            self.media = sum(self.lista) / len(self.lista)
            self.soma = sum(self.lista2) / len(self.lista2)

        for num in self.lista:
            if num < 150:
                self.numeros += 1
            self.resultado = (self.numeros * 100) / numeros


        return print("A media do salario dos habitantes é de: ", round(self.media), "\nA media do numero de filhos dos habitantes é de: ",round(self.soma), "\nO maior salario entre os habitantes é de: ", max(self.lista), "\nO percentual de habitantes com salario abaixo de R$150,00 é de: ", round(self.resultado))

