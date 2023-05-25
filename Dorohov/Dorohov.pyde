bg = 0

def setup():
    size(600,400)
    
def draw():
    global bg
    background(bg)
    #кнопка прямоугольная
    fill(255,0,0)
    # левый верхний угол 250 150, размеры 100 на 50
    rect(250,150,100,50) # x от 250 до 250+100, y от 150 до 150 + 50
    
    
    #круглая кнопка
    #если круглая кнопка нажата
    xDif = 400 - mouseX
    yDif = 350 - mouseY
    
def mouseClicked():
    global bg
    if mouseX > 250 and mouseX < 350 and mouseY > 150 and mouseY < 200:
        bg = 255
    
    
        
        
