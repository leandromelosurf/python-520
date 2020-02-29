import os
from sys import platform
from random import randint

## Inicializa a lista de amigos que vão participar do sorteio
amigos = []

## Preenche a lista de amigos que vão participar do sorteio
qtd_amigos = int(input("Quantos amigos seu grupo possui? "))
for i in range(qtd_amigos):
    amigo = input("Qual o nome do {0}º amigo? ".format(i+1))
    amigos.append({'id': i+1, 'nome': amigo})

## Inicializa a lista onde ficará o resultado do sorteio
sorteio = []


def sortear(sorteando, amigos, sorteados, sorteio, contador):
    ## Verifica se a quantidade de chamadas recursivas não está próxima
    ## de ultrapassar a quantidade máxima
    ## Se estiver, retornamos False para recomeçar o sorteio
    contador += 1
    if contador > 900:
        return False

    ## Sorteia um amigo
    sorteado = amigos[randint(0,qtd_amigos-1)]

    ## Verifica se o amigo sorteado já não foi sorteado por outro
    requisito_1 = (sorteado['id'] in sorteados)
    ## Verifica se o amigo sorteado já não sorteou quem o está sorteando
    ## Só evita aquelas coisas chatas de um sair com o outro e o outro com o um
    ## É opcional, você pode remover :)
    requisito_2 = ([x for x in sorteio if x['sorteante'] == sorteando['id'] and \
    x['sorteado'] == sorteando['id']])
    ## Verifica se quem sorteia não sorteou ele mesmo
    requisito_3 = (sorteado['id'] == sorteando['id'])

    if (requisito_1 or requisito_2 or requisito_3):
        ## Se qualquer um dos requisitos acima for verdadeiro
        ## realiza-se o sorteio novamente até que encontre um resultado satisfatório
        sortear(sorteando, amigos, sorteados, sorteio, contador)
    else:
        ## Se não, adicionamos o resultado do sorteio na lista de resultados
        sorteio.append({'sorteante': sorteando['id'], 'sorteado':sorteado['id']})
        return True

## Enquanto a função sortear retornar False e não tiver um sorteio satisfatório
## o sorteio será realizado novamente
while len(sorteio) != qtd_amigos:
    sorteio = []
    for rodada in range(qtd_amigos):
        ## O sorteio é feito um por um e sempre conferido

        sorteados = [x['sorteado'] for x in sorteio]
        ## Contador de chamadas recursivas
        contador = 0

        sortear(amigos[rodada], amigos, sorteados, sorteio, contador)

## Abre arquivo txt de resultado e escreve "Resultado do sorteio nele"
file = open("resultado.txt", "w")
file.write("Resultado do sorteio: \n")

## Divulga o resultado do sorteio
for rodada in sorteio:
    for amigo in amigos:
        if rodada['sorteante'] == amigo['id']:
            sorteante = amigo['nome']
        elif rodada['sorteado'] == amigo['id']:
            sorteado = amigo['nome']

    ## Sempre que um novo resultado for exibido, a tela da linha de comando é
    ## limpa de forma que o próximo amigo não veja o sorteado pelo anterior
    ## Não queremos estragar a surpresa né ;)
    if platform == 'linux2' or platform == 'darwin' or platform == 'linux':
        os.system("clear")
    elif platform == 'win32' or platform == 'cygwin':
        os.system("cls")

    input("Por favor, chame o amigo {0} e pressione ENTER para ver quem ele sorteou.".format(sorteante))
    input("Você sorteou o amigo: {0}\n\nPressione ENTER para continuar.".format(sorteado))

    ## Escreve no arquivo resultado.txt "Fulando sorteou Ciclano"
    file.write("{0} sorteou {1}\n" .format(sorteante, sorteado))

## Fecha o arquivo resultado.txt
file.close()
print("Sorteio encerrado. Divirta-se!")