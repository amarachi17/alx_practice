x = 10
def local_global():
    x = 20
    print("Inside local_global:", x)
    
local_global()
print("Outside the function, global x: ",x)