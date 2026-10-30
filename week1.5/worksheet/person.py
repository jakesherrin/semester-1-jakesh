# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, date_of_birth) :
        self.name = name
        self.date_of_birth = date_of_birth.split("/")
    
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials (self) :
        name_split = self.name.split(" ")
        return ("".join([word[0] for word in name_split])).upper()

    def is_birthday (self) :
        today_date = str(date.today()).split("-")

        if today_date[1] + today_date[2] == self.date_of_birth[1] + self.date_of_birth[2] :
           return True
        else :
            return False
