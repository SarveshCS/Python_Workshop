# List of basic colors
colors = 'Red','Green','Blue','Yellow','Orange','Purple','White','Black'

# Take input from the user
char = input("Enter a character: ").upper()

# Display the color name that starts with the input character
for color in colors:
    if color.startswith(char):
        print(f"The color is {color}")
        break
else:
    print("No basic color starts with that letter.")