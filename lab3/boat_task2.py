from graph import *
#texture
brushColor(0,205,255)
rectangle(0,0,1000,1000)

brushColor('blue')
rectangle(0,300,1000,450)

brushColor(230,255,0)
rectangle(0,450,1000,1000)
#umbrella
brushColor('brown')
rectangle(100,600,110,400)
polygon([(20,440),(200,440),(105,400)])
line_umb_x = 25
for i in range (8):
    line(105,400,line_umb_x,440)
    line_umb_x+=20
#clouds
brushColor('white')
circle(100,50,20)
circle(120,40,20)
circle(140,50,20)
circle(160,40,20)
circle(100,70,20)

circle(100,70,20)
circle(120,70,20)
circle(140,70,20)
circle(160,70,20)

#sun
brushColor('yellow')
penColor('yellow')
circle(400,50,50)

#boat
penColor('black')
brushColor('brown')
rectangle(200,350,400,400)
penColor('brown')
circle(200,350,50)
brushColor('blue')
penColor('blue')
rectangle(0,300,400,350)
#boat nose
brushColor('brown')
penColor('black')
line(400,400,400,350)

polygon([(400,400),(400,350),(480,350)])
brushColor('black')
circle(420,370,13)
brushColor('white')
circle(420,370,11)
brushColor('black')
rectangle(300,350,305,250)

brushColor('white')
polygon([(305,350),(320,290),(350,290)])
polygon([(320,290),(350,290),(305,250)])




run()
