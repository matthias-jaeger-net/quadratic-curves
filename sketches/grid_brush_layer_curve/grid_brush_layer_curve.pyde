"""
Saves an image of a layered grid composition on a dark background
"""

def grid(layer, w, h, s) :
    r = w / s
    c = h / s
    for u in range(r) : 
        for v in range(c) : 
            cell(u, v, layer)

def curves(u, v, layer) :
    k = random(-0.03, 0.03)
    sw = random(0, 120) * layer
    for x in range(-120, 120) :
        y = k * x * x
        s = map(x, -50, 50, 1, sw)
        s = abs(cos(s * s) * sqrt(s))
        strokeWeight(s)
        point(x + u * 100 + 50, y + v * 100 + 50)
    
def cell(u, v, layer) :
    strokeWeight(1)
    noFill()
    rect(u * 100, v * 100, 100, 100)   
    if (random(0, 1) > 0.4) :
        curves(u, v, layer)

def setup() :
    size(2000, 1000)
    background(0)
    stroke(255, 100)
    for layer in range(3) :
        grid(layer, width, height, 100)
    save("out.jpg")
    exit()
