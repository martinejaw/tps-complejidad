from os import system
import time
def menu():
	print("===============================================================")
	print("||                                                           ||")
	print("||                     1_ Comenzar                           ||")
	print("||                     2_ Salir                              ||")
	print("||                                                           ||")
	print("===============================================================")


def id_producto(lineas, pos):

	cont = 0
	for i in range(len(lineas)):
		cont += 1
		if lineas[pos][i] == ",":
			break

	id_prod = lineas[pos][cont+1:cont+1+4]
	if "," in id_prod:
		id_prod = lineas[pos][cont+1:cont+1+3] #Tomo el id de producto en el caso de que el id este comprendido entre 100 y 999
		if "," in id_prod:
			id_prod = lineas[pos][cont+1:cont+1+2] #Tomo el id de producto en el caso de que el id este comprendido entre 10 y 99

			if "," in id_prod:
				id_prod = lineas[pos][cont+1:cont+1+1] #Tomo el id de producto en el caso de que el id este comprendido entre 0 y 9

	
	return id_prod


def cantidad(lineas, pos):

	cont = 0
	cont_comas = 0
	for i in range(len(lineas[pos])):
		cont += 1
		if lineas[pos][i] == "," and cont_comas < 3:
			cont_comas += 1
		elif cont_comas == 3:
			break

	cantidad = lineas[pos][cont:cont+2]
	if "]" in cantidad:
		cantidad = lineas[pos][cont:cont+1]

	cantidad = int(cantidad) #Lo convierto a entero puesto que despues necesito preguntar si es mayor o igual a un numero
	return cantidad


archivo = open("Articulos por Sucursal 10k - Ordenado.txt", "r")
lineas = archivo.readlines()
archivo.close()

menu()

ingreso = input()

lista_final = []


if ingreso == "1":

	horaComienzo = time.perf_counter()
	id_prod_respaldo = id_producto(lineas, 0)

	hayCero = False
	hayCinco = False
	for i in range(len(lineas)):
		
		if id_prod_respaldo == id_producto(lineas, i):
			if cantidad(lineas, i) == 0:
				hayCero = True
			elif cantidad(lineas, i) > 5:
				hayCinco = True

		else:
			if hayCero and hayCinco:
				lista_final.append(id_prod_respaldo)
			
			hayCero = False
			hayCinco = False
			id_prod_respaldo = id_producto(lineas, i)
			if cantidad(lineas, i) == 0:
				hayCero = True
			elif cantidad(lineas, i) > 5:
				hayCinco = True
			
	system("cls")
	print("Tiempo: ",time.perf_counter()-horaComienzo)
	for i in range(len(lista_final)):
		print("ID Producto:", lista_final[i], '\n')
	print("Cantidad de IDs encontrados: ",len(lista_final))
	a = input()
elif ingreso == "2":
	system("cls")
	print("Aprobamos? Supongo que si xd")
