from processing.Sound import SoundFile

img1 = 0
img = 0
img2 = 0
f = 0
color 





def setup():
    file = SoundFile(this, "vine-boom.mp3")
    file.play()
    global img, img1, img2, f
    size(800, 600)
    music = SoundFile
  

    img = loadImage("photo.jpeg")
    img1 = loadImage("img1.png")
    img2 = loadImage("img2.png")
    f = createFont("Arial",16)


def draw():
    global img, img1, img2, f
    background(0)
    textFont(f,30) 
  

    image(img, width/2-img.width/2, height/2-img.height/9)
  

    x1 = 30
    y1 = 10
    x2 = 500
    y2 = 10



    image(img1, x1, y1)
    text("Coding", x1 + 50, y1 + img1.height + 30)
    noFill()
    stroke(random(255), 0, 0)
    rect(x1, y1, img1.width, img1.height)
    image(img2, x2, y2)
    text("Games", x2 + 70, y2 + img2.height + 30)
    noFill()
    stroke(random(255), random(255), random(255))
    rect(x2, y2, img2.width, img2.height)
