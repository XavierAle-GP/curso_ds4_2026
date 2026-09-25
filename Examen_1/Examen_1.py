# Nombre completo: Xavier Alejandro González Pacheco
# Fecha: 24-09-2026
# Uso: python Examen_1.py -i frases_celebres.csv -o frases_corregidas.csv
# Declaración de uso de IA generativa: Sí. Modelo: MAI-Code-1.1-Flash (versión 2026-09-24)

import argparse
import csv
import re
from collections import defaultdict

class Pelicula:
    def __init__(self, nombre):
        self.nombre = nombre.strip()

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()

class FraseCelebre:
    def __init__(self, frase, pelicula):
        self.frase = frase.strip()
        self.pelicula = Pelicula(pelicula.strip())

    def __str__(self):
        return f'"{self.frase}" - {self.pelicula.nombre}'

    def __repr__(self):
        return self.__str__()

def normalizar_texto(texto):
    texto = texto.lower()
    return re.sub(r"[^a-záéíóúñü0-9]+", " ", texto).strip()

def obtener_palabras(texto):
    return [palabra for palabra in normalizar_texto(texto).split() if palabra]

def leer_csv(ruta_archivo):
    frases = []
    try:
        with open(ruta_archivo, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                frase = (fila.get("frase") or "").strip()
                pelicula = (fila.get("pelicula") or fila.get("película") or "").strip()
                if frase and pelicula:
                    frases.append(FraseCelebre(frase, pelicula))
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe. Se trabajará con una lista vacía.")
    except Exception as error:
        print(f"Error al leer el archivo CSV: {error}")
    return frases

def guardar_csv(ruta_archivo, frases):
    with open(ruta_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["frase", "pelicula"])
        escritor.writeheader()
        for frase in frases:
            escritor.writerow({
                "frase": frase.frase,
                "pelicula": frase.pelicula.nombre,
            })

def buscar_palabra(frases, palabra):
    palabra_normalizada = normalizar_texto(palabra)
    if not palabra_normalizada:
        print("Debe ingresar una palabra válida.")
        return []
    resultados = []
    for frase in frases:
        texto_frase = normalizar_texto(frase.frase)
        texto_pelicula = normalizar_texto(frase.pelicula.nombre)
        if palabra_normalizada in texto_frase.split() or palabra_normalizada in texto_pelicula.split():
            resultados.append(frase)
    return resultados

def contar_palabras_diferentes(frases):
    palabras = set()
    for frase in frases:
        palabras.update(obtener_palabras(frase.frase))
    return len(palabras)

def contar_frases_por_pelicula(frases):
    peliculas = defaultdict(list)
    for frase in frases:
        peliculas[frase.pelicula.nombre].append(frase)
    return sorted(peliculas.items(), key=lambda item: (-len(item[1]), item[0]))

def mostrar_resultados_busqueda(resultados):
    if not resultados:
        print("No se encontraron coincidencias.")
        return
    print(f"\nSe encontraron {len(resultados)} coincidencias:")
    for frase in resultados:
        print(f"- {frase}")

def mostrar_estadisticas(frases):
    cantidad_palabras = contar_palabras_diferentes(frases)
    cantidad_frases = len(frases)
    cantidad_peliculas = len({frase.pelicula.nombre for frase in frases})

    print("\n==== ESTADÍSTICAS ====")
    print(f"Número de palabras diferentes: {cantidad_palabras}")
    print(f"Número de frases: {cantidad_frases}")
    print(f"Número de películas: {cantidad_peliculas}")

def mostrar_frases_por_pelicula(frases):
    ordenado = contar_frases_por_pelicula(frases)
    if not ordenado:
        print("No hay frases registradas.")
        return
    print("\n==== FRASES POR PELÍCULA ====")
    for pelicula, lista_frases in ordenado:
        print(f"{pelicula} ({len(lista_frases)} frase(s))")
        for frase in lista_frases:
            print(f"  - {frase.frase}")

def mostrar_menu():
    print("\n===== MENÚ =====")
    print("1. Buscar palabra")
    print("2. Agregar nueva frase")
    print("3. Mostrar estadística general")
    print("4. Mostrar frases por película")
    print("0. Salir")

def agregar_frase(frases, ruta_salida):
    print("\n==== AGREGAR FRASE ====")
    frase_texto = input("Escribe la frase: ").strip()
    pelicula_texto = input("Escribe la película: ").strip()
    if not frase_texto or not pelicula_texto:
        print("La frase y la película no pueden estar vacías.")
        return

    frases.append(FraseCelebre(frase_texto, pelicula_texto))
    guardar_csv(ruta_salida, frases)
    print("La frase fue agregada y guardada correctamente.")

def main():
    parser = argparse.ArgumentParser(description="Gestor de frases célebres por película.")
    parser.add_argument("-i", "--input", required=True, help="Archivo CSV de entrada con frases y películas.")
    parser.add_argument("-o", "--output", required=True, help="Archivo CSV de salida donde se guardarán los cambios.")
    args = parser.parse_args()
    frases = leer_csv(args.input)
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            palabra = input("Escribe la palabra a buscar: ").strip()
            resultados = buscar_palabra(frases, palabra)
            mostrar_resultados_busqueda(resultados)
        elif opcion == "2":
            agregar_frase(frases, args.output)
        elif opcion == "3":
            mostrar_estadisticas(frases)
        elif opcion == "4":
            mostrar_frases_por_pelicula(frases)
        elif opcion == "0":
            guardar_csv(args.output, frases)
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
