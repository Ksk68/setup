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

    if quantidade == 1:
        print(f"""
           ╔════(1){palavras[0]}
           ╚═══╗""")
        return "               ╚═══>"

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

def add_remove(resposta:int,ficheiro:str):
    if (resposta == 1):#abrir
        abrir_apps(ficheiro)
    elif (resposta == 2):#editar
        os.startfile(fr"{ficheiro}")



def abrir_apps(ficheiro:str):

    with open(ficheiro, 'r', encoding='utf-8') as arquivo:
        print(f"\n                  Abrindo arquivo: {ficheiro}")
        while True:
            hiperligacao = arquivo.readline().strip()

            if not hiperligacao:
                input("\n                  Clique Enter para fechar")
                break


            print(f"                  Abrindo: {hiperligacao}")
            try:
                os.startfile(hiperligacao)
            except FileNotFoundError:
                print(f"Erro: Arquivo ou caminho não encontrado: {hiperligacao}")
            except OSError as e:
                print(f"Erro do sistema ao tentar abrir {hiperligacao}: {e}")
            except Exception as e:
                print(f"Ocorreu um erro ao abrir {hiperligacao}: {e}")




def criar_setup(nome_setup:str):
    pass

def ler_hiper():
    txt = r"C:\Users\raulm\Documents\github projects\setup\pythonProject1\hiperligações.txt"
    nomes = ""
    hiperligacoes = []
    quantidade = 0
    sair = False
    with open(txt, 'r', encoding='utf-8') as arquivo:
        while sair != True:
            nome = arquivo.readline().strip()
            if not nome:
                sair = True
            else:
                if quantidade == 0:
                    nomes = nome
                else:
                    nomes = nomes + "," + nome
                hiperligacao = arquivo.readline().strip()
                hiperligacoes.append(hiperligacao)
                quantidade = quantidade + 1
    return nomes,hiperligacoes,quantidade


#main

default_text = "Abrir,Adicionar,Remover"
setups_nomes,setups_hiperligacoes,quantidade_setups = ler_hiper()

print(banner)

setup_type = int(input(info_maker(quantidade_setups,setups_nomes)))

limpar()
resposta = int(input(info_maker(2,"Abrir,Editar")))
add_remove(resposta,fr"{setups_hiperligacoes[setup_type - 1]}")


