def setup():
    size(354, 354)
    translate(width*0.5, height*0.5)
    k = 0 #random(-0.01, 0.01)
    c = 0 #random(-10.0, 10.0)
    for x in range(int(-width*0.5), int(width*0.5)):
        y = k * x * x + c
        point(x, y)
    save("out/curve-k-"+str(k)+".jpg")
