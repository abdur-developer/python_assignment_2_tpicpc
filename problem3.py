#🟢 Problem 3: Area of a Triangle using Function 🔺
def triangle_area(base, height):
    return 0.5 * base * height

base = int(input("Enter base: "))
height = int(input("Enter height: "))
print("Area of triangle: ", triangle_area(base, height))