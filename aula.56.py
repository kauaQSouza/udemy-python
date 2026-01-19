entrada = input("Digite uma hora em numero inteiro: ")

try: 
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print(f"Bom dia, agora são {hora} da manhã.")
    elif hora >= 12 and hora <= 17:
        print(f"Boa tarde,agora são {hora} da tarde.")
    elif hora >= 18 and hora <= 23:
        print(f"Boa noite, agora são {hora} da noite.")  
    else: 
        print("Não conheço essa hora.")      
except:   
        print("POr favor digite certo plmds.")