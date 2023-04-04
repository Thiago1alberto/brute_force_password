# Brute Force Password
Este é um programa simples que tenta adivinhar uma senha por força bruta, utilizando todas as combinações possíveis de caracteres.
- Tentativa por força bruta é uma técnica utilizada para descobrir uma senha ou chave criptográfica através da geração sistemática de todas as possíveis combinações de caracteres até encontrar a senha correta.
# Como funciona
O programa utiliza a biblioteca itertools para gerar todas as combinações possíveis de caracteres, em ordem crescente de tamanho. Em seguida, ele testa cada combinação gerada até encontrar a senha correta.

# Uso
Ao executar o programa, o usuário será solicitado a digitar a senha que deseja adivinhar. O programa, então, tentará adivinhar a senha utilizando a abordagem de força bruta. Se a senha for encontrada, o programa exibirá a senha na tela. Caso contrário, ele exibirá a mensagem "Não foi possível adivinhar a senha".

# Limitações
Esse programa é uma implementação básica de força bruta e não é otimizado para lidar com senhas muito longas ou complexas. Além disso, é importante ressaltar que tentar adivinhar senhas sem autorização pode ser considerado um crime
- é importante ressaltar que a tentativa por força bruta pode ser extremamente custosa em termos de recursos computacionais, especialmente se a senha em questão for complexa ou muito longa. Dependendo da complexidade da senha e da capacidade do computador utilizado, pode levar dias, semanas ou até mesmo meses para que uma senha seja descoberta por força bruta.

```python Digite a senha: abc123
Senha encontrada: abc123
Tempo de execução: 4.54 segundos

Digite a senha: senha
Senha encontrada: senha
Tempo de execução: 2.29 segundos

Digite a senha: 1234
Senha encontrada: 1234
Tempo de execução: 0.52 segundos

Digite a senha: 123456
Senha encontrada: 123456
Tempo de execução: 0.63 segundos

Digite a senha: abcde
Senha encontrada: abcde
Tempo de execução: 0.72 segundos 
