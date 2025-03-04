import os
import chardet
from Exercici1 import E1
from Exercici2 import E2

# Ruta del dataset complet
#folder_path = r'D:\cole\Gis\Gis_practiques\Dataset' #Ventura
folder_path = r"C:\Mis_cosas\06_UNI\CUARTO\PRACTICAS GIS\Gis_practiques\Dataset" #David

# Preguntar al usuario qué ejercicio ejecutar
print("📌 Selecciona qué ejercicio quieres ejecutar:")
print("1 - Solo Ejercicio 1 (análisis de contraseñas)")
print("2 - Solo Ejercicio 2 (gráficos)")
print("3 - Ambos ejercicios")
opcion = input("Ingrese el número de la opción: ")

# Inicializar las clases según la opción elegida
e1 = E1() if opcion in ["1", "3"] else None
e2 = E2() if opcion in ["2", "3"] else None

for root, dirs, files in os.walk(folder_path):
    for file in files:
        path = os.path.join(root, file)
        data = None
        
        try:
            with open(path, 'r', encoding='utf-8') as dataset:
                data = dataset.read()
            # Si falla, intentamos con otros encodings comunes
        except (UnicodeDecodeError, TypeError):
            print(f"Problema amb {file}, intentant ISO-8859-1...")
            try:
                with open(path, 'r', encoding='ISO-8859-1') as dataset:
                    data = dataset.read()
            except UnicodeDecodeError:
                print(f"Problema amb {file} a l'intentar llegir amb ISO-8859-1")

        if data:
            if e1:
                e1.extract_data(data)
            if e2:
                e2.extract_data(data)

# Mostrar resultados de E1
if e1:
    e1.print_results()

# Mostrar gráficas de E2
if e2:
    e2.show_all_graphs()