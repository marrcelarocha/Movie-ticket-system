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

cinemas = {
    "1": { 
        "1": movie1,
        "2": movie3,
        "3": movie4
    },
    "2": {  
        "1": movie2,
        "2": movie5,
        "3": movie6
    },
    "3": {  
        "1": movie7,
        "2": movie8,
        "3": movie9
    }
}

def navegação_conta():
    navegar_conta = input("\nVocê deseja:\n[1] - Visualizar compras passadas\n[2] - Cancelar compra\n[3] - Realizar avaliação do filme\n[4] - Voltar ao menu\n> ")
    match navegar_conta:
        case "1":
            if len(histórico_filmes) == 0:
                print("\nNenhuma compra realizada.")
                navegação_conta()
            else:
                print("\nCompras passadas:", ", ".join(histórico_filmes))
                navegação_conta()
        case "2":
            if len(histórico_filmes) > 0:
                histórico_filmes.remove(histórico_filmes[len(histórico_filmes) - 1])
                print("\nÚltima compra cancelada.")
                navegação_conta()
            else:
                print("\nNenhuma compra para cancelar.")
                navegação_conta()
        case "3":
            if len(histórico_filmes) == 0:
                print("\nNenhuma compra realizada para avaliar.")
                navegação_conta()
            avaliação = input("Digite sua avaliação (1 a 5 estrelas): ")
            if avaliação in ("1","2","3","4","5"):
                print("Avaliação registrada! Obrigado pelo feedback.")
                navegação_conta()
            else:
                print("Avaliação inválida!")
                navegação_conta()
        case "4":
            menu()
        case _:
            print("Opção inválida!")
            navegação_conta()



usuarios = {}
def conta():
    global usuarios
    escolha = input("\nJá tem cadastro?\n[1] - Sim\n[2] - Não\n> ")
    
    if escolha == "1":
        login = input("\nDigite seu login: ")
        senha = input("Digite sua senha: ")
        if login in usuarios and usuarios[login] == senha:
            print("\nLogin realizado com sucesso!")
            navegação_conta()
        else:
            print("Login ou senha incorretos!")
            return
    
    elif escolha == "2":    
        nome = input("\nDigite seu nome: ")
        usuarios["Nome_usuário"] = nome
        login = input("Crie um login: ")
        if login in usuarios:
            print("Login já existe! Tente novamente.")
            return
        senha = input("Crie uma senha: ")
        usuarios[login] = senha
        print("\nCadastro realizado com sucesso!")
        navegação_conta()

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

def pipoca():
    escolha = input("\nGostaria de comprar pipoca?\n[1] - Sim\n[2] - Não\n> ")
    if escolha == "1":
        tamanho = input("\nEscolha o tamanho da pipoca:\n[1] - Pequena (R$ 4,50)\n[2] - Média (R$ 6,00)\n[3] - Grande (R$ 7,50)\n> ")
        match tamanho:
            case "1":
                print("Pipoca pequena adicionada ao pedido!")
                return 4.5
            case "2":
                print("Pipoca média adicionada ao pedido!")
                return 6.0
            case "3":
                print("Pipoca grande adicionada ao pedido!")
                return 7.5
            case _:
                print("Opção inválida!")
    elif escolha == "2":
        print("Pipoca não adicionada ao pedido.")
        return 0
    else:
        print("Opção inválida!")

assentos = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
def escolher_assento():
    global assentos
    assento = input(f"\nAssentos disponíveis: {', '.join(assentos)}\n> ")
    
    if assento in assentos:
        print("Assento reservado!\n")
        valor_pipoca = pipoca()
        decisão = input("\nGostaria de finalizar a compra?\n[1] - Sim\n[2] - Não\n> ")
        if decisão == "1":
            assentos.remove(assento)
            tipo = input("\nQual o tipo de ingresso?\n[1] - Meia entrada (R$ 15,00)\n[2] - Inteira (R$ 30,00)\n[3] - Meia entrada e Assinante do grupo da pipoca (R$ 10,00)\n[4] - Inteira e Assinante do grupo da pipoca (R$ 25,00)\n> ")
            if tipo == "1":
                total = 15 + valor_pipoca
                print(f"\nTotal : R$ {total}")
                pagamento()
            elif tipo == "2":
                total = 30 + valor_pipoca
                print(f"\nTotal : R$ {total}")
                pagamento()
            elif tipo == "3":
                total = 10 + valor_pipoca
                print(f"\nTotal : R$ {total}")
                pagamento()
            elif tipo == "4":
                total = 25 + valor_pipoca
                print(f"\nTotal : R$ {total}")
                pagamento()
            else:
                print("Opção inválida!")
        elif decisão == "2":
            menu()
        else:
            print("Opção inválida!")
    else:
        print("Assento não encontrado!")
        escolher_assento()

histórico_filmes = [] 

def menu():
    while True:
        print("\nBEM-VINDO AO SISTEMA DE RESERVA DE BILHETES DE CINEMA!\n")
        escolha = input("[1] - Escolher cinema\n[2] - Entrar na conta\n[3] - Sair\n> ")

        match escolha:
            case "1":
                sub_escolha = input("\nEscolha o cinema:\n[1] - Cinesystem\n[2] - Kinoplex\n[3] - Centerplex\n> ")
                
                if sub_escolha not in cinemas:
                    print("Opção inválida!")
                    continue

                print("\nFilmes em cartaz:")
                for key, filme in cinemas[sub_escolha].items():
                    print(f"[{key}] - {filme.name}")

                sub_sub_escolha = input("> ")

                if sub_sub_escolha in cinemas[sub_escolha]:
                    filme = cinemas[sub_escolha][sub_sub_escolha]
                    print(f"\nDuração : {filme.duration_in_minutes} minutos")
                    print(f"Gênero : {filme.genre}")
                    
                    decisao = input("\nVocê deseja:\n[1] - Reservar assento\n[2] - Voltar ao menu\n> ")
                    if decisao == "1":
                        histórico_filmes.append(filme.name)
                        escolher_assento()
                    elif decisao == "2":
                        menu() 
                    else:
                        print("Opção inválida!")
                    
                else:
                    print("Opção inválida!")

            case "2":
                conta()

            case "3":
                sys.exit()

            case _:
                print("Opção inválida!")

def main():
    menu()

if __name__ == "__main__":
    main()