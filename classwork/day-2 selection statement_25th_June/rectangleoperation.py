''' Program to calculate perimeter and area of the rectangle '''
#input of length from the user
length = float(input("Enter the length of the rectangle(in cm): "))
#validating the length
if length < 0:
    exit("Length cannot be negative.")
#input of breadth from the user
breadth = float(input("Enter the breadth of the rectangle(in cm): "))
#validating the breadth
if breadth < 0:
    exit("Breadth cannot be negative.")
#-----------------------------------------------------
#Displaying data to the user
print("-----------------------------------------------------")
print("--------- Rectangle -------")
print("Length : ", length, "cm")
print("Breadth : ", breadth, "cm")
#-----------------------------------------------------
#Displaying perimeter of the rectangle
print("Perimeter : ", 2 * (length + breadth), "cm")
#-----------------------------------------------------
#Displaying area of the rectangle
print("Area : ", length * breadth, "sq.cm")
#---------------------------------------------------------
