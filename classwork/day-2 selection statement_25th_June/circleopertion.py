'''Program to calulate area of a circle'''
#input of radius from the user
radius = float(input("Enter the radius of the circle(in cm): "))
#validating the radius
if radius < 0:
    exit("Radius cannot be negative.")
#-----------------------------------------------------
#Displaying data to the user
print("Radius of the circle: ", radius, "cm")
#Displaying area of the circle
print("Area of the circle: ", 3.14 * (radius **2), "sq.cm")

#------------------------------------------------------------------
''' Output:
Enter the radius of the circle(in cm): 5
Radius of the circle:  5.0 cm
Area of the circle:  78.5 sq.cm'''
