productcode = input("Product Code: ")
destination = 0

shape = productcode[0:4]   
color = productcode[4:7]    
maxdim = int(productcode[7:10])   
mass = int(productcode[10:14])
condition = productcode[14:15]

if condition == "D" or mass > 2000 or maxdim > 50:
    if shape == "CUBE" and mass < 2500 and maxdim < 60:
        destination = 
    destination = "Inspect"
else:
    if shape == "BALL":
        if maxdim > 10 and color == "RED":
            destination = "B"
        else:
            destination = "A"   
    else:
        if shape == "CUBE":
            if color == "GRN" or color == "BLU" and maxdim < 10:
                destination = "C"
            else:
                destination = "D"
        else:
            destination = "E"
print(destination)

if 
