# quadratic-curves

Research on a visual composition of curves with the Processing IDE written in python mode.

![Cover](cover.jpg)

### Painting curves with brushes
In my last atelier session we were painting curves with brushes and I was amazed how easily an algorithmic type of compomposition can be done between two indiviuals. Later on I tried to recreate the algorithm in form of a python script and failed to achive the goals.

###  Plotting a curve in processing
Thhere are many ways to create a curvy shape in Processing, but I was looking for one that enables me to store the points of a shape in a list. Therefore I didn't use the ``arc()`` method, nor the ``curveVertex()``so far. I went for the most basic approach and attempted a single quadratic curve program.

#### Playing with things, like math ...
It's been a while since I got introduced to quadratic curves in school, I had to freshen up my knowledge a bit. For the first sketch I work with the formula ``F(x) = k * x * x``where k is a value that influences the shape of the curve in my drawing. When k is a negative value the curve opens downwards, when k is a positive value the opposite. The curve also will flatten out to a straight line when k approaches ``Infinity``

##### The formula written in code
```python
for x in range(-r, r):
    y = k * x * x
    point(x, y)
```
