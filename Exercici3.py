import re
from collections import defaultdict, Counter
import matplotlib.pyplot as plt

class E3:
    def __init__(self):
        self.users_passwords = defaultdict(list)  # Diccionari usuari -> llista de conrtrasenyes
        self.reused_passwords_count = 0
        self.total_repeated_users = 0

    def extract_data(self, data):
        """📌 Agrupar las contrasnyes per usuari"""
        lines = data.strip().split("\n")
        
        for line in lines:
            if ":" in line:
                username, password = line.split(":", 1)
            elif ";" in line:
                username, password = line.split(";", 1)
            else:
                continue  # Ignorar línies sense format vàlid
            
            username, password = username.strip(), password.strip()
            self.users_passwords[username].append(password)

    def analyze_patterns(self):
        """Analitzar com els usuaris reutilitzen contrasenyes"""

        reused_users = 0  # Usuaris amb contrasenyes repetides
        total_users = 0    # Total d'usuaris amb més d'una contrasenya
        pattern_counter = Counter()

        for user, passwords in self.users_passwords.items():
            if len(passwords) > 1:  # Només analitzem usuaris repetits
                total_users += 1
                unique_passwords = set(passwords)

                if len(unique_passwords) < len(passwords):  # Si hi han repetides
                    reused_users += 1

                # Analitzar patrons de modificació
                sorted_passwords = sorted(unique_passwords)  # Ordenem per tamany
                for i in range(len(sorted_passwords) - 1):
                    if self.are_related(sorted_passwords[i], sorted_passwords[i + 1]):
                        pattern_counter["modificación mínima"] += 1
                    elif sorted_passwords[i] in sorted_passwords[i + 1] or sorted_passwords[i + 1] in sorted_passwords[i]:
                        pattern_counter["contraseña extendida"] += 1
                    elif re.sub(r"\d", "", sorted_passwords[i]) == re.sub(r"\d", "", sorted_passwords[i + 1]):
                        pattern_counter["solo cambio de número"] += 1

        # Guardem estadístiques
        self.reused_passwords_count = reused_users
        self.total_repeated_users = total_users
        self.pattern_counter = pattern_counter

    def are_related(self, pwd1, pwd2):
        """Verifica si dues contrasenyes són similars canviant 1-2 caràcters"""
        if abs(len(pwd1) - len(pwd2)) > 2:
            return False
        diff_count = sum(c1 != c2 for c1, c2 in zip(pwd1, pwd2))
        return diff_count <= 2

    def print_results(self):
        """Mostar resultats de l'anàlisi"""
        if self.total_repeated_users == 0:
            print("no hi han usuaris amb més d'una contrasenya al dataset.")
            return

        percentage = (self.reused_passwords_count / self.total_repeated_users) * 100
        print(f"Usuaris amb múltiples contrasenyes: {self.total_repeated_users}")
        print(f"Usuaris que reutilitzen contrasenyes: {self.reused_passwords_count} ({percentage:.2f}%)")

        print("\nPatrons observats de contrasenyes:")
        for pattern, count in self.pattern_counter.items():
            print(f"  - {pattern}: {count}")

        # Mostrar exemples d'usuaris que reutilitzen contrasenyes
        print("\nExemples d'usuaris que reutilitzen contrasenyes:")
        examples_shown = 0
        for user, passwords in self.users_passwords.items():
            if len(set(passwords)) < len(passwords):  # Si l'usuari repeteix contrasenya
                print(f"  {user}: {passwords}")
                examples_shown += 1
                if examples_shown >= 5:
                    break

    def plot_patterns(self):
        """Generar gràfic amb els patrons detectats"""
        if not self.pattern_counter:
            print("No hi ha dades suficients per fer el gràfic.")
            return

        patterns, counts = zip(*self.pattern_counter.items())

        plt.figure(figsize=(10, 6))
        plt.barh(patterns, counts, color="purple")
        plt.xlabel("Nombre de vegades que passa")
        plt.ylabel("Patró detectat")
        plt.title("Patrons de modificació de contrasenyes")
        plt.show()
