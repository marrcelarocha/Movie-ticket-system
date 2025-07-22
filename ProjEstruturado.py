class MOVIE:
    def __init__(self, name, duration_in_minutes, genre):
        self.name = name
        self.duration_in_minutes = duration_in_minutes
        self.genre = genre

movie1 = MOVIE("Divergent", 139, "action")
movie2 = MOVIE("Toy story 1", 81, "animation")
movie3 = MOVIE("Notting Hill", 124, "romance")
movie4 = MOVIE("The conjuring", 112, "horror")
movie5 = MOVIE("Minha mãe é uma peça", 84, "comedy")
movie6 = MOVIE("Interestelar", 169, "science fiction")
movie7 = MOVIE("A viagem de Chihiro", 125, "fantasy")
movie8 = MOVIE("Saw", 103, "horror")
movie9 = MOVIE("Sonic: O filme", 99, "comedy")

def escolher_assento():
    assento = input("Escolha um assento: A1, A2, A3, B1, B2, B3, C1, C2, C3\n")
    print("Assento reservado!")


escolha = input("Escolha uma opção:\n[1] - Escolher cinema e filme\n ")
match escolha:
    case "1":
        sub_escolha = input("Escolha o cinema:\n[1] - Cinesystem\n[2] - Kinoplex\n[3] - Centerplex\n")
        match sub_escolha:
            case "1":
                sub_sub_escolha = input("Escolha o filme:\n[1] - Divergent\n[2] - Notting Hill\n[3] - The conjuring\n")
                match sub_sub_escolha:
                    case "1":
                        print(movie1.duration_in_minutes)
                        print(movie1.genre)
                        escolher_assento()
                    case "2":
                        print(movie3.duration_in_minutes)
                        print(movie3.genre)
                        escolher_assento()
                    case "3":
                        print(movie4.duration_in_minutes)
                        print(movie4.genre)
                        escolher_assento()
                    case _:
                        print("Opção inválida!")
            case "2":
                sub_sub_escolha = input("Escolha o filme:\n[1] - Toy story 1\n[2] - Minha mãe é uma peça\n[3] - Interestelar\n")
                match sub_sub_escolha:
                    case "1":
                        print(movie2.duration_in_minutes)
                        print(movie2.genre)
                        escolher_assento()
                    case "2":
                        print(movie5.duration_in_minutes)
                        print(movie5.genre)
                        escolher_assento()
                    case "3":
                        print(movie6.duration_in_minutes)
                        print(movie6.genre)
                        escolher_assento()
                    case _:
                        print("Opção inválida!")
            case "3":
                sub_sub_escolha = input("Escolha o filme:\n[1] - A viagem de Chihiro\n[2] - Saw\n[3] - Sonic: o filme\n")
                match sub_sub_escolha:
                    case "1":
                        print(movie7.duration_in_minutes)
                        print(movie7.genre)
                        escolher_assento()
                    case "2":
                        print(movie8.duration_in_minutes)
                        print(movie8.genre)
                        escolher_assento()
                    case "3":
                        print(movie9.duration_in_minutes)
                        print(movie9.genre)
                        escolher_assento()
                    case _:
                        print("Opção inválida!")
            case _:
                print("Opção inválida!")
        
    case _:
        print("Opção inválida!")