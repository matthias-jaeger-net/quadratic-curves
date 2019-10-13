# quadratic-curves

Write-up and documentation my process for creating visual compositions using the concept of quadratic equations.

![Cover](cover.jpg)
Beta version of the artwork using my building blocks

## A starting point - painting curves with brushes
In one atelier-session we were painting curves with brushes.I was amazed how easily an algorithmic compomposition can be done between two indiviuals. Later on I tried to recreate the algorithm in form of a python script and failed to achive the goals. This is a collection of my attempts to understand what it takes to create a visually interesting composition in the form of a python script.

# First Steps
## Starting small scale
There are many ways to create a curvy shape in Processing. You could look at the PShape object, the curveVertex of a shape or the curveTightness paramtet. All those thing help you to create curves on the computer. What I was looking for was one that enables me to store the points of a shape in a list. This way I can, at a later time, compare two shapes with each other. I didn't use the ``arc()`` method, nor the ``curveVertex()`` so because of this reason. First went for the most basic approach and attempted a single quadratic curve program.

- [x] Make a sketch that plots the points of a single curve
- [x] Pick one quadratic equasion and test values
- [x] Refactor to a function definition
- [x] Make a composition with multiple calls of that function

## Imagine the following program

![Curve example](curve.jpg)
An upwards pointing quadratic curve plotted with the code below.

```python
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
```

```python
for x in range(-r, r):
    y = k * x * x
    point(x, y)
```

## Expressing the curve is a main building block
It's been a while since I got introduced to quadratic curves in school, I had to freshen up my knowledge a bit. For the first sketch I work with the formula ``F(x) = k * x * x``where k is a value that influences the shape of the curve in my drawing. When k is a negative value the curve opens downwards, when k is a positive value the opposite. The curve also will flatten out to a straight line when k approaches ``Infinity``

## The formula written in code
I imagine a simple Processing sketch (in python mode) that saves an image with a fixed number points I want to plot.
```python
for x in range(-r, r):
    y = k * x * x
    point(x, y)
```
