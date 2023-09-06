# Chinese Chef is a specific type of chef, so it can do the things a general chef can do, plus more!

# importing the Chef class & putting it as a class parameter lets the Chinese Chef do general Chef thingies!
from chef import Chef
class ChineseChef(Chef):

    #To override a function from the base class, just simply define the function again
    def make_special(self):
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")

