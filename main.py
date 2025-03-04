import os
from Exercici1 import E1
from Exercici2 import E2
from Exercici3 import E3

# Ruta del dataset complet
#folder_path = r'D:\cole\Gis\Gis_practiques\Dataset' #Ventura
folder_path = r"C:\Mis_cosas\06_UNI\CUARTO\PRACTICAS GIS\Gis_practiques\Dataset" #David

# Preguntar al usuario qué ejercicio ejecutar
print("📌 Selecciona qué ejercicio quieres ejecutar:")
print("1 - Solo Ejercicio 1 (análisis de contraseñas)")
print("2 - Solo Ejercicio 2 (gráficos)")
print("3 - Solo Ejercicio 3 (reutilización de contraseñas)")
print("4 - Todos los ejercicios")
opcion = input("Ingrese el número de la opción: ")

# Inicializar las clases según la opción elegida
e1 = E1() if opcion in ["1", "4"] else None
e2 = E2() if opcion in ["2", "4"] else None
e3 = E3() if opcion in ["3", "4"] else None

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
            if e3:
                e3.extract_data(data)

# Mostrar resultados de E1
if e1:
    e1.print_results()

# Mostrar gráficas de E2
if e2:
    e2.show_all_graphs()

# Mostrar resultados de E3 
if e3:
    e3.analyze_patterns()
    e3.print_results()
    e3.plot_patterns()