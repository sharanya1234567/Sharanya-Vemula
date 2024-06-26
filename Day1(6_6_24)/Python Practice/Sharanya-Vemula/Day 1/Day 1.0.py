#10.1. Area Calculator:
#Create a function Calculate_area(shape, dimensions) that takes the shape (e.g., "rectangle", "circle") and its dimensions as arguments.
#The function should calculate the area based on the shape and return the result.
#Implement logic for handling different shapes (rectangle, circle) and their corresponding dimensions (length, width for rectangle; radius for circle).


def Calculate_area(shape, dimensions):
    if shape == "rectangle":
        length, width = dimensions
        return length * width
    elif shape == "circle":
        radius = dimensions[0]
        return 3.14 * (radius ** 2)
    else:
        return None

rectangle_area = Calculate_area("rectangle", [6, 3])
print("Area of rectangle:", rectangle_area)

circle_area = Calculate_area("circle", [8])
print("Area of circle:", circle_area)


 


 
 