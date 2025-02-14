'''
Aggregate relationships represent the relationship between the whole and a part of the class, member objects are part
 of the general object, but the member object can exist independently of the general object.

 --------------------------------------------->  key question  <-------------------------------------------------------
key question 🤔: What is the difference between aggregation relationship and composition relationship?

-If the parts can continue to exist independently, even if the main object disappears, then it is aggregation.

-If the parts are completely dependent on the main object and cease to exist when the main object disappears, then it is composition.

-----------------------------------------------------------------------------------------------------------------------

'''


class Doctor:
    """
    Represents a doctor with a name.
    """

    def __init__(self, name):
        self.name = name


class Hospital:
    """
    Represents a hospital that contains a list of doctors (Aggregation).

    The hospital can have multiple doctors, but doctors can exist independently
    of the hospital.
    """

    def __init__(self, name):
        self.name = name
        self.doctors = []  # List of doctors (doctors can exist without the hospital)

    def add_doctor(self, doctor):
        """
        Adds a doctor to the hospital's list.
        """
        self.doctors.append(doctor)


# Usage
hospital = Hospital("General Hospital")
doctor1 = Doctor("Dr. Carlos")
doctor2 = Doctor("Dr. Ana")

hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

# Displaying the doctors associated with the hospital
print(f"The hospital {hospital.name} has the following doctors:")
for doctor in hospital.doctors:
    print(f"- {doctor.name}")

# Demonstrating aggregation: doctors still exist even if the hospital is deleted
print(hospital.doctors)  # Shows the list of doctors
del hospital  # Deleting the hospital

# Doctors still exist and can be accessed
print(doctor1.name)
print(doctor2.name)

