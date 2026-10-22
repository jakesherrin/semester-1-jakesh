"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

colour_period = 0

for steps in range (0, (maxtime + 1)) :
    print(f"Time {systime:03} State {state}")

    colour_period = colour_period + 1

    if colour_period >= states.get(state) :
        key_list = list(states.keys())

        if key_list.index(state) + 1 < key_list.length() :
            state = key_list[key_list.index(state) + 1]
        else :
            state = key_list[0]
        colour_period = 0


    systime = systime + 1

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14