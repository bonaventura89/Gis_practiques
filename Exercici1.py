###
# Calculeu quantes i quin percentatge de les contrasenyes de D:
# 1. són numèriques (és a dir, contenen només caràcters numèrics).
# 2. són alfabètiques (és a dir, contenen només caràcters alfabètics).
# 3. són alfanumèriques (és a dir, contenen només caràcters alfabètics i/o numèrics, però no símbols).
# 4. contenen un número que podria ser un any del segle XX o XXI.
# 5. són alfabètiques i tenen totes les lletres en minúscules.
# 6. són alfabètiques i tenen totes les lletres en majúscules.
# 7. són alfabètiques, comencen amb una lletra majúscula i tenen la resta de lletres minúscules.
###
import re

class E1: 
    def __init__(self):
        self.total_passwords= 0
        self.total_numeriques = 0
        self.total_alfabetiques = 0
        self.total_alfanumeriques = 0
        self.total_segles = 0
        self.total_lletresMinuscules = 0
        self.total_lletresMajuscules = 0
        self.total_lletresMajusMinus = 0

    def extract_data(self, data):
        """Processa el dataset i analitza cada contrasenya"""
        linies = data.strip().split("\n") #separem les línies
        for linia in linies:
            password = None

            if ":" in linia:
                _, password = linia.split(":", 1) #separem l'usuari de la contrasenya
            elif ";" in linia:
                _, password = linia.split(";", 1) #separem l'usuari de la contrasenya
            
            if password:
                password = password.strip().replace(" ", "") #eliminem espais en blanc

                if password:
                    self.total_passwords += 1
                    self.analitza_password(password) #analitza cada contrasenya

    def analitza_password(self, password):
        """Analitza una contrasenya i actualitza els comptadors"""
        if password.isdigit():
            self.total_numeriques += 1
        elif password.isalpha():
            self.total_alfabetiques += 1
            if password.islower():
                self.total_lletresMinuscules += 1
            elif password.isupper():
                self.total_lletresMajuscules += 1
            elif password[0].isupper() and password[1:].islower():
                self.total_lletresMajusMinus += 1
        
        if password.isalnum():
            self.total_alfanumeriques += 1

        if self.conté_segles(password):
            self.total_segles += 1

    def conté_segles(self, password):
        """Comprova si una contrasenya conté un número que podria ser un any del segle XX o XXI"""
        match = re.search(r"(19\d{2}|20\d{2})", password) #busca el patró 19XX o 20XX
        return match is not None #retorna True si troba un any

    def print_results(self):
        """Imprimeix els resultats"""
        print(f"")
        print(f"\nTotal passwords: {self.total_passwords}")
        print(f"Contrasenyes numèriques: {self.total_numeriques} ({self.percentage(self.total_numeriques)}%)")
        print(f"Contrasenyes alfabètiques: {self.total_alfabetiques} ({self.percentage(self.total_alfabetiques)}%)")
        print(f"Contrasenyes alfanumèriques: {self.total_alfanumeriques} ({self.percentage(self.total_alfanumeriques)}%)")
        print(f"Contrasenyes amb un any del segle XX o XXI: {self.total_segles} ({self.percentage(self.total_segles)}%)")
        print(f"Contrasenyes només minúscules: {self.total_lletresMinuscules} ({self.percentage(self.total_lletresMinuscules)}%)")
        print(f"Contrasenyes només majúscules: {self.total_lletresMajuscules} ({self.percentage(self.total_lletresMajuscules)}%)")
        print(f"Contrasenyes amb primera lletra majúscula i la resta minúscula: {self.total_lletresMajusMinus} ({self.percentage(self.total_lletresMajusMinus)}%)\n")

    def percentage(self, value):
        """Calcula el percentatge respecte al total de contrasenyes"""
        return round((value / self.total_passwords) * 100, 2)
