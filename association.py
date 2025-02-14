'''
The association type relationship indicates that a property of a class contains a reference to an instance (or instances)
of another class. Association is the most commonly used relationship between a class and another class, meaning
that there is a connection between one type of object and another type of object.

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


class User:
    """
    Represents a user who owns a car (Association).
    """
    def __init__(self, name, car):
        self.name = name
        self.car = car  # Strong relationship (Association)

    def show_car(self):
        """
        Displays the car owned by the user.
        """
        print(f"{self.name} owns a {self.car.get_info()}.")


# Example usage
my_car = Car("Toyota", "Corolla")
user = User("Alice", my_car)  # The user owns the car (Association)
user.show_car()