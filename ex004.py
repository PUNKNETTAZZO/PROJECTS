# Captar do usuário um objeto
n = input("Digite algo: ")


# Função dos tradutores
def tradutor_booleano(tipo):
    if tipo == True:
        return str('Verdadeiro')
    else:
        return str('Falso')


def tradutor_type(tipo):
    if tipo == str:
        return 'Caractere'
    elif tipo == int:
        return 'Inteiro'
    elif tipo == float:
        return 'Flutuante'
    elif tipo == bool:
        return 'Booleano'


# Criação dos tipos
type = type(n)
num = n.isnumeric()
alfnum = n.isalnum()
alf = n.isalpha()
upper = n.isupper()
lower = n.islower()

# Tradução dos tipos
tipo = tradutor_type(type)
numpt = tradutor_booleano(num)
alfnumpt = tradutor_booleano(alfnum)
alfpt = tradutor_booleano(alf)
upperpt = tradutor_booleano(upper)
lowerpt = tradutor_booleano(lower)

# Retorno dos tipos do objeto digitado
print(
    f"O tipo do objeto digitado é {tipo} \nO objeto digitado é numérico? {numpt}\nO objeto digitado é alfanumérico? {alfnumpt}\nO objeto digitado é alfabético? {alfpt}\nO objeto digitado está todo em letras maiúsculas? {upperpt}\nO objeto digitado está todo em letras minúsculas? {lowerpt}")
