while True:
    usuario = input("Digite seu nome de usuário: ").strip()
    senha = input("Digite sua senha: ")

    if usuario ==" ":
        print("O nome de usuário não pode ser vazio. ")

    if senha ==" ":
        print("A senha não pode ser vazia. ")

    elif senha <=6:
        print("A senha deve conter mais de seis caracteres.")
    else:
        break

print("Usuário: ", usuario)
print("Senha: ", senha)
print("Usuário cadastrado com sucesso!")