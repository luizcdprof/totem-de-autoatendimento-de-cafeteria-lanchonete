import os

# Declaração das Variáveis Globais
opcao = 0
usuarios = []
produtos = []
pedidos = []

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pressione_enter():
    input('Pressione ENTER para continuar...')

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
def show_menu(menu, opcoes = True):
    global opcao
    menu_line = '+----------------------------+'
    clear_screen()
    show_title()
    print(menu_line)

    if(menu == 'principal'):
        print('| 1. Usuário                 |')
        print('| 2. Produto                 |')
        print('| 3. Pedido                  |')
        print('| 0. Sair                    |')
    elif(menu == 'usuario'):
        print('| USUÁRIO                    |')
        print(menu_line)
        print('| 1. Novo Usuário            |')
        print('| 2. Ver Usuários            |')
        print('| 0. Voltar                  |')
    elif(menu == 'novo_usuario'):
        print('| NOVO USUÁRIO               |')
    elif(menu == 'listar_usuarios'):
        print('| VER USUÁRIOS               |')
    elif(menu == 'produto'):
        print('| PRODUTO                    |')
        print(menu_line)
        print('| 1. Novo Produto            |')
        print('| 2. Ver Produtos            |')
        print('| 0. Voltar                  |')
    elif(menu == 'novo_produto'):
        print('| NOVO PRODUTO               |')
    elif(menu == 'listar_produtos'):
        print('| VER PRODUTOS               |')
    elif(menu == 'pedido'):
        print('| PEDIDO                     |')
        print(menu_line)
        print('| 1. Novo Pedido             |')
        print('| 2. Ver Pedidos             |')
        print('| 0. Voltar                  |')
    elif(menu == 'novo_pedido'):
        print('| NOVO PEDIDO                |')
    elif(menu == 'listar_pedidos'):
        print('| VER PEDIDOS                |')
    else:
        pass

    print(menu_line)
    if opcoes:
        opcao = input('Escolha a opção desejada: ')

def cadastrar(tipo):
    if(tipo == 'usuarios'):
        codigo = len(usuarios) + 1
        nome = input('Digite o nome do usuário: ')
        email = input('Digite o e-mail do usuário: ')
        # Adicionar o usuário à matriz caso não exista
        usuarios.append([codigo, nome, email])
    elif(tipo == 'produtos'):
        codigo = len(produtos) + 1
        nome = input('Digite o nome do produto: ')
        quantidade = float(input('Digite a quantidade do produto: '))
        valor = float(input('Digite o valor do produto: '))
        # Adicionar o produto à matriz
        produtos.append([codigo, nome, quantidade, valor])
    elif(tipo == 'pedidos'):
        numero = len(pedidos) + 1
        usuario = int(input('Digite o código do usuário: '))
        produto = int(input('Digite o código do produto: '))
        quantidade = float(input('Digite a quantidade do pedido: '))
        # Adicionar o pedido à matriz
        pedidos.append([numero, usuario, produto, quantidade])

def listar(tipo):
    if(tipo == 'usuarios'):
        for usuario in usuarios:
            print(f'código {usuario[0]} - {usuario[1]} - {usuario[2]}')
    elif(tipo == 'produtos'):
        for produto in produtos:
            print(f'código {produto[0]} - {produto[1]} - {produto[2]}')
    elif(tipo == 'pedidos'):
        for pedido in pedidos:
            print(f'pedido {pedido[0]} - usuário {usuarios[pedido[1]-1][1]} - produto {produtos[pedido[2]-1][1]} - qtd = {pedido[3]}')
    else:
        print('Não há valores a exibir...')
        pressione_enter()

while True:
    show_menu('principal')

    if(opcao == '1'): # Opção "Usuário" do menu principal
        show_menu('usuario')
        if(opcao == '1'): # Opção "Novo Usuário" do menu "Usuário"
            show_menu('novo_usuario', False)
            cadastrar('usuarios') 
        elif(opcao == '2'): # Opção "Listar Usuários" do menu "Usuário"
            show_menu('listar_usuarios', False)
            listar('usuarios')
            pressione_enter()
        elif(opcao == '0'): # Opção "Voltar" do menu "Usuário"
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '2'): # Opção "Produto" do menu principal
        show_menu('produto')
        if(opcao == '1'): # Opção "Novo Produto" do menu "Produto"
            show_menu('novo_produto', False)
            cadastrar('produtos') 
        elif(opcao == '2'): # Opção "Listar Usuários" do menu "Produto"
            show_menu('listar_produtos', False)
            listar('produtos')
            pressione_enter()
        elif(opcao == '0'): # Opção "Voltar" do menu "Produto"
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '3'): # Opção "Pedido" do menu principal
        show_menu('pedido')
        if(opcao == '1'): # Opção "Novo Pedido" do menu "Pedido"
            show_menu('novo_pedido', False)
            cadastrar('pedidos') 
        elif(opcao == '2'): # Opção "Listar Pedidos" do menu "Pedido"
            show_menu('listar_pedidos', False)
            listar('pedidos')
            pressione_enter()
        elif(opcao == '0'): # Opção "Voltar" do menu "Pedido"
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '0'): # Opção "Sair" do menu principal
        break
    else:
        print('Opção inválida! Digite uma opção do menu...')

clear_screen()
print('O programa foi encerrado.')