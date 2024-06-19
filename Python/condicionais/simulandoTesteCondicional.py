#Um algoritimo que:
#peça ao usuario para digitar o seu ano de nascimento, o ano atual, descubra se o usuario é maior de idade
#se for, pede o titulo de eleitor dele
#senão, pede um documento do responsavel.


anoNascimento = int(input('Digitar o seu ano de nascimento:'))
anoAtual = int(input('Digitar o ano atual:'))
idade = anoAtual - anoNascimento

if idade >= 18:
    tituloLeitor = input('Digite seu titulo de eleitor:')
else:
    tituloLeitor = input('Digite o documento do responsavel:')