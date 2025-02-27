class E1: 

    def __init__(self):
        self.total_contraseñas= 0
        self.total_numeros = 0
        self.total_lletres = 0
        self.total_lletresNumeros = 0
        self.total_segles = 0
        self.total_lletresMenor = 0
        self.total_lletresMajor = 0
        self.total_lletresMenorMajor = 0

    def extrect_data(self, data):
        
        A = data.split("\n")
        for line in A:
            print(line)
            print(line.split(":"))

        return 
