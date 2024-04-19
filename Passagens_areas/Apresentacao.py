# MENU DE OPÇÕES
def mostra_menu():
    print("==" * 50)
    print(
        "Informe a opão desejada: \n"
        "Digite 1 para comprar passagens \n"
        "Digite 2 para listar passagens \n"
        "Digite 3 para sair do programa \n"
    )
    print("==" * 50)
    print()


def menu_compra_passagem():
    print("Opçãoselecionada: comprar de passagens")
    origem = input("Informe a origem? ")
    destino = input("Informe o destino? ")
    preço = float(input("Informe o preço? "))
    
    return origem, destino, preço

def lista_passagens(passagens_compradas):
    for indice, passagem in enumerate(passagens_compradas):
        print(f"{indice+1}) {passagem}")