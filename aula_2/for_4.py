

numerais = ['0', '1' ,'2', '3', '4,','5','6','7','8','9']

idade = input('digite sua idade:')

for letra in idade:
    if letra in numerais:
        print('digitou um numero')
    else:
        print('digitou uma letra')
