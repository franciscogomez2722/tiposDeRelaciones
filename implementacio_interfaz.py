from abc import ABC, abstractmethod

class Trabajador(ABC):  # Interfaz simulada
    @abstractmethod
    def trabajar(self):
        pass

class Medico(Trabajador):
    def trabajar(self):
        print("El médico atiende a los pacientes.")

class Enfermera(Trabajador):
    def trabajar(self):
        print("La enfermera cuida a los pacientes.")

# Uso
medico = Medico()
enfermera = Enfermera()

medico.trabajar()
enfermera.trabajar()
