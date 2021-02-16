


#-----insertar caracteres

print("inserte la palabra")
palabra=input()

#--- funcion que analiza si letra es una vocal o no
def funcionAbecedario(letra):
	vocales=['a','e','i','o','u']
	for y in range(0,len(vocales),1):
		if vocales[y]==letra.lower():
			return True


#--- se analiza la palabra con un bucle
for i in range(0,len(palabra),1):

#--- resultado final
	if funcionAbecedario(palabra[i])!=True:
		print(palabra[i].lower())


if funcionAbecedario(palabra[len(palabra)-1])==True:
		print("la ultima es una vocal")
else: 
	print("la ultima letra no es vocal")



	

    