from paises_mongo import(
    importar_paises,
    mostrar_americas,
    mostrar_americas_mas_100m,
    mostrar_distinto_africa,
    actualizar_egipto,
    eliminar_pais_codigo_258,
    mostrar_poblacion_rango,
    mostrar_ordenado_nombre,
    buscar_paises_por_letra,
    crear_indice_codigo
)

salir = True


def mostrar_menu():
    print("\n------- MENU --------")
    print("\n1. IMPORTAR PAISES")
    print("\n2. MOSTRAR PAISES REGION AMERICAS")
    print("\n3. MOSTRAR PAISES REGION AMERICAS CON POBLACION DE MAS DE 100M")
    print("\n4. MOSTRAR PAISES REGION DISTINTA DE AFRICA")
    print("\n5. ACTUALIZAR EGIPTO")
    print("\n6. ELIMINAR PAIS CON EL CODIGO 258")
    print("\n7. MOSTRAR PAISES CUYA POBLACION SEA MAYOR A 50M Y MENOS A 150M")
    print("\n8. MOSTRAR PAISES ORDENADOS POR NOMBRE DE MANERA ASCENDENTE")
    print("\n9. BUSCAR PAISES POR LETRA")
    print("\n10. CREAR INDICE PARA EL CODIGO PAIS")
    print("\n11. SALIR (INGRESE CUALQUIER NUMERO PARA SALIR)")


while salir:
    mostrar_menu()

    print("\n<< Ingrese la opcion del MENU >>")
    res = int(input("\n>> "))

    match res:
        case 1:
            importar_paises()
        case 2:
            mostrar_americas()
        case 3:
            mostrar_americas_mas_100m()
        case 4:
            mostrar_distinto_africa()
        case 5:
            actualizar_egipto()
        case 6:
            eliminar_pais_codigo_258()
        case 7:
            mostrar_poblacion_rango()
        case 8:
            mostrar_ordenado_nombre()
        case 9:
            letra = input("\nIngrese una letra para buscar el pais: ")
            buscar_paises_por_letra(letra)
        case 10:
            crear_indice_codigo()
        case _:
            salir = False