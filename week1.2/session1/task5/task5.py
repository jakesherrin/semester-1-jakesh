# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Newcastle"] = "Tyne"
rivers["Hull"] = "Humber"

# Display all the keys
print(rivers.keys())

# Display all the values
print(rivers.values())

# Display all the key:value pairs, as tuples
london, leeds, liverpool, newcastle, hull = rivers.items()

print(london)

# Delete an entry from the rivers database
rivers.pop("Leeds")
