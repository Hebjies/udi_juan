
"""
crear un codigo en python para un bar "La Sol Sed" que tenga un menu con las siguientes opciones:
1.Cervezas Colombianas
2.Cervezas Corona
3.Cerveza Coronita
4.Ron Medellin, Ron Caldas por 750 ml
5.Vodka smirnoff de lulo 750 ml
6.Whisky buchanans Master 750 ml
7.Aguardiente por 375  ml
8.Aguardiente por 750 ml
9.Aguardiente por 1000 ml
10.Aguardiente por 2000 ml
11.Smirnoff coctel
12.Mike coctel
13.Michelada clasica
14.Michelada con frutas
15.salir
El programa debe preguntar que desea ordenar, si desea algo mas y cuando el cliente diga que ya no desea nada mas,
debe mostrar el total de la cuenta.
"""
menu = {
        'Cerveza Colombiana':3000,
        'Cerveza Corona': 6000,
        'Cerveza Coronita': 4000,
        'Ron Medellin, Ron Caldas por 750 ml': 70000,
        'Vodka smirnoff de lulo 750 ml': 70000,
        'Whisky buchanans Master 750 ml': 200000,
        'Aguardiente por 375 ml': 40000,
        'Aguardiente por 750 ml': 75000,
        'Aguardiente por 1000 ml': 85000,
        'Aguardiente por 2000 ml': 140000,
        'Smirnoff coctel': 9000,
        'Mike coctel': 8000,
        'Michelada clasica': 7000,
        'Michelada con frutas': 9000
        }
num = 1
print('')
for licor, precio in menu.items():
    precio = "{:,}".format(precio).replace(',','.')
    print(f'{num}. {licor} | valor: ${precio} pesos')
    num += 1
print('')
#crear una lista vacia para ir guardando los productos que el cliente desea
productos = []

#crear una variable para controlar si el cliente desea seguir ordenando
seguir_ordenando = "si"

#crear un ciclo while para ejecutar el programa hasta que el cliente diga que ya no desea ordenar mas
# while seguir_ordenando == "si":
#     print("Bienvenido al Bar la Sol Sed, por favor seleccione una opcion del menu")
#     print("1.Cerveza Colombiana")
#     print("2.Cerveza Corona")
#     print("3.Cerveza Coronita")
#     print("4.Ron Medellin, Ron Caldas, Aguardiente Antioqueño por 1 litro")
#     print("5.Smirnoff 750 ml")
#     print("6.Whisky buchanans Master 750 ml")
#     print("7.Aguardiente por 375  ml")
#     print("8.Aguardiente por 750 ml")
#     print("9.Aguardiente por 1000 ml")
#     print("10.Aguardiente por 2000 ml")
#     print("11.Smirnoff coctel")
#     print("12.Mike coctel")
#     print("13.Michelada clasica")
#     print("14.Michelada de frutas")
#     # opcion = int(input("Digite el numero de la opcion que desea: "))
#     pedido = str(input('Escriba el producto que desea: '))
    # if opcion == 1:
    #     productos.append(precios[0])
    # elif opcion == 2:
    #     productos.append(precios[1])
    # elif opcion == 3:
    #     productos.append(precios[2])
    # elif opcion == 4:
    #     productos.append(precios[3])
    # elif opcion == 5:
    #     productos.append(precios[4])
    # elif opcion == 6:
    #     productos.append(precios[5])
    # elif opcion == 7:
    #     productos.append(precios[6])
    # elif opcion == 8:
    #     productos.append(precios[7])
    # elif opcion == 9:
    #     productos.append(precios[8])
    # elif opcion == 10:
    #     productos.append(precios[9])
    # elif opcion == 11:
    #     productos.append(precios[10])
    # elif opcion == 12:
    #     productos.append(precios[11])
    # elif opcion == 13:
#         print ("Con que cerveza desea la michelada?:1. ")
#         Cerveza= int (input("1. Nacional 2. Importada "))
#         if Cerveza == 1:
#             productos.append(precios[12]+3000)
#         else:
#             productos.append(precios[12]+4000)
#     elif opcion == 14:
#         print ("Con que cerveza desea la michelada?:1. ")
#         Cerveza= int (input("1. Nacional 2. Importada "))
#         if Cerveza == 1:
#             productos.append(precios[13]+3000)
#         else:
#             productos.append(precios[13]+4000)
#     elif opcion == 15:
#         break
#     else:
#         print("Opcion no valida")
#     seguir_ordenando = input("Desea ordenar algo mas? (si/no): ")

# #crear una variable para almacenar la suma de los precios de los productos
# suma = 0

# #crear un ciclo for para sumar los precios de los productos
# for producto in productos:
#     suma += producto

# #imprimir el total de la cuenta
# print("El total de la cuenta es: ", suma)