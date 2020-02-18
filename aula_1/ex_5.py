usuario = {
    'nome': input('Digite nome:'),
    'idade': input('Digite idade:'),
    'email': input('Digite email:')
}

if int(idade) > 18:
    print('ola')
else:
    print('bloqueado')

print(usuario)
print(usuario['nome'])
print(usuario['idade'])
print(usuario['email'])
