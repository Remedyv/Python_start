# bg = 0

# def setup():
#     size(600,400)
    
# def draw():
#     global bg
#     background(bg)
#     #кнопка прямоугольная
#     fill(255,0,0)
#     # левый верхний угол 250 150, размеры 100 на 50
#     rect(250,150,100,50) # x от 250 до 250+100, y от 150 до 150 + 50
    
    
#     #круглая кнопка
#     #если круглая кнопка нажата
#     xDif = 400 - mouseX
#     yDif = 350 - mouseY
    
# def mouseClicked():
#     global bg
#     if mouseX > 250 and mouseX < 350 and mouseY > 150 and mouseY < 200:
#         bg = 255
x = 1
y = 1
x1 = 500
y1 = 1
img = 0
def setup():
    global img
    size(600,600)
    img = loadImage("Jota.png")
def draw():
    background(0)
    global x,y,img, x1,y1
    # image(img,100,100,100)
    rect(x,y,200,100)
    rect(x1,y1,200,100)
    x = x + 1
    y = y + 1
    x1 = x1 - 1
    y1 = y1 + 1
    
# def keyPressed():
#     if key == CODED:
#         if keyCode == UP:
#             text(u"Мой проект", 250,250)    
        
