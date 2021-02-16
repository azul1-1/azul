palabra=input();

abecedario="abcdefghijklmnopqrstuvwxyz"

resultado=""

for i in range(0,len(palabra),1):

	indice=(abecedario.find(palabra[i])+2)
	if (indice<26 and indice>=2):
		resultado=resultado+abecedario[indice]
	elif(abecedario.find(palabra[i])==-1):
		resultado=resultado+palabra[i]
	else:
		resultado=resultado+palabra[i]



print(resultado)
