"""
Saves an image of a single quadratic curve with a "brushed" look
"""

def setup() :

    # Create a 900x354 window
    size(900, 354)

    # Move the origin to the center
    translate(width * 0.5, height * 0.5)

    r = 200

    # Make a short curve
    for x in range(-r, r) :

        # The k-parameter affects the look
        k = -0.001

        # Calculate a y component
        y = k * x * x

        #
        # Simulating an even preassured brush stroke
        #
        # Map the loop variable to a value between -0.5 and 0.5
        s = map(x, -r, r, 1, 100)

        # Then take the absolute value of this to get only positive values
        s = abs(cos(s * s) * sqrt(s)) 

        # Assigning the effect to the stroke
        strokeWeight(s)

        # Draw the points to the window
        point(x, y)

    # Done with calculation and drawing
    save("out.jpg")

    exit()
