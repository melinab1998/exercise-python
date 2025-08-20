lista_personas = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Fito', 'Garcia', 23),
    ('33333333', 'Leo', 'Peralta', 26),
    ('44444444', 'Bruno', 'Mac', 25),
    ('55555555', 'Nico', 'Zaoral', 27),
    ('44444444', 'Bruno', 'Mac', 25),
]

def ordenar(lista_personas):
    edades = [persona[3] for persona in lista_personas]
    return sorted(edades)

def convertir_a_diccionario(lista_personas):
    return {persona[0]: (persona[1], persona[2], persona[3]) for persona in lista_personas}

def devolver_edad(lista_personas, dni):
    diccionario_personas = convertir_a_diccionario(lista_personas)
    datos = diccionario_personas.get(dni)
    return datos[2] if datos else "DNI no encontrado"

def eliminar_repetidos(lista_personas):
    personas_unicas = []
    for persona in lista_personas:
        if persona not in personas_unicas:
            personas_unicas.append(persona)
    return personas_unicas

def separar_por_edad(lista_personas):
    mayores = []
    menores = []
    for persona in lista_personas:
        if persona[3] >= 25:
            mayores.append(persona)
        else:
            menores.append(persona)
    return mayores, menores

def obtener_promedio(lista):
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        return 0

def main():
    print('Resultados:\n')
    print(' * Edades ordenadas: %s\n' % ordenar(lista_personas))
    print(' * Elementos como diccionario: %s\n' % convertir_a_diccionario(lista_personas))
    print(' * La edad para dni 55555555 es: %s\n' % devolver_edad(lista_personas, '55555555'))
    print(' * Elementos únicos: %s\n' % eliminar_repetidos(lista_personas))
    print(' * Los mayores de 25 son: %s\n' % separar_por_edad(lista_personas)[0])
    print(' * Los menores de 25 son: %s\n' % separar_por_edad(lista_personas)[1])
    print(' * El promedio de las edades es: %s\n' % obtener_promedio(ordenar(lista_personas)))
    print(' * El promedio de una lista vacía es: %s\n' % obtener_promedio([]))

if __name__ == "__main__":
    main()