def operecion_matematica_Suma(numero1,numero2):
    '''Es una simple operacion de suma'''
    return numero1 + numero2




def operecion_matematica_Suma_resta(numero1,numero2):
    ''' Es una Funcion para sumar y restar dos numeros de forma separada'''
    return numero1 + numero2, numero1 - numero2


def listado(conjunto_datos):
    '''Es una funcion para mostrar personas en un conjunto de datos e imprime persona'''
    for persona in conjunto_datos:
        print(persona)

def agregar(lista,valor):
    '''Es una funcion para agregar un valor a la lista'''
    lista.append(valor)




# datos = ['ana','andres','sofia']


# print(listado(datos))


# num1 = int(input('ingrese su primer numero: '))
# num2 = int((input('ingrese su segundo numero: ')))

# print('El resultado es: 'operecion_matematica_Suma(num1, num2))

# *************************************************************************************************

# num1 = int(input('ingrese su primer numero: '))
# num2 = int((input('ingrese su segundo numero: ')))

# total, diferencia = operecion_matematica_Suma_resta(num1, num2)

# print('El resultado es de la resta entre esos numeros es: ',diferencia,'   y el total de esos numeros es:',total)

# El codigo de arriba sirve para poder realizar una suma y una resta con el mismo grupo de numeros 
# ----------------------------------------------------------------------------------------------------------------------------------------



datos = ['ana','andres','sofia']
contador = 0

while contador < 3:
    nombres_para_agregar = input('ingrese un nombre: ')
    agregar(datos, nombres_para_agregar)
    contador += 1
    
print(datos)


# El codigo de arriba se usa la funcion agregar para agragar en la lista datos nombres en este caso con While y el contador serian 3 



