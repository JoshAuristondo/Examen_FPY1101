def mostrar_menu():
    menu = ["\n========== MENÚ PRINCIPAL ==========", 
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
        opcion = int(input("\nIngrese opcion: "))
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

def validar_3d(es_3d):
    return es_3d.lower() in ["s", "n"] 

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

def cupos_por_genero(peliculas, cartelera, genero):
    total = 0

    for codigo in peliculas:
        if peliculas[codigo][1].upper() == genero.upper():
            total += cartelera[codigo][1]
    
    if total != 0:
        print(f"El total de cupos disponibles es: {total}")
        return

    print(f"No hay cupos para [{genero}]")

def buscar_por_rango(peliculas, cartelera, p_min, p_max):
    lista = []
    for codigo in cartelera:
        precio = cartelera[codigo][0]
        cupos = cartelera[codigo][1]
        if precio <= p_max and precio >= p_min and cupos != 0:
            nombre = peliculas[codigo][0]
            lista.append(nombre + "--" + codigo)

    lista.sort()

    if len(lista) != 0:
        print(f"\nResultados de busqueda entre [{p_min} - {p_max}]:")
        for pelicula in lista:
            print(pelicula)
    else:
        print("No hay películas en ese rango de precios.")

def buscar_codigo(peliculas, cartelera, codigo):
    return codigo in peliculas
     
def actualizar_precio(peliculas, cartelera, codigo, precio):
    if not buscar_codigo(peliculas, cartelera, codigo):
        return False
    
    if not validar_precio(precio):
        return False
    
    cartelera[codigo][0] = precio
    return True
    
def agregar_pelicula(peliculas, cartelera, codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):

    if buscar_codigo(peliculas, cartelera, codigo):
        return False

    peliculas[codigo] = [
        titulo,
        genero,
        int(duracion),
        clasificacion.upper(),
        idioma,
        es_3d.lower() == "s"
    ]

    cartelera[codigo] = [
        int(precio),
        int(cupos)
    ]

    return True

def eliminar_pelicula(peliculas, cartelera, codigo):
    if not buscar_codigo(peliculas, cartelera, codigo):
        return False

    del peliculas[codigo]
    del cartelera[codigo]
    return True
    
def main():
    peliculas = {}
    cartelera = {}

    opcion = 0

    while opcion != 6:
        mostrar_menu()
        opcion = leer_opcion()
        match opcion:
            case 1:
                if len(peliculas) == 0:
                    print("\nNo hay peliculas\n")
                else:
                    genero = input("Ingrese género a consultar: ")
                    cupos_por_genero(peliculas, cartelera, genero) 
            case 2:
                if len(peliculas) == 0:
                    print("\nNo hay peliculas\n")
                else:
                    while True:
                        try:
                            p_min = int(input("Ingrese precio mínimo: "))
                            p_max = int(input("Ingrese precio máximo: "))

                            if p_min <= 0 or p_max <= 0 or p_min > p_max:
                                print("Valores no validos, ingrese nuevamente")
                            else:
                                break
                        except ValueError:
                            print("Debe ingresar valores enteros")

            case 3:
                if len(peliculas) == 0:
                    print("\nNo hay peliculas\n")
                else:
                    pregunta = True
                    while pregunta:
                        codigo = input("Ingrese código de película: ").strip()
                        precio = input("Ingrese nuevo precio: ")
                        if actualizar_precio(peliculas, cartelera, codigo, precio):
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                        pregunta = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower() == "s"
            case 4:
                codigo = input("Ingrese código de película: ").strip().upper()
                if not validar_codigo(peliculas, cartelera, codigo):
                    print("¡Codigo no valido!")
                    continue
                titulo = input("Ingrese título: ").strip()
                if not validar_titulo(titulo):
                    print("¡Titulo no valido!")
                    continue                
                genero = input("Ingrese género: ").strip()
                if not validar_genero(genero):
                    print("¡Género no valido!")
                    continue 

                duracion = input("Ingrese duración (minutos): ")
                if not validar_duracion(duracion):
                    print("¡Duración no valida!")
                    continue                     

                clasificacion = input("Ingrese clasificación: ").strip() 
                if not validar_clasificacion(clasificacion):
                    print("¡Clasificación no valida!")
                    continue

                idioma = input("Ingrese idioma: ").strip()
                if not validar_idioma(idioma):
                    print("¡Idioma no valido!")
                    continue

                es_3d = input("¿Es 3D? (s/n): ")
                if not validar_3d(es_3d):
                    print("¡Respuesta no valida!")
                    continue

                precio = input("Ingrese precio: ") 
                if not validar_precio(precio):
                    print("¡Precio no valido!")
                    continue

                cupos = input("Ingrese cupos: ")
                if not validar_cupos(cupos):
                    print("¡Cupos no validos!")
                    continue 

                if agregar_pelicula(peliculas, cartelera, codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
                    print("Película agregada")
                else:
                    print("El código ya existe")
                
            case 5:
                if len(peliculas) == 0:
                    print("\nNo hay peliculas\n")
                else:
                    codigo = input("Ingrese codigo de pelicula a eliminar: ").strip()
                    if eliminar_pelicula(peliculas, cartelera, codigo):
                        print("Película eliminada")
                    else:
                        print("El código no existe")
            case 6:
                print("Programa finalizado.")       

main()