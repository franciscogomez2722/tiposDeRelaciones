class HistorialMedico:
    def __init__(self, enfermedades):
        self.enfermedades = enfermedades

class Paciente:
    def __init__(self, nombre, enfermedades):
        self.nombre = nombre
        self.historial = HistorialMedico(enfermedades)  # Creación dentro de Paciente

# Uso
paciente = Paciente("Ana", ["Diabetes", "Hipertensión"])

print(f"Paciente: {paciente.nombre}")
print("Historial Médico:", paciente.historial.enfermedades)


