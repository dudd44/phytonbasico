while True:
    try:
        usuario = input("Digite seu nome de usuário: ").strip()
        senha = input("Digite sua senha: ")

        if usuario == "":
            print("O nome de usuário não pode ser vazio. ")
            continue

        elif len(senha) == "":
            print("A senha não pode ser vazia. ")

        if len(senha) < 6 :
            print("A senha deve conter mais de seis caracteres.")

        else:
            break

    except ValueError:
        print("O nome de usuário não pode ser vazio. ")
        print("A senha não pode ser vazia. ")

print("Usuário: ", usuario)
print("Senha: ", senha)
print("Usuário cadastrado com sucesso!")