#Aula 55

entrada = input("Digite um numero INTEIRO: ")

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = "impar"
    
    if par_impar:
        par_impar_texto = "Par"

    print(f"O numero {entrada_int} é {par_impar_texto}")

else: 
    print("Você não digitou um numero inteiro.")

    