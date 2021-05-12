# num = input('ingrese su numero: ')

# while not num.isdigit():
#     print('pone un numero pelotudo: ')
#     num = input('ingrese su NUUUUMEROOOO: ')
#     print('bien boludo biieeeen')

# En el codigo de arriba solicita un numero, sino lo es "not num.isdigito" osea pusiste una letra, te vulve a pedir numero hasta que lo ingreses


acumulador = 0
ciclo = 0

cantidad_de_numeros = int(input('Ingrese cuantos numeros desea ingresar'))

while ciclo < cantidad_de_numeros:
    numero = int(input('ingrese un numero: '))
    acumulador += numero
    ciclo += 1
    print(acumulador)
print('El total es: ',acumulador)


# El codigo de arriba es un acumulador

# --------------------------------------------------------------------------------------------------------


datos = ['ana','andres','sofia']
contador = 0

while contador < 3:
    nombres_para_agregar = input('ingrese un nombre: ')
    agregar(datos, nombres_para_agregar)
    contador += 1
    
    print(datos)

# El codigo de arriba permite agregar 3 nombres 


