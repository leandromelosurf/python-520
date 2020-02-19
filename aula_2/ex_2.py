emails = [
	'petyfezygniyg@msddvqiytmpogire',
	'yjozbkgirsfchbjtlnigqqeohaj',
	'axukkfdcpemkruogaemqlcyfngun',
	'czmymzvhdyfltqe@rktzjljbs',
	'@yoeisikhawyno@b',
	'dfeydhfnlydwrlvpmsomi',
	'xogsqaxph@btippxiz',
	'hxkuqlyxreuwfzwypvw',
	'togaczelhzijnafhyg@czp@f',
	'jxtmqikapfv@uqqckowiz@hyi',
]

for email in emails:
    contador = 0
    for letra in email:
        if letra == '@':
            contador = contador + 1
    if contador == 1:
        print('Digitou um email válido')
    else:
        print('Não digitou um email')