def mostrar_menu():
    menu = ["========== MENÚ PRINCIPAL ==========", 
            "1. Cupos por género", 
            "2. Búsqueda de películas por rango de precio", 
            "3. Actualizar precio de película", 
            "4. Agregar película", 
            "5. Eliminar película", 
            "6. Salir", 
            "=" * 36]
    for opcion in menu:
        print(opcion)

def leer_opcion():
    try:
        opcion = int(input("\nIngrese opcion:\n-> "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("¡Valor fuera de las opciones!")
            return
    except ValueError:
        print("¡Valor no entero!")
        return
    
def validar_codigo(peliculas, cartelera, codigo):
    if codigo in peliculas:
        return False

    if len(codigo) == 0 or codigo == "":
        return False
    
    return True

def validar_titulo(titulo):
    return len(titulo) != 0

def validar_genero(genero):
    return len(genero) != 0

def validar_duracion(duracion):
    try:
        duracion = int(duracion)
        return duracion > 0
    except ValueError:
        return False 

def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ["A", "B", "C"]

def validar_idioma(idioma):
    return len(idioma) != 0

def validar_3d(valor):
    return valor.lower() in ["s", "n"] 

def validar_precio(precio):
    try:
        precio = int(precio)
        return precio > 0
    except ValueError:
        return False 
    
def validar_cupos(cupos):
    try:
        cupos = int(cupos)
        return cupos >= 0
    except ValueError:
        return False 
    
##Funciones principales