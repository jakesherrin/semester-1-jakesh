# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

# Initialise the sequence list and adds the first term (0)
sequence = [0]

# This is the loop which adds a new term each time it iterates, up until value L is reached
for k in range (1, L) :

    # Calculates and adds the new term 
    new_term = sequence[k - 1] - k
    if new_term <= 0 or (new_term in sequence) == True :
        new_term = new_term + (2 * k)

    sequence.append(new_term)

# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence