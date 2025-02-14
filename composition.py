'''
The combination relation represents the relation between the whole and the part of the class, and the whole and the part
have a constant lifetime. Once the overall object does not exist, some of the objects will not exist and all will die in
the same lifetime.

 --------------------------------------------->  key question  <-------------------------------------------------------
key question 🤔: What is the difference between aggregation relationship and composition relationship?

-If the parts can continue to exist independently, even if the main object disappears, then it is aggregation.

-If the parts are completely dependent on the main object and cease to exist when the main object disappears, then it is composition.

-----------------------------------------------------------------------------------------------------------------------

'''

# MedicalHistory class represents the patient's medical record.
class MedicalHistory:
    def __init__(self, diseases):
        self.diseases = diseases  # List of diseases the patient has.

# Patient class represents a patient with a name and a medical history.
class Patient:
    def __init__(self, name, diseases):
        self.name = name  # Patient's name.
        self.history = MedicalHistory(diseases)  # Composition: MedicalHistory is created within Patient.

# Usage
patient = Patient("Ana", ["Diabetes", "Hypertension"])  # Creating a patient with medical conditions.

# Display patient information.
print(f"Patient: {patient.name}")
print("Medical History:", patient.history.diseases)

# Deleting the patient object.
del patient

# These lines will cause an error because 'patient' no longer exists.
print(f"Patient: {patient.name}")
print("Medical History:", patient.history.diseases)

