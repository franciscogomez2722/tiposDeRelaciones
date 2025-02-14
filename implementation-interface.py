'''
The implementation type relation (Interface) is mainly used to specify the relation between interfaces and
implementation classes. and implementation classes. An interface (including an abstract class) is a
collection of methods.

--------------------------------------------->  key question  <-------------------------------------------------------
key question 🤔: What is the difference between inheritance relationship and application/interface relationship?

- Use inheritance if a class is really a specialization of another. ⭐

- Use interfaces if several classes must share methods, but do not have a hierarchical relationship. 😎

-----------------------------------------------------------------------------------------------------------------------

'''


from abc import ABC, abstractmethod

class Worker(ABC):  # Simulated interface
    """
    Represents a generic worker interface using the ABC (Abstract Base Class).
    Defines a contract for the 'work' method that must be implemented by subclasses.
    """

    @abstractmethod
    def work(self):
        """
        Abstract method that must be implemented by any subclass.
        Represents the action of working.
        """
        pass


class Doctor(Worker):
    """
    Represents a doctor who inherits from Worker and implements the work method.
    """

    def work(self):
        """
        Implements the work method for a doctor.
        Prints a message describing the doctor's work.
        """
        print("The doctor attends to patients.")


class Nurse(Worker):
    """
    Represents a nurse who inherits from Worker and implements the work method.
    """

    def work(self):
        """
        Implements the work method for a nurse.
        Prints a message describing the nurse's work.
        """
        print("The nurse takes care of patients.")


# Example usage
doctor = Doctor()
nurse = Nurse()

doctor.work()
nurse.work()
