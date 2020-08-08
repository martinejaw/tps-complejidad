import math
import time
import collections


def primeFactors(n): 
    resta = n
    factores=[]
    multi = 1
    #  Imprime el numero de 2 que divide n
    while n % 2 == 0: 
        factores.append(2)
        n = n / 2
    # n deberia ser impar aca 
    # asi que puedo hacer un salto de 2 ( i = i + 2) 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        while n % i== 0: 
            factores.append(i)
            n = n / i
        
              
    # Cndicion si f es un primo 
    # mayor que 2
    if n > 2: 
        factores.append(n)
    
    frec= collections.Counter(factores)
    #Todas estas lineas comentadas que siguen, eran para pruebas
    #print(factores)
    #print(frec)
    #for valor in frec:
     #   print(frec[valor])
    #print(len(frec))

    for valor in frec:
        multi*=(pow(valor,frec[valor]+1)-1)/(valor-1)
    return int(multi-resta)


def primeFactors2(n): 
    resta = n
    factores=[]
    multi = 1
    i=0
    while n!=1 and arrayprimos[i]<math.sqrt(n): 
        while n%arrayprimos[i]==0:
            factores.append(arrayprimos[i])
            n = n / arrayprimos[i]
        i+=1
    # Cndicion si f es un primo 
    # mayor que 2
    if n > 2: 
        factores.append(n)
    
    frec= collections.Counter(factores)
    #Todas estas lineas comentadas que siguen, eran para pruebas
    #print(factores)
    #print(frec)
    #for valor in frec:
     #   print(frec[valor])
    #print(len(frec))
    for valor in frec:
        multi*=(pow(valor,frec[valor]+1)-1)/(valor-1)
    return int(multi-resta)

def amigos(limit):
    for x in range(220,limit):
        if(x % 2 ==0 or x%5 ==0):
            di=primeFactors2(x)
            if(di > x and di <= limit):
                dj=primeFactors2(di)
                if(dj==x):
                    salida.append([x,di])
    return salida

def amigos2(limit):
    start = time.time()
    for x in range(220,limit):
        if(x % 2 ==0 or x%5 ==0):
            di=primeFactors(x)
            if(di > x and di <= limit):
                dj=primeFactors(di)
                if(dj==x):
                    salida.append([x,di])
    end= time.time()
    print('Tiempo: ',end-start)
    return salida

def primosff(num,pr):
    div=0
    while pr[div]<num:
        if num%pr[div]==0:
            return False
        else:
            if pr[div]>math.sqrt(num):
                return True
            else:
                div+=1

limite = int(input('Limite: '))
salida=[]
start = time.time()
if limite>=150000:

	prim=3
	arrayprimos=[2,3]
	while prim<math.sqrt(limite)+1:
		prim=prim+2
		if primosff(prim,arrayprimos):
			arrayprimos.append(prim)

	print(amigos(limite))

	end= time.time()
	print('Tiempo: ',end-start)

else:
	print(amigos2(limite))

