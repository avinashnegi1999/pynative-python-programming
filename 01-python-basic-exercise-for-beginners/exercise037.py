# ========question========
# Exercise 37. Simple Countdown Timer
#
# Use a while loop for a countdown from a starting value. Follow the example by printing positive values, then Blast off! at zero.
#
# Given Input: start_count = 5
#
# Expected Output: 5 4 3 2 1 Blast off!


# ========hints========
# Update the counter so the loop terminates; time.sleep can add a delay.


# Write your code below.

import time

count = 5

while count > 0:
    print(count)
    # Pause the program for 1 second
    time.sleep(1)
    # Decrement the counter
    count -= 1

print("Blast off!")
