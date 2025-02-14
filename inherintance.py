'''
The inheritance relationship is used to describe the relationship between parent and child classes.
In the inheritance relationship, the subclass inherits all the functions of the parent class and
the parent class has attributes and methods in common.

--------------------------------------------->  key question  <-------------------------------------------------------
key question 🤔: What is the difference between inheritance relationship and application/interface relationship?

- Use inheritance if a class is really a specialization of another. ⭐

- Use interfaces if several classes must share methods, but do not have a hierarchical relationship.😎

-----------------------------------------------------------------------------------------------------------------------

'''

class User:
    """
    Represents a generic user with basic attributes.
    """

    def __init__(self, name, age):
        """
        Initializes a user with a name and age.

        :param name: The name of the user.
        :param age: The age of the user.
        """
        self.name = name
        self.age = age

    def show_info(self):
        """
        Displays the user's information.
        """
        print(f"Name: {self.name}, Age: {self.age}")


class Medical(User):  # Inheritance
    """
    Represents a medical professional, inheriting from User.
    """

    def __init__(self, name, age, specialty):
        """
        Initializes a medical professional with a name, age, and specialty.

        :param name: The name of the medical professional.
        :param age: The age of the medical professional.
        :param specialty: The medical specialty.
        """
        super().__init__(name, age)
        self.specialty = specialty


class Nurse(User):  # Inheritance
    """
    Represents a nurse, inheriting from User.
    """

    def __init__(self, name, age, area):
        """
        Initializes a nurse with a name, age, and area of expertise.

        :param name: The name of the nurse.
        :param age: The age of the nurse.
        :param area: The area of nursing specialization.
        """
        super().__init__(name, age)
        self.area = area


# Example usage
medical1 = Medical("Carlos", 45, "Cardiology")
nurse1 = Nurse("Laura", 30, "Pediatrics")

medical1.show_info()
nurse1.show_info()

