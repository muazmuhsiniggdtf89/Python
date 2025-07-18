import math

try:
    angle_degree = float(input("Enter the angle in degrees: "))
    angle_radians = math.radians(angle_degree)  # Convert degrees to radians

    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    tan_value = math.tan(angle_radians)

    print("Angle (in degrees):", angle_degree)
    print("Sine value:", sin_value)
    print("Cosine value:", cos_value)
    print("Tangent value:", tan_value)

except ValueError:
    print("Invalid input! Please enter a number.")
