# This file holds the class for student

class Student:

    #Initialize the function
    # This maps out the attributes a student should have
    # SELF should be included to initialize, followed, by attributes
    #   self is how attributes access one another. self must have the parameters to have the class recognize them as attributes
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.in_on_probation = is_on_probation

    
    # Classes can have their own functions that the class objects can access
    # Notice: a class function also has (self) in paranthesis
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    
        