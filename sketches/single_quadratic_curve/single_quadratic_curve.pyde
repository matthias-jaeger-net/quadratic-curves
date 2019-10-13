"""
Saves an image of a single quadratic curve
"""

def setup() :

    # Create a 900x354 window
    size(900, 354)
    
    # Move the origin to the center
    translate(width * 0.5, height * 0.5)
    
    # Cover the width as range for x
    for x in range(int(-width*0.5), int(width*0.5)) :
    
        # The k-parameter affects the look of the graph
        k = -0.0009
        
        # Calculate a y component with a quadratic formula
        y = k * x * x
        
        # Draw the points to the window
        point(x, y)
    
    # Done with calculation and drawing
    save("out.jpg")
    
    exit()
