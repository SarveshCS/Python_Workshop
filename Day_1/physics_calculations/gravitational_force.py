def calculate_gravitational_force(m1, m2, r):
    G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
    force = G * (m1 * m2) / (r ** 2)
    return force

# Input masses and distance
mass1 = float(input("Enter the mass of the first object (in kg): "))
mass2 = float(input("Enter the mass of the second object (in kg): "))
distance = float(input("Enter the distance between the centers of the two objects (in meters): "))

# Calculate gravitational force
force = calculate_gravitational_force(mass1, mass2, distance)

print(f"The gravitational force between the objects is {force} N")