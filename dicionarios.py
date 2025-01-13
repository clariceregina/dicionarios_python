'''
Exercício: Mini Tradutor
Crie um programa que:
Armazene palavras e suas traduções em um dicionário.
Ofereça ao usuário as seguintes opções:
Adicionar uma palavra e sua tradução.
Traduzir uma palavra.
Exibir todas as palavras cadastradas e suas traduções.
Remover uma palavra do dicionário.
Atualizar a tradução de uma palavra existente.
'''

# instrução que importa o módulo OS da biblioteca padrão
import os
 
# função de retorno ao menu principal
def voltar_menu_principal():
    # Detecta o sistema operacional e limpa a tela corretamente
    if os.name == 'nt':  # para Windows
        os.system('cls')
    else:  # para sistemas Unix (Linux/macOS)
        os.system('clear')


def encerrar_programa():
    print("Programa encerrado!")
    exit()

# armazenar palavras e tradução
tradutor = {
    'hug': 'abraço',
    'grazie': 'obrigada/o'
}

# menu
def menu():
    print(
        '''MENU:
1. Traduzir uma palavra
2. Adicionar uma palavra e sua tradução
3. Exibir todas as palavras cadastradas e sua tradução
4. Atualizar a tradução de uma palavra existente
5. Remover uma palavra do tradutor
6. Encerrar''')

# pessoa usuária insere opção desejada
def escolher():
    while True:
        voltar_menu_principal()
        menu()
        opcao_desejada = input('\nSelecione a opção desejada: ')

        # opção 1 - traduzir uma palavra
        if opcao_desejada == '1':
            palavra = input('Insira a palavra para tradução: ')
            if palavra in tradutor:
                print(f'A tradução de "{palavra}" é "{tradutor[palavra]}".')
            else:
                print(f'A palavra "{palavra}" não foi encontrada no tradutor. Recomendamos adicioná-la na opção 2 do Menu.')

        # opção 2 - adicionar uma palavra e sua tradução
        elif opcao_desejada == '2':
            palavra_nova = input('Insira a palavra a ser traduzida: ')
            traducao_nova = input(f'Insira a tradução de "{palavra_nova}": ')
            tradutor[palavra_nova] = traducao_nova
            print(f'A tradução de "{palavra_nova}" foi adicionada com sucesso!')

        # opção 3 - exibir as palavras cadastradas e sua tradução
        elif opcao_desejada == '3':
            print('As palavras cadastradas e suas respectivas traduções são:\n')
            for p, t in tradutor.items():
                print(p + ' : ' + t)

        # opção 4 - atualizar a tradução de uma palavra existente
        elif opcao_desejada == '4':
            palavra_atualizar = input('Insira a palavra a ser atualizada: ')
            traducao_atualizar = input(f'Insira a tradução atualizada de "{palavra_atualizar}": ')
            if palavra_atualizar in tradutor:
                tradutor[palavra_atualizar] = traducao_atualizar
                print('Atualização realizada com sucesso!')
                print(tradutor)
            else:
                print(f'A palavra {palavra_atualizar} não consta no tradutor. Recomendamos adicioná-la na opção 2 do Menu.')

        # opção 5 - remover uma palavra do tradutor
        elif opcao_desejada == '5':
            deletar = input('Insira a palavra a ser deletada: ')
            if deletar in tradutor:
                del tradutor[deletar]
                print(f'A palavra "{deletar}" foi deletada com sucesso!')
            else:
                print(f'A palavra {deletar} não consta no tradutor.')

        # opção 6 - encerrar programa
        elif opcao_desejada == '6':
            encerrar_programa()

        # opção escolhida inválida
        else:
            print('Opção inválida! Insira um número de 1 a 6.')
            voltar_menu_principal()
