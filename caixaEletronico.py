while True:
    try:
        saque = int(input ("Digite o valor do saque: "))
        if saque <=0:
            print("O saque deve ser maio que 0.")
            continue

        elif saque >=1000:
            print("O saque deve ser menor que 1000 reais")
            continue

        else:
            print("Valor aceito! ")
            break
            
    except ValueError:
        print("Digite apenas números inteiros.")

print("Saque concluído: ", saque) 