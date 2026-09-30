#numero inteiro 7 -1 : int
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))

s = n1 + n2
print("A soma de {0} e {1} é {2}".format(n1, n2, s))

#numero real 3.14 2.71 : float
n3 = float(input("Digite um valor: "))
print(n3)
print(type(n3)) #verifica o tipo da variável

#numero verdadeiro (True False) : bool
n4 = bool(input("Digite um valor: "))
print(n4)
print(type(n4)) #verifica o tipo da variável

#numero texto "Olá, mundo!" : str
n5 = str(input("Digite um valor: "))
print(n5)
print(type(n5)) #verifica o tipo da variável
print(n5.isnumeric()) #verifica se o valor é um número
print(n5.isalpha()) #verifica se o valor é uma letra
print(n5.isalnum()) #verifica se o valor é uma letra ou número
print(n5.isupper()) #verifica se o valor é uma letra maiúscula
print(n5.islower()) #verifica se o valor é uma letra minúscula
print(n5.isspace()) #verifica se o valor é um espaço em branco
print(n5.istitle()) #verifica se o valor é um título
print(n5.startswith("Olá")) #verifica se o valor começa com "Olá"
print(n5.endswith("mundo!")) #verifica se o valor termina com "mundo!"
print(n5.replace("Olá", "Oi")) #substitui "Olá" por "Oi"
print(n5.upper()) #converte o valor para maiúscula
print(n5.lower()) #converte o valor para minúscula  
print(n5.capitalize()) #converte o valor para maiúscula a primeira letra
print(n5.title()) #converte o valor para maiúscula a primeira letra de cada palavra
print(n5.strip()) #remove os espaços em branco do início e do fim
print(n5.lstrip()) #remove os espaços em branco do início
print(n5.rstrip()) #remove os espaços em branco do fim
print(n5.split()) #divide o valor em uma lista de palavras
print(n5.splitlines()) #divide o valor em uma lista de linhas
print(n5.join("Olá, mundo!")) #junta o valor com uma string
print(n5.find("mundo")) #verifica se o valor contém "mundo"
print(n5.count("o")) #verifica quantas vezes o valor contém "o"
print(n5.index("mundo")) #verifica a posição do valor "mundo"
print(n5.rindex("mundo")) #verifica a posição do valor "mundo" da direita para a esquerda
print(n5.replace("mundo", "Python")) #substitui "mundo" por "Python"
pr
