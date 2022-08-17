from ModelExercicios import ModelExercicios

class ControlExercicios:

    # ============================================================================ C O N S T R U T O R ======================================================================================

    #Metodo Construtor

    def __init__(self):
        self.modelo = ModelExercicios()
        self.opcao = -1

    # ============================================================================== M E N U ========================================================================================

    #Menu

    def menu(self):
        print("\nEscolha um dos exercicios abaixo: " +
              "\n0. Sair" +
              "\n1. Exercicio 1" +
              "\n2. Exercicio 2" +
              "\n3. Exercicio 3" +
              "\n4. Exercicio 4" +
              "\n5. Exercicio 5" +
              "\n6. Exercicio 6" +
              "\n7. Exercicio 7" +
              "\n8. Exercicio 8" +
              "\n9. Exercicio 9" +
              "\n10. Exercicio 10" +
              "\n11. Exercicio 11" +
              "\n12. Exercicio 12" +
              "\n13. Exercicio 13" +
              "\n14. Exercicio 14" +
              "\n15. Exercicio 15"  +
              "\n16. Exercicio 16"  +
              "\n17. Exercicio 17"  +
              "\n18. Exercicio 18"  +
              "\n19. Exercicio 19"  +
              "\n20. Exercicio 20")
        self.opcao = int(input())#Coletando a escolha do usuario

    # ============================================================================== O P E R A C A O ====================================================================================

    def operacao(self):

        while(self.opcao != 0):
            self.menu()#Mostrar menu na tela
            if self.opcao == 0:
                print("Obrigado!")
            elif self.opcao == 1:
                print(self.modelo.exercicio1())
            elif self.opcao == 2:
                print(self.modelo.exercicio2())
            elif self.opcao == 3:
                print(self.modelo.exercicio3())
            elif self.opcao == 4:
                print(self.modelo.exercicio4())
            elif self.opcao == 5:
                print(self.modelo.exercicio5())
            elif self.opcao == 6:
                print(self.modelo.exercicio6())
            elif self.opcao == 7:
                print(self.modelo.exercicio7())
            elif self.opcao == 8:
                print(self.modelo.exercicio8())
            elif self.opcao == 9:
                print(self.modelo.exercicio9())
            elif self.opcao == 11:
                print(self.modelo.exercicio11())
            elif self.opcao == 12:
                print(self.modelo.exercicio12())
            elif self.opcao == 13:
                print(self.modelo.exercicio13())
            elif self.opcao == 14:
                print(self.modelo.exercicio14())
            elif self.opcao == 15:
                print(self.modelo.exercicio15())
            elif self.opcao == 16:
                print(self.modelo.exercicio16())
            elif self.opcao == 17:
                print(self.modelo.exercicio17())
            elif self.opcao == 18:
                print(self.modelo.exercicio18())
            elif self.opcao == 19:
                print(self.modelo.exercicio19())
            elif self.opcao == 20:
                print(self.modelo.exercicio20())
            else:
                print('Problema Encontrado!\n Tente Novamente!')












