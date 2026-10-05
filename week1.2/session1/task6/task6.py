# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
albums = {"Title Fight" : [("Shed", 2011), ("Floral Green", 2012), ("Hyperview", 2015)],
          "Deftones" : [("Adrenaline", 1995), ("Around the Fur", 1999), ("White Pony", 2001), ("Saturday Night Wrist", 2006), ("Diamond Eyes", 2010), ("Koi No Yokan", 2012), ("Gore", 2016), ("Ohms", 2020 )],
          "Black Country, New Road" : [("For the First Time", 2019), ("Ants From Up There", 2022)]}

# Pretty-print the data structure
pprint(albums)

# Display details of one album recorded by a specific artist
