frase = 'Curso em Vídeo Python   '
print(frase[3]) #imprime a patir do caractere 3
print(frase[3:13]) #imprime do caractere 3 atè o 12
print(frase[:13]) #imprime do inicio ate o 12
print(frase[3:])#imprime do 3 até o final
print(frase[1:15:2]) #imprime do 1 até o 14 pulando 2 em 2
print(frase[::2])#imprime do inicio até o fim pulando 2 em 2
print("""Isto é um texto longo para usar aparecer da mesma
        forma como está formatado aqui,
        respeitando a formatação, para isso basta
        utilizar aspas tripla""") #imprime texto sem perder a formatação
print(frase.count('o'))#faz a contagem da letra especificada
print(frase.count('O'))#faz a contagem da letra especificada
print(frase.upper().count('O'))#transforma as string em maiuscula e faz a contagem da letra especificada
print(len(frase))#imprime a quantidade de letras que há na variavel
print(len(frase.strip()))#desconsidera espaços vazios no inicio e fim
frase = frase.replace('Python', 'Android')#substitue a a palavra especificada
print(frase)
print('Curso' in frase)#Faz um pesquisa se existe tal palavra e retorna true ou false
print(frase.find('em'))#mostra a posição que e palavra està
print(frase.find('Python'))#caso não encontre a palavra, se retorna -1
print(frase.find('Android'))#mostra a posição que e palavra està
print(frase.find('android'))#caso não encontre a palavra, se retorna -1
print(frase.lower().find('vídeo'))#Transforma todas a letras em minusculo e mostra a posisao da palavra especificada
print(frase.split())#imprime a frase separada por aspas
dividido = frase.split()
print(dividido[0])#imprime a primeira palavra
print(dividido[3][1])#Pega a terceira palavra e imprime a posicao da string especificada
