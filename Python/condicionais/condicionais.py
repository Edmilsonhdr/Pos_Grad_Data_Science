# Operadores Lógicos:
# and: Verdadeiro se ambas as condições forem verdadeiras
# or: Verdadeiro se pelo menos uma condição for verdadeira
# not: Inverte o valor lógico

# Operadores de Comparação:
# == : Igual a
# != : Diferente de
# > : Maior que
# < : Menor que
# >= : Maior ou igual a
# <= : Menor ou igual a


idade = int(input('Digite sua idade:'))


# IF
if idade > 18:
    print("É maior de idade")
elif idade == 18:
    print("É Guerreiro Jedi")
else:
    print("É MENOR de idade")


#TERNARIO
idadeAtual = 18
print("É MAIOR") if idadeAtual >= 18 else print("É maior")


nome = 'Marcio'
match nome:
    case 'Antonio':
        print("Não é Marcio")
    case 'Pedro':
        print("Não é Pedro")
    case 'Marcio':
        print("Achou o Marcio")