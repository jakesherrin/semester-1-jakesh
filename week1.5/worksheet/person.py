# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, date_of_birth) :
        self.name = name
        self.date_of_birth = date_of_birth
    
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials (self) :
        name_split = self.name.split(" ")
        return ("".join([word[0] for word in name_split])).upper()

    def is_birthday ()

guy = Person("James Brodrick Cuthbert William James", 10)

print(guy.initials())