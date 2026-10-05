# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
print(both) # tomato will be printed

# Why does the following code diplay five items?

food = fruit.union(vegetables)
print(food) # it will print "apple" "orange" "tomato" "leek" "potato" 
 
# Add an item to fruit
fruit.add("potato")

print(fruit) # it will print "apple" "orange" "tomato" "cherry"

# Remove an item from vegetables
vegetables.discard("leek")
print(vegetables) # it will print "leek" "tomato"

# Find and display symmetric difference of the two sets
print(fruit.symmetric_difference(vegetables))
