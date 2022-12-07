def soma(nums):
    soma = 0
    for num in nums:
        soma += num
    return soma
    

lista_numeros = []

while True:
    q = int(input('Digite o números a ser somado (0 encerra o programa): '))
    if q == 0:
        break
    else:
        lista_numeros.append(q)

s = soma(lista_numeros)

print(f'{s}')
