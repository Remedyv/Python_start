def setup():
    size(600,500)
def draw():
    
    global s, m, h
    s = second()
    m = minute()
    h = hour()
    ms = millis()
    background(255)
    noFill()
    strokeWeight(25)
    rect(100,250,400,200)
    fill(0)
    rect(100,450,30,50)
    rect(470,450,30,50)
    rect(200,230,200,15)
    textSize(300)
    text(":",265,425)
    textSize(170)
    text(m,320,410)
    text(h,150,410)
