
def cadastrar():
    users = []
    user = input("Digite o nome de usuário: ")
    users.append(user)
    senha = int(input("Digite a senha: "))
    senhaconfirm = int(input("Confirme a senha: "))
    if senha != senhaconfirm:
        print("Senhas devem ser iguais")
        raise Exception("ERRO")
    print("Usuário criado!")

    def logar():
        log = input("Digite o nome do usuário: ")
        pas = int(input("Digite a senha: "))
        if log != user or pas != senha: 
            print("Usuário ou senha incorreto!")
            raise Exception("ERRO")
    
    print("Se deseja sair, digite 0 ")
    print("Para logar, digite 1")
    act1 = int(input("O que deseja fazer: "))
    if act1 == 0:
        raise Exception("Finalizado")
    elif act1 == 1:
        logar()
    else:
        raise Exception("1 ou 0")
    
    
    def lista():
        print("Olá! Vamos acompanhar as suas notas")
        notas = ["Matemática: 10", "Português: 9", "Geografia: 8.5"]
        print("Digite 1 para adicionar notas")
        print("Digite 2 para remover notas")
        print("Digite 3 para ver as notas")
        act = int(input("Digite o que deseja fazer: "))
        if act == 1:
            notas.append(input("Digite a matéria e nota que deseja adiconar: "))
            print("Notas atualizadas!")
            print(notas)
        elif act == 2:
            notas.remove(input("Digite a matéria e nota que deseja retirar: "))
            print("Notas atualizadas!")
            print(notas)
        elif act == 3:
            print(notas)
        else:
            print("Digite apena 1,2 ou 3!")
    lista()

print("Olá, bem vindo!")
print("Primeiro passo: criar um usuário")
cadastrar()

