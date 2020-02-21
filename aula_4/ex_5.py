import string
import re
import datetime


print(string.ascii_lowercase)
print(string.ascii_uppercase)

hoje = datetime.datetime.now()
daqui_trinta_dias = hoje + datetime.timedelta(30)

print(daqui_trinta_dias)