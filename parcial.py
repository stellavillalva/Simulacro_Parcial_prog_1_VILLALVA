def mostrar_menu_ppal(opcion: int)-> str:
    """esta funcion muestra el menu principal del sistema.
    argumentos: opcion >> int
    retornos:  menu >> str
    """ 
    print("""bienvenido al sistema de administracion de 'empire inventory'
       ingrese una opcion de interes:
       1-Cargar producto/s. 
       2-Buscar producto. 
       3-Ordenar inventario. 
       4-Mostrar producto más caro y más barato. 
       5-Mostrar productos con precio mayor a 15000. 
       6-Salir""") 
    return opcion

#2. Cargar inventario: 
#• Desarrollar una función que permita al usuario ingresar los datos del o los 
#productos en una matriz (nombre, precio, cantidad).  
#• El sistema debe permitir al usuario ingresar la cantidad deseada de productos. 

def cargar_inventario():
    inventario = []
    while True:
            nombre_prod = input("ingrese nombre del producto: ")
            precio = float(input(f"ingrese precio de {nombre_prod}: $"))
            cantidad_prod = int(input("ingrese cantidad de producto: "))
            producto = [nombre_prod, precio, cantidad_prod]
            inventario.append(producto)    

            continuar = input("desea agregar mas? (s/n): ")
            if continuar == "n":
                    print(inventario)
                    break 
            
            
    