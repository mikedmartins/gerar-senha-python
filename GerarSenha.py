import string
import random

while True:
    tamanho = int(input('Digite a quantidade de caracteres da senha: '))
    print('Digite 1 somente letras minusculas')
    print('Digite 2 para letras minuscolas e maiusculas')
    print('Digite 3 para letras e números')
    print('Digite 4 para letras, números e caracteres')
    tipo = int(input())

    if tipo == 1:
        valores = string.ascii_lowercase
        break
    elif tipo == 2:
        valores = string.ascii_letters
        break
    elif tipo == 3:
        valores = string.ascii_letters + string.digits
        break
    elif tipo == 4:
        valores = string.ascii_letters + string.digits + string.punctuation
        break
    else:
        print('Digite uma alternativa válida.')

senha = ''.join(random.choice(valores) for _ in range(tamanho))
print(senha)
