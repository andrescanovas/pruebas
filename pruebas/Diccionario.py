# -------------------------------------DICCIONARIOS---------------------------------------
#  los diccionarios se manejan con el formato NOMBRE_DICCIONARIO = {CLAVE:VALOR,CLAVE:VALOR,CLAVE:VALOR}


diccionario = {1:'Canox',5:'mikase',2:'goku',3:'vegeta',4:'gohan'}



# for personas in diccionario:
#     print(personas,diccionario[personas])



# for persona in diccionario.values():          -----------> es lo mismo que lo de arriba
#     print(persona)


# for personas in diccionario:
#     print(diccionario[personas])







# ------------------------------------------------DICCIONARIO DENTRO DE UN DICCIONARIO--------------------------------------------------

diccionarios = {1:{'nombre':'Canox','altura':180,'edad':28,},2:{'nombre':'Sofi','altura':160,'edad':28,},3:{'nombre':'Pablo','altura':170,'edad':28,},4: {'nombre':'Mikasa','altura':160,'edad':28,}}

# 



for personas in diccionarios:
    print(personas,diccionarios[personas]['altura'])


# LO DE ARRIBA MUESTRA DICCIONARIOS SUB DICCIONARIOS


# ----------------------------------------------------------------------------------------------------------------------------------------







