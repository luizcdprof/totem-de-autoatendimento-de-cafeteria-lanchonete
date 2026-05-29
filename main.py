import os

# Declaração das Variáveis Globais
opcao = 0
usuarios = []
produtos = []
pedidos = []

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir o Logotipo
def show_title():
    print('''
        ███████████ █████                  ███████████           █████                            
        ░█░░░███░░░█░░███                  ░█░░░███░░░█          ░░███                             
        ░   ░███  ░  ░███████    ██████    ░   ░███  ░   ██████  ███████    ██████  █████████████  
            ░███     ░███░░███  ███░░███       ░███     ███░░███░░░███░    ███░░███░░███░░███░░███ 
            ░███     ░███ ░███ ░███████        ░███    ░███ ░███  ░███    ░███████  ░███ ░███ ░███ 
            ░███     ░███ ░███ ░███░░░         ░███    ░███ ░███  ░███ ███░███░░░   ░███ ░███ ░███ 
            █████    ████ █████░░██████        █████   ░░██████   ░░█████ ░░██████  █████░███ █████
            ░░░░░    ░░░░ ░░░░░  ░░░░░░        ░░░░░     ░░░░░░     ░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░ 
    ''')

# Função para exibir os menus
def show_menu(menu):
    global opcao
    clear_screen()

    if(menu == 'principal'):
        print('1. Usuário')
        print('2. Produto')
        print('3. Pedido')
        print('0. Sair')
    elif(menu == 'usuario'):
        print('### Usuário ###')
        print('1. Novo Usuário')
        print('2. Ver Usuários')
        print('0. Voltar')
    else:
        pass

    opcao = input('Escolha a opção desejada: ')

while True:
    show_title()
    show_menu('principal')

    if(opcao == '1'): # Opção "Usuário" do menu principal
        show_menu('usuario')
        if(opcao == '1'):
            clear_screen()
            print('### NOVO USUÁRIO ###')
            nome = input('Digite o nome do usuário: ')
            email = input('Digite o e-mail do usuário: ')
            # Adicionar o usuário à matriz
            usuarios.append([nome, email])
        elif(opcao == '2'):
            print('### VER USUÁRIOS ###')
            for usuario in usuarios:
                print(f'{usuario[0]} - {usuario[1]}')
            input('Pressione ENTER para continuar...')
        elif(opcao == '3'):
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '2'):
        clear_screen()
        print('Carrinho')
    elif(opcao == '3'):
        clear_screen()
        print('Em desenvolvimento...')
    elif(opcao == '4'):
        break
    else:
        print('Opção inválida! Digite uma opção do menu...')

clear_screen()
print('O programa foi encerrado.')