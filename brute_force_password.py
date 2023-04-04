import random
import string
import itertools

"""
def generate_password(length=8):
    # Gera uma senha aleatória com letras minúsculas, maiúsculas e dígitos
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))
    
"""

def brute_force_password(password, max_length=8):
    # Tenta adivinhar a senha por força bruta
    for length in range(1, max_length + 1):
        for guess in itertools.product(string.ascii_letters + string.digits, repeat=length):
            guess_password = ''.join(guess)
            if guess_password == password:
                return guess_password
            else:
                print(f'\rTentando senha: {guess_password}', end='')
    return None

# Solicita a senha ao usuário
password = input('Digite a senha: ')

# Tenta adivinhar a senha por força bruta
guess_password = brute_force_password(password)

if guess_password:
    print(f'\nSenha encontrada: {guess_password}')
else:
    print('\nNão foi possível adivinhar a senha')
