import numpy as np

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


# crear una lista vacia para ir guardando los productos y cantidades que el cliente desea
precios = []
cantidades = []
# crear una variable para controlar si el cliente desea seguir ordenando
seguir_ordenando = "si"

# crear un ciclo while para ejecutar el programa hasta que el cliente diga que ya no desea ordenar mas
while seguir_ordenando == "si":
    num = 1
    print('')
    for licor, precio in menu.items():
        precio = "{:,}".format(precio).replace(',','.')
        print(f'{num}. {licor}....valor: ${precio} pesos')
        num += 1
    print('')
    opcion = int(input("Digite el numero de la opcion que desea: "))
    try:
        precios.append(list(menu.values())[opcion-1])
        print('')
        num_prod = int(input("¿Que cantidad desea ordenar de este mismo producto?: "))
        cantidades.append(num_prod)
        print('')
        seguir_ordenando = input("Desea ordenar algo mas? (si/no): ")
    except:
        print('El producto no existe, porfavor elija una opcion valida')
        continue


# producto punto entre precios y cantidades, correspondiente al valor total de la cuenta.
suma = np.dot(precios,cantidades)

# suma = 0
# for i in range(len(precios)):
#     suma += (precios[i]*cantidades[i])

# imprimir el total de la cuenta
suma = "{:,}".format(suma).replace(',','.')
print('')
print(f'El valor de su cuenta es de: ${suma} pesos')