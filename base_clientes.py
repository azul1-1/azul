from tkinter import *

#importar cuadros de mensajes:

from tkinter import messagebox

raiz=Tk()

miFrame1=Frame(raiz)

miFrame1.pack()

miFrame1.config(background="blue")


#crear menu
barraMenu=Menu(raiz)

raiz.config(menu=barraMenu, width=350, height=350)


#-----------creacion de pantalla

ecuacion=StringVar()

pantalla=Entry(miFrame1,text=ecuacion)
pantalla.grid(row=1,column=1,padx=10,pady=5,columnspan=5)
pantalla.config(background="black",fg="green",justify=("left"), width=30)

raiz.config(bg="red")


#-----------creacion de pantalla ecuacion

ecu=StringVar()

pantalla_ecu=Entry(miFrame1,text=ecu)

pantalla_ecu.grid(row=8,column=1,padx=10,pady=5,columnspan=5)
pantalla_ecu.config(background="black",fg="green",justify=("left"), width=30)


#-----------creacion de pantalla resultado

result=StringVar()

pantalla_result=Entry(miFrame1,text=result)

pantalla_result.grid(row=10,column=1,padx=10,pady=5,columnspan=5)
pantalla_result.config(background="black",fg="green",justify=("left"))

#-----------Funcion para resultado:


def separar():

	s=ecu.get().split("+")
	listdatos=[]


	for i,y in enumerate(s):


		if y.count("x")==1:

			p=y.split("x")
			listdatos.append(p[0])

		elif y.count("=")==1:

			p=y.split("=")
			listdatos.append(p[0])
			listdatos.append(p[1])
		

	return listdatos

    
def solucion():

    try:

	     l=separar()

	     a=float(l[0])
	     b=float(l[1])
	     c=float(l[2])-float(l[3])

	     a1=(b**2-(4*a*c))**0.5
	     a2=(b**2-(4*a*c))

	     r1=(-b+a1)/(2*a)
	     r2=(-b-a1)/(2*a)

	     if a2<0:
	     	result.set("no existe")
	     else:
	        result.set("x1= "+str(r1)+"x2= "+str(r2))

    except:
    	 result.set("error")



	
#-----------Funcion para borrar:


def borrartotal():

	ecuacion.set("")
	ecu.set("")
	result.set("")
	  
	    	
	      

	    

	




#-----------Funcion para botones:


def numeropulsado(num):

	ecuacion.set(ecuacion.get()+num)

#funcion para borrar (del):

def borrar():
	s=ecuacion.get()

	ecuacion.set(s[0:len(s)-1])


#funcion para colocar la ecuacion en pantalla:


def ecuacionPantalla():

	if ecu.get()=="":
		ecu.set(ecuacion.get()+"x2+")
		ecuacion.set(" ")
		
	elif (ecu.get().count("+"))==1:
		ecu.set(ecu.get()+ecuacion.get()+"x+")
		ecuacion.set(" ")

	elif (ecu.get().count("+"))==2 and (ecu.get().count("="))==0 :
		ecu.set(ecu.get()+ecuacion.get()+"=")
		ecuacion.set(" ")
	else:
		ecu.set(ecu.get()+ecuacion.get())
		ecuacion.set(" ")
		





	







#-----------creacion de botones:

#-----------fila 1:

boton7=Button(miFrame1,text="7",width=3,command=lambda:numeropulsado("7"))
boton7.grid(row=2,column=1)

boton8=Button(miFrame1,text="8",width=3,command=lambda:numeropulsado("8"))
boton8.grid(row=2,column=2)

boton9=Button(miFrame1,text="9",width=3,command=lambda:numeropulsado("9"))
boton9.grid(row=2,column=3)

#-----------fila 2:

boton6=Button(miFrame1,text="6",width=3,command=lambda:numeropulsado("6"))
boton6.grid(row=3,column=1)

boton5=Button(miFrame1,text="5",width=3,command=lambda:numeropulsado("5"))
boton5.grid(row=3,column=2)

boton4=Button(miFrame1,text="4",width=3,command=lambda:numeropulsado("4"))
boton4.grid(row=3,column=3)


#-----------fila 3:

boton3=Button(miFrame1,text="3",width=3,command=lambda:numeropulsado("3"))
boton3.grid(row=4,column=1)

boton2=Button(miFrame1,text="2",width=3,command=lambda:numeropulsado("2"))
boton2.grid(row=4,column=2)

boton1=Button(miFrame1,text="1",width=3,command=lambda:numeropulsado("1"))
boton1.grid(row=4,column=3)

#-----------fila 4:

botonDecimal=Button(miFrame1,text=".",width=3,command=lambda:numeropulsado("."))
botonDecimal.grid(row=5,column=1)

boton0=Button(miFrame1,text="0",width=3,command=lambda:numeropulsado("0"))
boton0.grid(row=5,column=2)

botonDel=Button(miFrame1,text="Del",width=3, command=lambda:borrar())
botonDel.grid(row=5,column=3)

#-----------fila 5:

botonsiguiente=Button(miFrame1,text="siguiente",width=6, command=lambda:ecuacionPantalla())
botonsiguiente.grid(row=6,column=1)


botonborrar=Button(miFrame1,text="borrar",width=6, command=lambda:borrartotal())
botonborrar.grid(row=6,column=2)

botonmenos=Button(miFrame1,text="-",width=6, command=lambda:numeropulsado("-"))
botonmenos.grid(row=6,column=3)
#-----------fila 6:

botoncalcular=Button(miFrame1,text="calcular",width=6, command=lambda:solucion())
botoncalcular.grid(row=7,column=1)


#-----------configuracion barra archivo

archivoMenu=Menu(barraMenu, tearoff=0)


archivoMenu.add_command(label="nuevo")
archivoMenu.add_command(label="abrir")
archivoMenu.add_command(label="guardar")
archivoMenu.add_command(label="guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="salir")
#-----------configuracion barra edicion
archivoEdicion=Menu(barraMenu, tearoff=0)


archivoEdicion.add_command(label="calcular",command=solucion)
archivoEdicion.add_command(label="almacenar resultado")
archivoEdicion.add_command(label="cambiar modelo")
archivoEdicion.add_separator()
archivoEdicion.add_command(label="salir")
#creacion de cuadro de archivo


barraMenu.add_cascade(label="archivo",menu=archivoMenu)
barraMenu.add_cascade(label="edicion",menu=archivoEdicion)




raiz.mainloop()