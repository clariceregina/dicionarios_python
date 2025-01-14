#Exercício: Mini Tradutor
#Crie um programa que:
#Armazene palavras e suas traduções em um dicionário.
#Ofereça ao usuário as seguintes opções:
#Adicionar uma palavra e sua tradução.
#Traduzir uma palavra.
#Exibir todas as palavras cadastradas e suasss traduções.
#Remover uma palavra do dicionário.
#Atualizar a tradução de uma palavra existente.

def menu():
    print(
        '''MENU:
1. Traduzir uma palavra
2. Adicionar uma palavra e sua tradução
3. Exibir todas as palavras cadastradas e sua tradução
4. Atualizar a tradução de uma palavra existente
5. Remover uma palavra do tradutor''')

def escolher():
    opcao_desejada = input('\nSelecione a opção desejada: ')
    if opcao_desejada == '1':
        traduzir_palavra()
    elif opcao_desejada == '2':
        adicionar_palavra()
    elif opcao_desejada == '3':
        exibir_palavras()
    elif opcao_desejada == '4':
        atualizar_traducao()
    elif opcao_desejada == '5':
        deletar_palavra()
    else:
        print('Opção inválida! Insira um número de 1 a 5.')

# armazenar palavras e tradução
tradutor = {
    'hug': 'abraço',
    'grazie': 'obrigada/o'
}

def traduzir_palavra():
    palavra = input('Insira a palavra para tradução: ')
    if palavra in tradutor:
        print(f'A tradução de "{palavra}" é "{tradutor[palavra]}".')
        print(exibir_palavras())
    else:
        print(f'A palavra "{palavra}" não foi encontrada no tradutor. Recomendamos adicioná-la na opção 2 do Menu.')

def adicionar_palavra():
    palavra_nova = input('Insira a palavra a ser traduzida: ')
    traducao_nova = input(f'Insira a tradução de "{palavra_nova}": ')
    tradutor[palavra_nova] = traducao_nova
    print(f'A tradução de "{palavra_nova}" foi adicionada com sucesso!')
    print(exibir_palavras())

def exibir_palavras():
    print('\nAs palavras cadastradas e suas respectivas traduções são:')
    for p, t in tradutor.items():
        print(f'{p} : {t}')

def atualizar_traducao():
    palavra_atualizar = input('Insira a palavra a ser atualizada: ')
    if palavra_atualizar in tradutor:
        traducao_atualizar = input(f'Insira a tradução atualizada de "{palavra_atualizar}": ')
        tradutor[palavra_atualizar] = traducao_atualizar
        print('Atualização realizada com sucesso!')
        print(exibir_palavras())
    else:
        print(f'A palavra {palavra_atualizar} não consta no tradutor. Recomendamos adicioná-la na opção 2 do Menu.')


def deletar_palavra():
    deletar = input('Insira a palavra a ser deletada: ')
    if deletar in tradutor:
        del tradutor[deletar]
        print(f'A palavra "{deletar}" foi deletada com sucesso!')
        print(exibir_palavras())
    else:
        print(f'A palavra {deletar} não consta no tradutor.')

menu()
escolher()
