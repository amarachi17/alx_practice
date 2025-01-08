x = 10

def outer_function():
    x = 17
    
    def inner_function():
        x = 28
        print("Inner function:", x)
        
    inner_function()
    
    print("Inner function, local x: ", x)
    
outer_function()
print("Outer function, global x: ", x)