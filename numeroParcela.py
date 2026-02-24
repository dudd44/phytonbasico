while True:
    try:
        parcela = float(input("Digite o número de parcelas:"))
        if 1<= parcela <=12:
            break
        else:
            print("O número de parcelas deve ser entre 1 e 12. ")
    except ValueError:
        print ("Digite apenas números inteiros.")

print ("parcela Cadastrada: ", parcela)