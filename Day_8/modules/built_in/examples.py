import math
import datetime
import random
import os

print(dir(math))
# Using the math module
print("The value of pi is:", math.pi)
print("The square root of 16 is:", math.sqrt(16))

# Using the datetime module
now = datetime.datetime.now()
print("Current date and time:", now)

# Using the random module
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

# Using the os module
current_directory = os.getcwd()
print("Current working directory:", current_directory)