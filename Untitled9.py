suma =0 #acumulador
cant_edad=0#contador de edades
for edad in range (0,10):
    edad=int(input("ingrese la edad:"))
    suma=suma+edad
    cant_edad=cant_edad+1
promedio=suma/cant_edad
print("el promedio es:", promedio)