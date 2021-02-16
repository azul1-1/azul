


#-----insertar caracteres

print("inserte la palabra")
palabra=input()

#--- funcion que analiza si letra es una vocal o no
a=int(0)
e=int(0)
b=int(0)
o=int(0)
u=int(0)


#--- se analiza la palabra con un bucle
for i in range(0,len(palabra),1):
	
	if palabra[i].lower()=='a':
		a=a+1
	elif palabra[i].lower()=='e':
		e=e+1
	elif palabra[i].lower()=='i':
		b=b+1
	elif palabra[i].lower()=='o':
		o=o+1
	elif palabra[i].lower()=='u':
		u=u+1

print("a: ",a)
print("e: ",e)
print("i: ",b)
print("o: ",o)
print("u: ",u)


#--- resultado final



	

    