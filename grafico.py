#array = ["A","(","B","(","E","(K","L"),"C","(","G",")"(","H","("M","),"I","J",")",")",")"]
array = str (input("Ingrese una cadena: "))  
arbol = list(array)
tamaño = len(array)
nivelop = array.count("(")
nivelcls = array.count(")")
fila = 0
j = 0
aux1 = 0
c = 0
profundidad = 0
print("Cadena: ",arbol)
if nivelop == nivelop:
    for i in range(tamaño):
        if arbol[i] == "(":            
            aux1 = fila
            fila += 1 
            aux1 = fila
            c += 1
            print("Fila: ", fila ,"Valor: ", arbol[i] , "Token: Símbolo de agrupación")
        if arbol[i] == ")":
            print("Fila: ", aux1 ,"Valor: ", arbol[i] , "Token: Símbolo de agrupación")
            fila -= 1
            aux1 = fila
        if arbol[i] != "(" and arbol[i] != ")" and arbol[i] != "," and arbol[i] != "." and arbol[i] != " ":
            j += 1
            print("Fila: ", aux1 ,"Valor: ", arbol[i] , "Token: id", j)
    print("Filas totales: ",c)
else :
    print("error sintactico")