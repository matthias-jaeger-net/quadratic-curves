"""
Saves an image of a grid with a quadratic curve in each cell
"""
def setup() :
    
    # Create a window to draw in
    size(900, 400)
    
    # Loop in u and v direction
    for u in range(9):
        for v in range(4):
            # Draw the grid bounds with a rectangle
            rect(u * 100, v * 100, 100, 100)
            
            # Randomize the look of each curve
            k = random(-0.03, 0.03)
            
            for x in range(-50, 50) :
                # Calculate a y component 
                y = k * x * x
                
                # Draw the points to the window
                point(x + u * 100 + 50, y + v * 100 + 50)
    
    # Done with calculation and drawing
    save("out.jpg")
    exit()
