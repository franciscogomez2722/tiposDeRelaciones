"""Se da cuando una clase usa otra temporalmente dentro de un método, sin guardarla como atributo.

  Ejemplo: Un Doctor depende de un Paciente cuando lo atiende, pero no lo almacena."""


class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre

class Doctor:
    def __init__(self, nombre):
        self.nombre = nombre

    def atender_paciente(self, paciente):
        print(f"El Dr. {self.nombre} está atendiendo a {paciente.nombre}")

# Uso
doctor = Doctor("Carlos")
paciente = Paciente("Ana")

doctor.atender_paciente(paciente)  # Relación temporal
