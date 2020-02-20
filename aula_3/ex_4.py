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

def verificar_se_e_email(email):
	contador = 0
    for letra in email:
        if letra == '@':
            contador = contador + 1
    return True if contador == 1 else False

for email in emails:
	if verificar_se_e_email(email):
		print('é um email mesmo')
	else:
		print('num é não')
