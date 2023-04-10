def fibonacci(numeroFornecido):
    a = 0
    b = 1
    while b <= numeroFornecido:
        if b == numeroFornecido:
            return True
        a, b = b, a + b
    return False


numero_Fornecido = 13
if fibonacci(numero_Fornecido):
    print('O número fornecido faz parta da sequência de Fibonacci!')
else:
    print('O número fornecido não faz parta da sequência de Fibonacci!')

numero_Fornecido = 92
if fibonacci(numero_Fornecido):
    print('O número fornecido faz parta da sequência de Fibonacci!')
else:
    print('O número fornecido não faz parta da sequência de Fibonacci!')
