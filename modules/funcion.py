#*************
# Sena, Mosquera CBA
# Brayan Esteban Penagos Gutierrez
# Version 3.0
# 02/05/2024
# Ficha: 2877795
#Funcionalidad: Lista con numeros aleatorios
#*************

def funcion():
    #Importamos el modulo que nos va a permitir generar numeors random 
    import random
    import os
    from colorama import Fore, Style
    #Iniciamos un bucle while
    while True:
        #Esta funcion es para limpiar la pantalla
        os.system('cls')
        #Creamos las listas y contadores que vallamos a usar
        lista = []
        numeros_impresos = []
        suma_lista = 0
        contador = 0  

        while True:
            #Creamos el generador de numeros aleatorios
            numero = random.randint(0, 20)
            #Si el numero es igual a cero que termine de generar numeros
            if numero == 0:
                break
            #Cada numero que se genere que lo ingrese a la lista vacia
            lista.append(numero)
            numeros_impresos.append(str(numero))
            suma_lista += numero
            contador += 1  # Incrementamos el contador cada vez que se agrega un elemento

    #Los numero dentor de la lista se van a sumar
        print("[" + ", ".join(numeros_impresos) + "]")

        #Nos imprime la longitud de la lista
        print(Fore.LIGHTBLUE_EX + f"La longitud de la lista es:{Style.RESET_ALL} {contador}" )

    #Aca podremos saber si cada numero que salio es pas o impar
        for num in lista:
            if num % 2 == 0:
                print( f"{num}{Fore.CYAN } es par { Style.RESET_ALL}")
            else:
                print(f"{num} {Fore.MAGENTA }es impar{Style.RESET_ALL}")

    #Los numeros de la lista se van a sumar
        print(Fore.LIGHTYELLOW_EX +f"La suma de los numeros en la lista es:{Style.RESET_ALL} {suma_lista}")

    #Calculamos el promedio y lo imprimimos en pantalla
        promedio = suma_lista / contador
        print(Fore.LIGHTGREEN_EX +f"El promedio de los numeros en la lista es:{Style.RESET_ALL} {promedio}")

        #Le preguntamos al usuario si quiere continuar o acabar
        entrada = input( Fore.LIGHTRED_EX + f"Desea ejecutar nuevamente el programa S/N?:{Style.RESET_ALL}  ").upper()
        #Creamos un while para el S o N
        while entrada not in ['S', 'N']:
        #Si se equivoca al digitar el usuario, le mandara este mensaje de que solo se puede S o N
            print( Fore.RED + "\nSolamente puede digitar S/N en mayúsculas." + Style.RESET_ALL)
            entrada = input("\nElija de nuevo ").upper()
        #Si elige N, se acabara el programa
        if entrada == 'N':
            break