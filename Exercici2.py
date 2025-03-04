#Mostreu una gràfica amb:

#1. les 30 contrasenyes més comunes i el número de vegades que apareixen a D.

#2. les longituds de les contrasenyes (és a dir, quantes contrasenyes de cada longitud hi ha a D). Quina és la
#contrasenya més curta? I la més llarga? Quina és la longitud mitjana i mediana?

#3. el número d’aparicions de cada dígit en el conjunt de totes les contrasenyes de D. Creieu que hi ha algun
#dígit més comú que els altres?

#4. els 30 anys (del segle XX o XXI) que apareixen més sovint en les contrasenyes i el número d’aparicions
#que tenen. Hi ha algun any que destaqui sobre els altres?

#Per cada gràfica, comenteu els resultats obtinguts i expliqueu quins patrons heu detectat en les contrasenyes
#analitzades

import re
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from collections import Counter

import numpy as np

class E2: 

    def __init__(self):
        self.passwords = []
        self.passwords_count = Counter()
    
    def extract_data(self, data):
        """Extrau les contrasenyes del dataset i les guarda en un comptador"""
        linies = data.strip().split("\n")
        for linia in linies:
            password = None

            if ":" in linia:
                _, password = linia.split(":", 1)
            elif ";" in linia:
                _, password = linia.split(";", 1)
            else:
                continue
            
            password = password.strip()
            if password:
                self.passwords.append(password)
                self.passwords_count[password] += 1  # Comptar les contrasenyes repetides

    def plot_top_passwords(self):
        """Gràfica de les 30 contrasenyes més comunes"""
        mes_comuns = self.passwords_count.most_common(30)

        if not mes_comuns:
            print("No s'han trobat contrasenyes")
            return
        
        passwords, counts = zip(*mes_comuns)
        plt.figure(figsize=(12, 6))
        plt.barh(passwords[::-1], counts[::-1]) #invertim l'ordre perquè les contrasenyes més comunes quedin a dalt
        plt.xlabel("Nombre de vegades")
        plt.ylabel("Contrasenya")
        plt.title("Les 30 contrasenyes més comunes")
        plt.show()
    
    def plot_length_distribution(self):
        """Gràfica de distribución de longitud de las contrasenyes"""
         # Calcular la longitud de cada contraseña
        lengths = [len(pwd) for pwd in self.passwords]

        if not lengths:
            print("⚠️ No hay contraseñas en el dataset.")
            return

        # Filtrar contraseñas extremadamente largas (mayores a 50 caracteres)
        max_length_allowed = 50
        filtered_lengths = [l for l in lengths if l <= max_length_allowed]

        # Contar cuántas contraseñas tienen cada longitud
        frequency = Counter(filtered_lengths)

        # Ordenar los datos por longitud
        sorted_lengths = sorted(frequency.items())
        x_vals = [item[0] for item in sorted_lengths]
        y_vals = [item[1] for item in sorted_lengths]

        # Crear la gráfica de barras
        plt.figure(figsize=(12, 6))
        plt.bar(x_vals, y_vals, color="skyblue")
        plt.xlabel("Longitud de la contraseña")
        plt.ylabel("Número de contraseñas")
        plt.title("Distribución de longitudes de las contraseñas (máx. 50 caracteres)")

        # Mostrar los números completos en el eje Y
        plt.ticklabel_format(style='plain', axis='y')  # Evita la notación científica
        plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))  # Formato con separadores de miles

        plt.xticks(x_vals, rotation=45)  # Rotar etiquetas para mayor claridad
        plt.tight_layout()
        plt.show()

        # Calcular estadísticas de longitudes
        min_length = min(filtered_lengths)
        max_length = max(filtered_lengths)
        avg_length = np.mean(filtered_lengths)
        median_length = np.median(filtered_lengths)

        # Encontrar la primera contraseña con la longitud mínima y máxima
        shortest_pwd = next(pwd for pwd in self.passwords if len(pwd) == min_length)
        longest_pwd = next(pwd for pwd in self.passwords if len(pwd) == max_length)

        # Mostrar resultados estadísticos
        print(f"La contraseña más corta: '{shortest_pwd}' con longitud {min_length}")
        print(f"La contraseña más larga (considerando el límite de 50 caracteres): '{longest_pwd}' con longitud {max_length}")
        print(f"Longitud media: {avg_length:.2f}")
        print(f"Longitud mediana: {median_length}")

    def plot_digit_frequency(self):
        """Gràfica de la freqüència d'aparició de cada dígit en les contrasenyes"""
        # Contar la frecuencia de los dígitos en todas las contraseñas
        digits = Counter(c for pwd in self.passwords for c in pwd if c.isdigit())

        if not digits:
            print("⚠️ No hay dígitos en las contraseñas.")
            return

        # Crear la gráfica de barras
        plt.figure(figsize=(8, 5))
        plt.bar(digits.keys(), digits.values(), color="red")
        plt.xlabel("Dígito")
        plt.ylabel("Frecuencia")
        plt.title("Frecuencia de aparición de cada dígito en contraseñas")

        plt.ticklabel_format(style='plain', axis='y')  # Evita la notación científica
        plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))  # Formato con separadores de miles

        plt.xticks(sorted(digits.keys()))  # Asegurar orden de los dígitos
        plt.tight_layout()
        plt.show()

    def plot_top_years(self):
        """Gràfica dels 30 anys més comuns en les contrasenyes"""
        years = []
        for pwd in self.passwords:
            match = re.findall(r"(19\d{2}|20\d{2})", pwd)  # Buscar años
            years.extend(match)

        counter = Counter(years)
        most_common_years = counter.most_common(30)

        if most_common_years:
            years, counts = zip(*most_common_years)

            plt.figure(figsize=(12, 5))
            plt.bar(years, counts)
            plt.xlabel("Año")
            plt.ylabel("Frecuencia")
            plt.title("Top 30 Años más comunes en las contraseñas")
            plt.xticks(rotation=45)
            plt.show()
        else:
            print("⚠️ No se encontraron años en las contraseñas.")

    def show_all_graphs(self):
        """Mostra tots els gràfics de l'exercici 2"""
        self.plot_top_passwords()
        self.plot_length_distribution()
        self.plot_digit_frequency()
        self.plot_top_years()