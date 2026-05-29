import os

# Declaração das Variáveis Globais
opcao = 0
usuarios = []
produtos = []
pedidos = []

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('Totem de Autoatendimento de Cafeteria/Lanchonete')
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
    print('1. Usuário')
    print('2. Produto')
    print('3. Pedido')
    print('4. Sair')

    opcao = input('Escolha a opção desejada: ')

    if(opcao == '1'):
        clear_screen()
        print('1. Novo Produto')
        print('2. Ver Produtos')
        print('3. Voltar')
        opcao = input('Escolha uma opção: ')
        if(opcao == '1'):
            clear_screen()
            print('NOVO PRODUTO')
            pnome = input('Digite o nome do produto: ')
            ppreco = input('Digite o preço do produto: ')
            pqtd = input('Digite a quantidade do produto: ')
            # Adicionar o produto à matriz
        elif(opcao == '2'):
            print('VER PRODUTOS')
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