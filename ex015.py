kmP = float(input('Kilômetros percorridos pelo cliente: '))
diasAluguel = float(input('Total de dias que o veículo foi alugado: '))
precoCarro = 60 * diasAluguel
precokmP = 0.15 *kmP
print('O preço total à ser pago pelo cliente é de: R$', precoCarro + precokmP)
