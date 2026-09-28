productcode = input()
destination = 0
packaging = 0

shape = productcode[0:4]   
color = productcode[4:7]    
maxdim = int(productcode[7:10])   
mass = int(productcode[10:14])
condition = productcode[14:15]

if shape == "CUBE" and (mass <= 2500 or maxdim <= 60):
        destination = "D"
        packaging = "Crate"
if condition == "D" or mass > 2000 or maxdim > 50:
    destination = "Inspect"
    packaging = "Hold"
else:
    if shape == "CONE" or mass > 1000:
        packaging = "Crate"
    else:
        if shape == "BALL":
            packaging = "Padded"
            if maxdim > 10 and color == "RED":
                destination = "B"
            else:
                destination = "A"   
        else:
            if shape == "CUBE":
                if (color == "GRN" or color == "BLU") and maxdim < 10:
                    destination = "C"
                else:
                    destination = "D"
            else:
                destination = "E"

print(destination)
print(packaging)

