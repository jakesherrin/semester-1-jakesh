# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth) :

        if not isinstance(birth, date) or not isinstance(name, str):
            raise TypeError()

        if name == "" :
            raise ValueError()
          
        self.name = name
        self.birth = birth
    
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials (self) :
        """ Returns the intials of the name atrribute string """
        name_split = self.name.split(" ")
        return ("".join([word[0] for word in name_split])).upper()

    def is_birthday (self) :
        """ Checks whether the month and day of today matches the month and day of the dob attribute """
        today_date = str(date.today()).split("-")
        birthday = str(self.birth).split("-")

        if today_date[1] + today_date[2] == birthday[1] + birthday[2] :
           return True
        else :
            return False
