'''
In most cases, dependencies are reflected in the methods of a class that use the object of another class as a parameter.
A dependency relationship is a “use” relationship. A change in a particular thing can affect other things that use it.

--------------------------------------------->  key question  <-------------------------------------------------------
key question 🤔: What is the difference between dependency relationship and association relationship?

-Uses association when a class has another class as an attribute.


-Use dependency when a class only uses another class temporarily to perform a task (For example a method).

-----------------------------------------------------------------------------------------------------------------------

'''


class Car:
    """
    Represents a car with a brand and model.
    """
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        """
        Returns the car's brand and model.
        """
        return f"{self.brand} {self.model}"


class Mechanic:
    """
    Represents a mechanic who repairs cars (Dependency).
    """
    def __init__(self, name):
        self.name = name

    def repair(self, car):
        """
        The mechanic temporarily interacts with a car to repair it.
        """
        print(f"Mechanic {self.name} is repairing the {car.get_info()}.")


# Example usage
my_car = Car("Toyota", "Corolla")
mechanic = Mechanic("Bob")
mechanic.repair(my_car)  # The mechanic depends on the car temporarily
