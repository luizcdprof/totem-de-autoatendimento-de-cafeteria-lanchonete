import os

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
    print('1. Produtos')
    print('2. Carrinho')
    print('3. ')
    print('4. Sair')

    opcao = input('Escolha a opção desejada: ')

    if(opcao == '1'):
        os.system('cls')
        print('1. Novo Produto')
        print('2. Ver Produtos')
        print('3. Voltar')
        opcao = input('Escolha uma opção: ')
        if(opcao == '1'):
            os.system('cls')
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
        os.system('cls')
        print('Carrinho')
    elif(opcao == '3'):
        os.system('cls')
        print('Em desenvolvimento...')
    elif(opcao == '4'):
        break
    else:
        print('Opção inválida! Digite uma opção do menu...')

os.system('cls')
print('O programa foi encerrado.')