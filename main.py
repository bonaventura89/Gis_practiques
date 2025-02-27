import os
from Exercici1 import E1

folder_path = r'D:\cole\Gis\Gis_practiques\Dataset'

E1 = E1()

for root, dirs, files in os.walk(folder_path):
    for file in files:
        path = os.path.join(root, file)
        try:
            with open(path, 'r', encoding='utf-8') as dataset:
                data = dataset.read()
                # Exercici 1
                E1.extrect_data(data)
                # Exercici 2
                # Exercici 3
        except Exception as e:
            print(f"Error al leer {path}: {e}")
