nome = input("Digite seu nome: ")
tamanho_do_nome = len(nome)

if tamanho_do_nome <= 4:
    print(f"Seu nome é pequeno, pois tem somente {len(nome)} letras")

elif tamanho_do_nome >= 5 and tamanho_do_nome <= 6:
        print(f"Seu nome é médio, pois tem {len(nome)} letras")

elif tamanho_do_nome >= 7:
      print(f"Seu nome é grande, pois tem {len(nome)} letras")
    

    
       