nome = input('digite seu nome:')
idade = input('digite idade:')
email =input('digite email:')

user = {
    'nome' : nome,
    'idade' : idade,
    'email' : email
}

idade = int (user['idade'])

if idade > 18:
    print('maior de 18')

else:
    print('menor de 18')