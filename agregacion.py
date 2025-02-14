'''
Es una relación débil  todo-parte, donde el todo contiene partes que pueden existir independientemente.

Ejemplo: Un Hospital tiene varios Médicos, pero los médicos pueden existir sin el hospital.
'''

class Medico:
    def __init__(self, nombre):
        self.nombre = nombre

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.medicos = []  # Lista de médicos (pueden existir sin el hospital)

    def agregar_medico(self, medico):
        self.medicos.append(medico)

# Uso
hospital = Hospital("General")
medico1 = Medico("Dr. Carlos")
medico2 = Medico("Dr. Ana")

hospital.agregar_medico(medico1)
hospital.agregar_medico(medico2)

print(f"El hospital {hospital.nombre} tiene los médicos:")
for m in hospital.medicos:
    print(f"- {m.nombre}")

print(hospital.medicos)
del hospital
print(medico1.nombre)
print(medico2.nombre)
