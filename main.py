import os
import chardet
from Exercici1 import E1

# Ruta del dataset completo
folder_path = r"C:\Mis_cosas\06_UNI\CUARTO\PRACTICAS GIS\Gis_practiques\Dataset"

e1 = E1()

for root, dirs, files in os.walk(folder_path):
    for file in files:
        path = os.path.join(root, file)
        
        try:
            try:
                with open(path, 'r', encoding='utf-8') as dataset:
                    data = dataset.read()
                    e1.extract_data(data)

            # Si falla, intentamos con otros encodings comunes
            except (UnicodeDecodeError, TypeError):
                print(f"Problema con {file}, intentando ISO-8859-1...")
                try:
                    with open(path, 'r', encoding='ISO-8859-1') as dataset:
                        data = dataset.read()
                        e1.extract_data(data)
                except UnicodeDecodeError:
                    print(f"Problema con {file} al intentar leer con ISO-8859-1")
                    
        except Exception as e:
            print(f"Error al leer {path}: {e}")

# Mostrar resultados
e1.print_results()
