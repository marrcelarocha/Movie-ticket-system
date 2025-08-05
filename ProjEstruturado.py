import sys

class MOVIE:
    def __init__(self, name, duration_in_minutes, genre):
        self.name = name
        self.duration_in_minutes = duration_in_minutes
        self.genre = genre

movie1 = MOVIE("Divergent", 139, "ação")
movie2 = MOVIE("Toy story 1", 81, "animação")
movie3 = MOVIE("Notting Hill", 124, "romance")
movie4 = MOVIE("The conjuring", 112, "terror")
movie5 = MOVIE("Minha mãe é uma peça", 84, "comédia")
movie6 = MOVIE("Interestelar", 169, "ficção científica")
movie7 = MOVIE("A viagem de Chihiro", 125, "fantasia")
movie8 = MOVIE("Saw", 103, "terror")
movie9 = MOVIE("Sonic: O filme", 99, "comédia")

usuarios = {}
def conta():
    global usuarios
    escolha = input("Já tem cadastro?\n[1] - Sim\n[2] - Não\n> ")
    
    if escolha == "1":
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
        if login in usuarios and usuarios[login] == senha:
            print("Login realizado com sucesso!")
            return 
        else:
            print("Login ou senha incorretos!")
            return
    
    elif escolha == "2":    
        login = input("Crie um login: ")
        if login in usuarios:
            print("Login já existe! Tente novamente.")
            return
        senha = input("Crie uma senha: ")
        usuarios[login] = senha
        print("Cadastro realizado com sucesso!")
        menu()
    else:
        print("Opção inválida!")
        return

def pagamento():
    metodo = input("Escolha o método de pagamento:\n[1] - Cartão de crédito\n[2] - Cartão de débito\n[3] - Pix\n> ")
    match metodo:
        case "1":
            print("Pagamento realizado com cartão de crédito!")
        case "2":
            print("Pagamento realizado com cartão de débito!")
        case "3":
            print("Pagamento realizado com Pix!")
        case _:
            print("Opção inválida!")

def escolher_assento():
    assentos = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    assento = input(f"\nEscolha um assento entre: {', '.join(assentos)}\n> ")
    
    if assento in ("A1","A2","A3","B1","B2","B3","C1","C2","C3"):
        print("Assento reservado!\n")
        assentos.remove(assento)
        decisão = input("Gostaria de finalizar a compra?\n[1] - Sim\n[2] - Não\n> ")
        if decisão == "1":
            tipo = input("Qual o tipo de ingresso?\n[1] - Meia entrada\n[2] - Inteira\n[3] - Meia entrada e Assinante do grupo da pipoca\n[4] - Inteira e Assinante do grupo da pipoca\n> ")
            if tipo == "1":
                print("\nTotal : R$ 15,00")
                pagamento()
            elif tipo == "2":
                print("\nTotal : R$ 30,00")
                pagamento()
            elif tipo == "3":
                print("\nTotal : R$ 10,00")
                pagamento()
            elif tipo == "4":
                print("\nTotal : R$ 25,00")
                pagamento()
            else:
                print("Opção inválida!")
        elif decisão == "2":
            menu()
        else:
            print("Opção inválida!")
    else:
        print("Assento não encontrado!")
 

def menu():
    escolha = input("Escolha uma opção:\n[1] - Escolher cinema\n[2] - Sair\n[3] - Entrar na conta\n> ")
    match escolha:
        case "1":
            sub_escolha = input("Escolha o cinema:\n[1] - Cinesystem\n[2] - Kinoplex\n[3] - Centerplex\n> ")
            match sub_escolha:
                case "1":
                    sub_sub_escolha = input("Escolha o filme:\n[1] - Divergent\n[2] - Notting Hill\n[3] - The conjuring\n> ")
                    match sub_sub_escolha:
                        case "1":
                            print(f"Duração : {movie1.duration_in_minutes} minutos")
                            print(f"Gênero : {movie1.genre}")
                            escolher_assento()
                        case "2":
                            print(f"Duração : {movie3.duration_in_minutes} minutos")
                            print(f"Gênero : {movie3.genre}")
                            escolher_assento()
                        case "3":
                            print(f"Duração : {movie4.duration_in_minutes} minutos")
                            print(f"Gênero : {movie4.genre}")
                            escolher_assento()
                        case _:
                            print("Opção inválida!")
                case "2":
                    sub_sub_escolha = input("Escolha o filme:\n[1] - Toy story 1\n[2] - Minha mãe é uma peça\n[3] - Interestelar\n> ")
                    match sub_sub_escolha:
                        case "1":
                            print(f"Duração : {movie2.duration_in_minutes} minutos")
                            print(f"Gênero : {movie2.genre}")
                            escolher_assento()
                        case "2":
                            print(f"Duração : {movie5.duration_in_minutes} minutos")
                            print(f"Gênero : {movie5.genre}")
                            escolher_assento()
                        case "3":
                            print(f"Duração : {movie6.duration_in_minutes} minutos")
                            print(f"Gênero : {movie6.genre}")
                            escolher_assento()
                        case _:
                            print("Opção inválida!")
                case "3":
                    sub_sub_escolha = input("Escolha o filme:\n[1] - A viagem de Chihiro\n[2] - Saw\n[3] - Sonic: o filme\n> ")
                    match sub_sub_escolha:
                        case "1":
                            print(f"Duração : {movie7.duration_in_minutes} minutos")
                            print(f"Gênero : {movie7.genre}")
                            escolher_assento()
                        case "2":
                            print(f"Duração : {movie8.duration_in_minutes} minutos")
                            print(f"Gênero : {movie8.genre}")
                            escolher_assento()
                        case "3":
                            print(f"Duração : {movie9.duration_in_minutes} minutos")
                            print(f"Gênero : {movie9.genre}")
                            escolher_assento()
                        case _:
                            print("Opção inválida!")
                case _:
                    print("Opção inválida!")

        case "2":
            sys.exit()
        case "3":
            conta()
        case _:
            print("Opção inválida!")

def main():
    menu()

if __name__ == "__main__":
    main()