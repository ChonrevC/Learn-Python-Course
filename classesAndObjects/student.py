# THIS IS A SUPPORTING FILE FOR "classesAndObjects.py"
# This file holds the class for student

class Student:

    #Initialize the function
    # This maps out the attributes a student should have
    # SELF should be included to initialize, followed, by attributes
    #   self allows for the class parameters to be made into attributes for an object
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.in_on_probation = is_on_probation
        