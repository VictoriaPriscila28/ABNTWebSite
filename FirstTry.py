list=[]
#SOBRENOME, Nome. Título: subtítulo (se houver). Edição (se houver). Local de publicação: Editora, ano de publicação da obra.
'insira os dados abaixo e em seguida sua referencia estara pronta'

nome= str(input('insira o nome e sobrenome do autor:')).strip().split()
titulo=str(input('digite o titulo da obra:'))
edicao= str(input('digite o numero da edição com o final ed:'))
lugar=str(input('digite o local em que foi publicado:'))
ano=int(input('digite o ano da publicação:'))
print('sua referencia vai ficar:',nome[1],nome[0],titulo,edicao,lugar,ano,)

