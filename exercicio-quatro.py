# 4) Faça um programa que receba dois argumentos, uma palavra/frase e uma letra. O programa deve retornar quantas vezes a letra apareceu na palavra/frase.

# Primeiro jeito de fazer:

palavra = input('Digite uma palavra: ')
letra = input('Digite uma letra: ')

print(f'A letra "{letra}" aparece {palavra.count(letra)} vezes na palavra "{palavra}".')

# Segundo jeito de fazer: 
outra_palavra = input('Digite uma palavra: ')
outra_letra = input('Digite uma letra: ')

contador = 0
for outra_letra in outra_palavra:
    if contador is outra_letra:
        contador = contador + 1

print(f'A letra "{outra_letra}" aparece {outra_palavra.count(outra_letra)} vezes na palavra "{outra_palavra}".')

# Terceiro jeito de fazer:



