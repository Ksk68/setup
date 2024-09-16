


def banner():
    print("""███████╗███████╗████████╗██╗   ██╗██████╗ 
    ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
    ███████╗█████╗     ██║   ██║   ██║██████╔╝
    ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
    ███████║███████╗   ██║   ╚██████╔╝██║     
    ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
    """)

def adicionar_ficheiro(resposta,ficheiro):
    pass

def remover_ficheiro(resposta,ficheiro):
    pass

def abrir_apps(resposta,ficheiro):
    pass

def add_remove(resposta,ficheiro):
    if (resposta == 1):
        adicionar_ficheiro()
    elif (resposta == 2):
        remover_ficheiro()
    elif (resposta == 3):
        abrir_apps()

def clear():
    try:
        import os
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)

banner()
resposta = int(input("""                                        
         ╔════(1) setup jogos                             
         ║
         ╚══╦═════(2) setup programação
            ║
            ╚═══> """))


if(resposta == 1):
    print("??")
elif(resposta == 2):
    clear()
    resposta = int(input("""                                        
             ╔════(1) default                   
             ║
             ╚══╦═════(2) python
                ║
                ╚═══> """))

    if(resposta == 1):
        resposta = int(input("""                                        
                     ╔════(1) adicionar                   
                     ║
                     ╚══╦═════(2) remover
                        ║
                        ╚═══> """))
        add_remove(resposta,"a")
    elif(resposta == 2):
        resposta = int(input("""                                        
                             ╔════(1) adicionar                   
                             ║
                             ╚══╦═════(2) remover
                                ║
                                ╚═══> """))
        add_remove(resposta,"a")

