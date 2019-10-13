"""
Saves an image of a simple grid
"""
def setup() :
    
    # Create a window to draw in
    size(900, 400)
    
    # Define a varibale for the scaling
    s = 100
    
    # Loop in u and v direction
    for u in range(9):
        for v in range(4):
            rect(u * s, v * s, s, s)
    
    # Done with calculation and drawing
    save("out.jpg")
    exit()
