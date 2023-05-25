#Это игра в Жанре кликер
#Звук работает только на proccesing 3. На более новой версии нужно удалить строчки кода:
#add_library('sound')  (9 строчка)
#a = SoundFile(this,"ll.mp3")    (32 строчка)
#с = SoundFile(this,"up.mp3")    (33 строчка)
#a.play()     (79 строчка)
#с.play()      (95,99,110,114 строчка)
#Чтобы играть с звуком нужно зайти в Инструменты,Manage Tools,Libraries,найти Sound и установить!
add_library('sound')
a = 0
с = 0
clicks = 500000
img = 0
img2 = 0
img3 = 0
buy = 100
xDif = 500
yDif = 100
xDif2 = 500
yDif2 = 200
click = 1
buy2 = 100
last_time = 0
interval = 2
cps = 0
r = 0
g = 0
b = 0
def setup():
    global a,img, b, clicks, img2, buy2, xDif2, yDif2, last_time,interval,cps,img3,c
    size(600,400)
    a = SoundFile(this,"ll.mp3")
    с = SoundFile(this,"up.mp3")
    img = loadImage("photo.png")
    img2 = loadImage("upgrade.png")
    img3 = loadImage("smile.png")
    last_time = second()
def draw():
    background(255)
    global a,img, b, clicks, img2, buy, buy2, xDif2, yDif2, last_time,interval,cps,r,g,img3,c
    if second() - last_time >= interval:
        if cps > 0:
            clicks+=cps
            last_time = second()
    image(img,200,200,220,220)
    image(img2,500,100,50,50)
    image(img2,500,200,50,50)
    image(img3,465,30,100,50)
    fill(0)
    textSize(35)
    textAlign(CENTER,CENTER)
    fill(r,g,b)
    text("!!!Proekt Clicker!!!",465,10)
    fill(0)
    text(clicks,320,100)
    textSize(25)
    text(buy,525,170)
    text(buy2,525,270)
    textSize(20)
    text("Cpc/Per click:",57,10)
    if buy > 3699:
        fill(255,0,0)
    else:
        fill(0)
    text(click,137,10)
    fill(0)
    text("Cps/Per second:",67,30)
    if buy2 > 3699:
        fill(255,0,0)
    else:
        fill(0)
    text(cps,152,30)
    r = random(1,255)
    g = random(1,255)
    b = random(1,255)
def mouseClicked():
    global clicks,xDif,yDif,click,buy, buy2, xDif2, yDif2, last_time,interval,cps,c
    fill(0)
    a.play()
    xDif = 500 - mouseX
    yDif = 100 - mouseY
    xDif2 = 500 - mouseX
    yDif2 = 200 - mouseY
    clicks += click
    if sqrt(xDif*xDif + yDif*yDif) < 50:
        if buy < clicks:
            if buy > 3699:
                textSize(100)
                text("no",150,300)
            else:
                clicks -= buy
                if buy > 499:
                    buy += 400
                    click *= 2
                    с.play()
                else:
                    buy += 200
                    click *= 2
                    с.play()
    if sqrt(xDif2*xDif2 + yDif2*yDif2) < 50:
        if buy2 < clicks:
            if buy2 > 3699:
                textSize(100)
                text("no",150,300)
            else:
                clicks -= buy2
                if buy2 > 499:
                    buy2 += 400
                    cps *= 2
                    с.play()
                else:
                    buy2 += 200
                    cps += 1
                    с.play()
