#Parte 1 Ingesta Datos Con Diccionario
try:
    print('¿Cuantos Alumnos Son?')
    numalum=int(input())
    dicnotas={}
    for i in range(0,int(numalum),1):
        print(f'¿Ingrese el Nombre del Alumno numero {i+1}?')
        alumno=input()
        print(f'¿Ingrese la Nota del Alumno numero {i+1}?')
        nota=int(input())
        dicnotas.update({f'alumno{i}':alumno,f'nota{i}':nota})
        #dicnotas.update({alumno:nota})
except ValueError as e:
    print(f'Ocurrio un Problema, Solo debes de ingresar numeros')
except Exception as e:
    print(e.__class__.__name__)
    print(f'Ocurrio un Problema : {str(e)}')
finally:
    print('Se termino la ejecucion')

#Parte 2 Nota Mayor
notamayor=int(dicnotas.get(f'nota{0}'))
alumnomayor=''
for i in range(0,numalum,1):
    if int(dicnotas.get(f'nota{i}'))>=notamayor:
        notamayor=int(dicnotas.get(f'nota{i}'))
        alumnomayor=dicnotas.get(f'alumno{i}')
print(f'La Nota Mayor es:{notamayor} del alumno:{alumnomayor}')

#Parte 3 Nota Menor
notamenor=int(dicnotas.get(f'nota{0}'))
alumomenor=''
for i in range(0,numalum,1):
    if int(dicnotas.get(f'nota{i}'))<=notamenor:
        notamenor=int(dicnotas.get(f'nota{i}'))
        alumomenor=dicnotas.get(f'alumno{i}')
print(f'La Nota Menor es:{notamenor} del alumno:{alumomenor}')


#Parte 3 Nota Promedio
sumatoria=0
promedio=0
for i in range(0,numalum,1):
    sumatoria=int(dicnotas.get(f'nota{i}'))+sumatoria
promedio=sumatoria/numalum
print(f'El promedio de las Notas es:{promedio}')
    


