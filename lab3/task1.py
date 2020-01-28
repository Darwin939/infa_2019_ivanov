from graph import *
#face
brushColor('yellow')
circle(300,200,100)
#mouth
brushColor('black')
rectangle(250,250,350,270)
#left eye
brushColor('red')
circle(250,170,25)
brushColor('black')
circle(250,170,10)

#right eye
brushColor('red')
circle(350,170,25)
brushColor('black')
circle(350,170,10)

#left eyebrow
brushColor('black')
polygon([(270,150),(270,160),(190,100),(190,90)])

#right eyebrow
polygon([(330,150),(330,140),(400,90),(400,100)])
run()