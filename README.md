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

def setup():
    size(800, 800)
    background(0)
    noFill()
    for i in range(9):
        for j in range(9):
            stroke(255, random(255))

            pushMatrix()
            translate(i * 100, j * 100)
            rect(0, 0, 100, 100)
            if (random(0, 1) > 0.5) : rotate(PI / 2)
            parabula(random(-0.01, 0.01), random(10, 20))
            
            translate(random(100), random(100))
            parabula(random(-0.01, 0.01), random(1, 3))

            popMatrix()

´´´
