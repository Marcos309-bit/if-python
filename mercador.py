


def menu():
    print("Você encontrou um mercador de poções")
    print("Seja Bem vindo ao mercador de poções!")
    print("************************itens************************")
    print("Item 1: Poção de vitalidade, Preço: 150 moedas")
    print("Item 2: Poção de magia, Preço: 200 moedas ")
    print("Item 3: Poção Elemental, Preço: 250 moedas")
    print("Item 4: Adaga Afiada, Preço: 250 moedas")
    print("Item 5: Arco de Caça, Preço: 250 moedas")

def escolha():
    moedas = 450.0
    resposta = 'S'
    while resposta == 'S' and moedas > 0:


        escolha = input("Escolha um item: \n")

        if escolha == '1':
            moedas -= 150.0
            print("Compra realizada com sucesso!")
            print(f"Ainda restam {moedas} moedas \n")

        elif escolha == '2':
            moedas -= 200.0
            print("Compra realizada com sucesso!")
            print(f"Ainda restam {moedas} moedas \n")

        elif escolha == '3':
            moedas -= 250.0
            print("Compra realizada com sucesso!")
            print(f"Ainda restam {moedas} moedas \n")

        elif escolha == '4':
            moedas -= 250.0
            print("Compra realizada com sucesso!")
            print(f"Ainda restam {moedas} moedas \n")

        elif escolha == '5':
            moedas -= 250.0
            print("Compra realizada com sucesso!")
            print(f"Ainda restam {moedas} moedas \n")

        resposta = input("Deseja contnuar comprando? [S] ou [N] \n").upper()

def caminho():

    guerreiro = input(f"Qual o nome do guerreiro? \n")

    print(f"Enquanto o guerreiro {guerreiro} seguia seu caminho , entrou em um empasse: ")

    caminho = input(f"qual caminho você escolheria? esquerda ou direita? \n")

    if caminho == "direita":
        menu()
        escolha()

    else:
        print("Continue colhendo material e siga seu caminho")


caminho()

