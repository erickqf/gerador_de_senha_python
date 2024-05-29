from secrets import SystemRandom
import string

def analisar_tipo(valor:str):
    if valor.isdigit():
        return True
    else:
        return False
def gerar_senha(qnt_caracteres:int):
    random=SystemRandom()
    senha=''.join([random.choice(caracteres_especiais),random.choice(letras_minusculas),random.choice(letras_maiusculas),SystemRandom().choice(digitos)])
    senha+=''.join(random.choices(caracteres_juntos,k=qnt_caracteres-4))
    lista_senha=[i for i in senha]
    random.shuffle(lista_senha)
    return ''.join(lista_senha)

tipo_input=False
qnt_caracteres=0

#Aqui estou criando variaveis para criar as senhas aleatorias
global caracteres_especiais,letras_minusculas,letras_maiusculas,digitos,caracteres_juntos
caracteres_especiais=string.punctuation
letras_minusculas=string.ascii_lowercase
letras_maiusculas=string.ascii_uppercase
digitos=string.digits
caracteres_juntos=''.join([caracteres_especiais,letras_minusculas,letras_maiusculas,digitos])

print("A sua senha terá quantos caracteres? Insira abaixo somente números")
while not tipo_input:
    resposta_usuario=input()
    tipo_input=analisar_tipo(resposta_usuario)
    if not tipo_input:
        print("Insira somente números inteiros")
    else:
        qnt_caracteres=int(resposta_usuario)
        if qnt_caracteres<8:
            print("Sua senha é muito fraca. Insira um valor maior que 7")
            tipo_input=False
        else:
            senha_gerada=gerar_senha(qnt_caracteres)
            print(f'Sua senha é: \n{senha_gerada}')
