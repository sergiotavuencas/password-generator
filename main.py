import random

# Letras, números e símbolos que serão inclusos na geração da senha
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '0123456789'
symbols = '!@#$%¨&*_+-=\\|<,.>:;?`^~()/[]{}'

# Quais serão inclusos, ou seja, se não quer símbolos, bastas mudar para False a variável symbs
upper, lower, digit, symbs = True, True, True, True

all = '' # Variável onde serão armazenados os caracteres

# Armazenamento dos caracteres
if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if digits:
    all += digits
if symbols:
    all += symbols
    
length = 20 # Quantidade de caracteres na senha
amount = 10 # Quantidade de senhas a serem geradas

'''
    Digamos que você queira gerar uma senha, mas não quer anotar,
    grave uma palavra na sua mente, ou anote essa palavra em algum lugar
    e armazene em seed, isso fará com que o programa sempre gere
    as mesmas senhas.
'''
# seed = 'teste'
# random.seed(seed)

for x in range(amount):
    password = ''.join(random.sample(all, length))
    
print(password)