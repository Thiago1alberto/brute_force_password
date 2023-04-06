import string
import itertools
import concurrent.futures

def brute_force_password(password, min_length=1, max_length=8):
    for length in range(min_length, max_length + 1):
        for guess in itertools.product(string.ascii_letters + string.digits, repeat=length):
            guess_password = ''.join(guess)
            if guess_password == password:
                return guess_password
            else:
                print(f'\rTentando senha: {guess_password}', end='')
    return None

def parallel_brute_force_password(password, lengths):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(brute_force_password, password, min_length, max_length): (min_length, max_length) for min_length, max_length in lengths}
        for future in concurrent.futures.as_completed(futures):
            min_length, max_length = futures[future]
            try:
                guess_password = future.result()
                if guess_password:
                    return guess_password
            except Exception as exc:
                print(f'Erro na faixa de comprimento ({min_length}, {max_length}): {exc}')
    return None

# Solicita a senha ao usuário
password = input('Digite a senha: ')

# Define as faixas de comprimento de senha para verificar
length_ranges = [(1, 3), (4, 4), (5, 8)]

# Tenta adivinhar a senha por força bruta em paralelo
guess_password = parallel_brute_force_password(password, length_ranges)

if guess_password:
    print(f'\nSenha encontrada: {guess_password}')
else:
    print('\nNão foi possível adivinhar a senha')
