# 3) Faça um programa que receba uma temperatura em graus Celsius e retorne ela em Fahrenheit. A fórmula de conversão é:
                            # F = (C * 9/5) + 32

graus_em_celcius = float(input('Quantos ºC está hoje? '))

formula_fahrenheit = (graus_em_celcius * 9/5) + 32

print(f'Os graus em Fahrenheit é: {formula_fahrenheit} ºC')