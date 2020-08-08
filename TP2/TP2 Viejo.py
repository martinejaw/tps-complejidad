from os import system
from time import sleep 
import time
def menu():
	print("===============================================================")
	print("||                                                           ||")
	print("||               1_ Comenzar                                 ||")
	print("||               2_ Cargar Articulo por Sucursal             ||")
	print("||               3_ Salir                                    ||")
	print("||                                                           ||")
	print("===============================================================")


archivo = open("Articulos por Sucursal 10k.txt", "r")
lineas = archivo.readlines()
archivo.close()

bandera = "s"
while bandera == "s":
	system("cls")
	menu()
	opcion = input()
	if opcion == "1":
		horaComienzo = time.perf_counter()
		todos_cero = []
		todos_id_art_cero = []
		todos_mayor5 = []
		todos_id_art_mayor5 = []

		for i in range(len(lineas)):
			espacios = 0
			band = True
			control = 0
			for j in range(len(lineas[i])):
				if lineas[i][j] == " " :
					espacios += 1

				#--------- Obtengo el id de articulo ----------#
				
				if espacios == 1 and control == 0:
					cont = 0
					
					while True:
						if lineas[i][j+cont] == ",":
							id_art_0 = lineas[i][j+1:cont+j]
							id_art_mayor5 = lineas[i][j+1:cont+j]
							control = 1
							break
						cont += 1	
				#---------------------------------------------#
				
				if (espacios == 3 and band) and lineas[i][j-1] == " ":
					#--------- Obtengo los articulos cuya cantidad es 0 ----------#
					if lineas[i][j] == "0":
						todos_id_art_cero.append(id_art_0)
						band = False
						
					else:
						#--------- Obtengo los articulos cuya cantidad es mayor a 5 ----------#
						if ((lineas[i][j] in ["1","2","3","4","5"]) and (lineas[i][j+1] in ["0","1","2","3","4","5","6","7","8","9"])) or (lineas[i][j] in ["6","7","8","9"]):
							todos_id_art_mayor5.append(id_art_mayor5)
							band = False
		

		#-------Elimino los duplicados-------#
		ceros = set(todos_id_art_cero)
		ceros = list(ceros)
		mayor5 = set(todos_id_art_mayor5)
		mayor5 = list(mayor5)

		#-------Verifico que existan articulos cuya cantidad es 0 en algunas sucursales y mayor que 5 en otras ----#
		lista_final = []
		for i in range(len(ceros)):
			if ceros[i] in mayor5:
				lista_final.append(ceros[i])


		system("cls")
		print("Tiempo: ",time.perf_counter()-horaComienzo)
		for i in range(len(lista_final)):
			print('ID Producto: ',lista_final[i],'\n')

		print("Cantidad de IDs encontrados: ",len(lista_final),'\n')
		a = input("Presione cualquier tecla para volver al menu principal")

	elif opcion == "2":
	
		system("cls")
		print("Es de vital importancia cargar los datos con el siguiente formato \n")
		print("'[id, id_articulo, id_sucursal, cantidad]'\n")
		datos = input()
		lineas.append(datos)
		print("\nInformación cargada con éxito...")
		sleep(0.5)
	elif opcion == "3":
		bandera = ""
	