


class Usuario:

    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade
        
usuario = Usuario(id=1, nome='leandro', idade=34)
usuario_2 = Usuario(id=1, nome='leandro2', idade=34)
print(usuario.id)
print(usuario.nome)
print(usuario.idade)