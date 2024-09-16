import os

banner = """
    ███████╗███████╗████████╗██╗   ██╗██████╗ 
    ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
    ███████╗█████╗     ██║   ██║   ██║██████╔╝
    ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
    ███████║███████╗   ██║   ╚██████╔╝██║     
    ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
    """

def info_maker(quantidade:int,palavras:str):
    palavras = palavras.split(",")
    tamanho = ""

    print("         ╔════(1) " + palavras[0])
    print("         ║")

    for i in range(1, len(palavras) - 1):
        print(f"         ╠════{tamanho + "═"}({i + 1}) {palavras[i]}")
        print("         ║")
        tamanho = tamanho + "══"

    print(f"         ╚═══╦═════{tamanho}({len(palavras)}) {palavras[-1]}")
    print("             ║")
    return "             ╚═══>"



def limpar():
    os.system('cls')
    print(banner)

def adicionar_ficheiro(resposta:int,ficheiro:str):
    pass
def remover_ficheiro(resposta:int,ficheiro:str):
    pass

def abrir_apps(resposta:int,ficheiro:str):
    pass

def add_remove(resposta:int,ficheiro:str):
    if (resposta == 1):
        abrir_apps()
    elif (resposta == 2):
        adicionar_ficheiro()
    elif (resposta == 3):
        remover_ficheiro()


print(banner)
resposta = int(input(info_maker(3,"Setup gaming,Setup programing,Criar setup")))

if(resposta == 1):
    limpar()
    resposta = int(input(info_maker(3,"Abrir,Adicionar,Remover")))
    add_remove(resposta, "a")

elif(resposta == 2):
    limpar()

    resposta = int(input(info_maker(2,"Default,python")))

    if(resposta == 1):
        limpar()

        resposta = int(input(info_maker(3,"Abrir,Adicionar,Remover")))
        add_remove(resposta,"a")

    elif(resposta == 2):
        limpar()

        resposta = int(input(info_maker(3,"Abrir,Adicionar,Remover")))
        add_remove(resposta,"a")

