class Medico:
    def __init__(self, nombre):
        self.nombre = nombre

    def atender(self, paciente):
        print(f"El Dr. {self.nombre} atiende a {paciente.nombre}.")

class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre

# Uso
medico1 = Medico("Carlos")
paciente1 = Paciente("Ana")

medico1.atender(paciente1)
