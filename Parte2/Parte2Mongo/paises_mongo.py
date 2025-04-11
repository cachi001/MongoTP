import requests
from pymongo import MongoClient
import urllib3

# Conexión a Mongo
client = MongoClient("mongodb://localhost:27017/")
db = client.paises_db
coleccion = db.paises

# Desactivar advertencias SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Bucle para recorrer códigos del 1 al 300 e importar países
def importar_paises():
    for code in range(1, 302):
        url = f"https://restcountries.com/v3.1/alpha/{code:03}"
        try:
            response = requests.get(url, verify=False, timeout=10)
            if response.status_code == 200:
                try:
                    datos = response.json()[0]
                    pais = {
                        "codigoPais": datos.get("ccn3"),
                        "nombrePais": datos.get("name", {}).get("common"),
                        "capitalPais": datos.get("capital", [None])[0],
                        "region": datos.get("region"),
                        "subregion": datos.get("subregion"),
                        "poblacion": datos.get("population"),
                        "latitud": datos.get("latlng", [None, None])[0],
                        "longitud": datos.get("latlng", [None, None])[1],
                        "superficie": datos.get("area")
                    }

                    if coleccion.find_one({"codigoPais": pais["codigoPais"]}):
                        coleccion.update_one({"codigoPais": pais["codigoPais"]}, {"$set": pais})
                    else:
                        coleccion.insert_one(pais)
                except Exception as e:
                    print(f"Error procesando código {code}: {e}")
            else:
                print(f"Código {code} no encontrado (HTTP {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión con código {code}: {e}")

# Función de impresión formateada
def mostrar_pais_formateado(pais):
    print(f"Nombre: {pais.get('nombrePais', 'Desconocido')}")
    print(f"Capital: {pais.get('capitalPais', 'No especificada')}")
    print(f"Región: {pais.get('region', '-')}")
    print(f"Subregión: {pais.get('subregion', '-')}")
    print(f"Población: {pais.get('poblacion', 0):,}")
    print(f"Superficie: {pais.get('superficie', 0):,} km²")
    print(f"Coordenadas: latitud {pais.get('latitud')}°, longitud {pais.get('longitud')}°")
    print("-" * 40)

# 5.1 Seleccionar países donde región sea Americas
def mostrar_americas():
    print("Países en América:\n")
    for pais in coleccion.find({"region": "Americas"}):
        mostrar_pais_formateado(pais)

# 5.2 Región Americas y población > 100 millones
def mostrar_americas_mas_100m():
    print("Países en América con población mayor a 100 millones:\n")
    for pais in coleccion.find({"region": "Americas", "poblacion": {"$gt": 100_000_000}}):
        mostrar_pais_formateado(pais)

# 5.3 Región distinta de Africa (usa $ne)
def mostrar_distinto_africa():
    print("Países fuera de África:\n")
    for pais in coleccion.find({"region": {"$ne": "Africa"}}):
        mostrar_pais_formateado(pais)

# 5.4 Actualizar Egypt → Egipto y cambiar población
def actualizar_egipto():
    coleccion.update_one(
        {"nombrePais": "Egypt"},
        {"$set": {"nombrePais": "Egipto", "poblacion": 95_000_000}}
    )

# 5.5 Eliminar país con código 258
def eliminar_pais_codigo_258():
    coleccion.delete_one({"codigoPais": "258"})

# 5.6 ¿Qué hace drop()?
"""
coleccion.drop() elimina toda la colección 'paises' con sus documentos.
db.drop_database('paises_db') elimina toda la base de datos.
Ambas operaciones son irreversibles.
"""

# 5.7 Población entre 50 y 150 millones
def mostrar_poblacion_rango():
    print("Países con población entre 50 y 150 millones:\n")
    for pais in coleccion.find({"poblacion": {"$gt": 50_000_000, "$lt": 150_000_000}}):
        mostrar_pais_formateado(pais)

# 5.8 Ordenar países por nombre ascendente
def mostrar_ordenado_nombre():
    print("Países ordenados por nombre (ascendente):\n")
    for pais in coleccion.find().sort("nombrePais", 1):
        mostrar_pais_formateado(pais)

# 5.9 ¿Qué hace skip()?
"""
El método skip(n) omite los primeros 'n' resultados.
Ejemplo: coleccion.find().skip(10) salta los 10 primeros documentos.
Sirve para paginación o evitar repetir resultados.
"""

# 5.10 Buscar países por letra inicial con regex
def buscar_paises_por_letra(letra):
    print(f"Países que empiezan con la letra '{letra.upper()}':\n")
    for pais in coleccion.find({"nombrePais": {"$regex": f"^{letra}", "$options": "i"}}):
        mostrar_pais_formateado(pais)

"""
Ejemplo: LIKE 'A%' en SQL → regex: {"nombrePais": {"$regex": "^A"}}
"""

# 5.11 Crear índice en campo código del país
def crear_indice_codigo():
    coleccion.create_index("codigoPais")

# 5.12 Backup de la base de datos
"""
Para hacer backup:
mongodump --db paises_db --out ./backup/

Para restaurar:
mongorestore --db paises_db ./backup/paises_db/
"""
""" 
    Para hacer backup de paises_db se puede usar el comando:
    mongodump --db paises_db --out ./backup/ 
    Esto genera una carpeta con la base de datos para restaurarla luego con:
    mongorestore --db paises_db ./backup/paises_db/ 
"""