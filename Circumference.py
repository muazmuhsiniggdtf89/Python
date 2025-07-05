# Function to calculate the circumference of a circle
def calculate_circumference(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference


radius = int(input("Enter the radius of the circle: "))
result = calculate_circumference(radius)
print("The circumference of the circle is:", result)
