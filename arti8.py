import turtle

luiz = turtle.Turtle()
luiz.pencolor("red")

def desenhe_flore():
    for _ in range(6):
        for _ in range(8):
                luiz.forward(20)
                luiz.right(30)
        luiz.right(60)
desenhe_flore()            
luiz.penup()
luiz.backward(150)
luiz.pendown()
desenhe_flore()           
luiz.penup()
luiz.backward(150)
luiz.pendown()
desenhe_flore()