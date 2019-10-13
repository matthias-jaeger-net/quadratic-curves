# quadratic-curves
Research on a visual composition of curves with the Processing IDE written in python mode.

´´´
def parabula(k, s):
    #beginShape()
    for x in range(-150, 150):
        y = k * x * x
        strokeWeight(map(x, -150, 150, 1, s))
        point(x, y)
    #endShape()
´´´
