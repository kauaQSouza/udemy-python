nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"seu nome invertido é {nome[::-1]}")

    if " " in nome:
        print(f"Seu nome tem espaço")   
    else: 
        print(f"Seu nome não contém espaço")    

    print(f"seu nome tem {len(nome)} letras") 
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else: 
    print("Desculpe, nada foi digitado.")