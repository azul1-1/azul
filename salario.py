
print("inserte salario por hora: ")
salario=input()
if salario.isnumeric()==False:
	print("inserte valor numerico: ")
	salario=input()

print("inserte horas trabajadas")
horas=input()

if horas.isnumeric()==False:
	print("inserte valor numerico: ")
	horas=input()

if int(horas)<8:
	total=int(horas)*float(salario)
	print(total)

elif int(horas)>8:
	total=8*float(salario)+((int(horas)-8)*float(salario)*2)
	print(total)