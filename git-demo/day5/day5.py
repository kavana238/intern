# task 1 

def  calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = float(input("enter the length of the rectangle:"))
width = float(input("enter the width of the rectangle:"))

area, perimeter = calc_rectangle(length ,width)

print(f"area: {area}")
print(f"perimeter: {perimeter}")

# task 2
