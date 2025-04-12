from os import system
# Projeto backend de calculadora de conversão de temperatura
# Autor: Mateus Levi Magalhães Gomes
# LinkedIn: https://www.linkedin.com/in/mateusmagalhaes/

# Título do projeto
titulo = """_________________________________________
 CALCULADORA DE CONVERSÃO DE TEMPERATURA
_________________________________________\n"""

def cfk(a):
    if a=="1":
        return " °C"
    elif a=="2":
        return " °F"
    else:
        return " K"

# Iniciando o loop do programa
final="1"
tip_erro = 0

while final=="1":

    # Recebendo os dados com tratamentos de erro
    while True:
        system("cls") # Comando para limpar a tela
        print(titulo)

        # Avisa o tipo de erro que deu
        if tip_erro == 1:
            print("*Opção inválida. Tente de novo!")

        de = input("\nSelecione sua unidade de medida: \n1. °C \n2. °F \n3. K\n")
        if de not in ["1", "2", "3"]:
            tip_erro = 1
        else:
            tip_erro = 0
            break

    while True:
        system("cls")
        print(titulo)
        print(f"De: {cfk(de)}")

        # Avisa o tipo de erro que deu
        if tip_erro == 1:
            print("Opção inválida. Tente de novo!")

        para = input("\nSelecione a medida para qual você quer converter: \n1. °C \n2. °F \n3. K\n")
        if para not in ["1", "2", "3"]:
            tip_erro = 1
        else:
            tip_erro = 0
            break

    while True:
        system("cls")
        print(titulo)
        print(f"De: {cfk(de)}   Para: {cfk(para)}")

        # Avisa o tipo de erro que deu
        if tip_erro == 1:
            print("*Esse valor não é um número. Digite novamente!")

        elif tip_erro == 2:
            print("*A unidade K (kelvin) não pode ser um número negativo. Digite novamente!")
        
        try:
            numero = float(input("\nDigite o valor: "))

        except ValueError:
            tip_erro = 1
        
        else:
            if (numero<0) and (de=="3"):
                tip_erro = 2
            else:
                tip_erro = 0
                break

    # Conversões das temperaturas
    if de=="1":
        de = " °C"

        if para=="1":
            num_conv = numero
            para = " °C"

        elif para=="2":
            num_conv = numero*1.8+32
            para = " °F"

        elif para=="3":
            num_conv = numero + 273
            para = " K"

    elif de=="2":
        de = " °F"

        if para=="1":
            num_conv = (numero-32)/1.8
            para = " °C"
        
        elif para=="2":
            num_conv = numero
            para = " °F"

        elif para=="3":
            num_conv = ((numero-32)*5/9)+273
            para = " K"

    elif de=="3":
        de = " K"

        if para=="1":
            num_conv = numero-273
            para = " °C"
        
        elif para=="2":
            num_conv = (numero-273)*1.8+32
            para = " °F"
        
        elif para=="3":
            num_conv = numero
            para = " K"


    # Imprimindo na tela a mensagem de converção
    # Escolhendo finalizar ou fazer uma nova consulta
    while True:
        system("cls")
        print(titulo)
        print(f"\033[1mResultado:\033[0m {numero}{de} é igual à {num_conv:.2f}{para}\n")
        
        if tip_erro == 1:
            print("*Opção inválida. Tente de novo!")
            tip_erro = 0

        final = input("\nDeseja fazer uma nova consulta? \n1. Sim\n2. Não\n")
        
        if final not in ["1", "2"]:
            tip_erro = 1
        else:
            break

    system("cls")
    