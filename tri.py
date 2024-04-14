import turtle

num_sides = int(input("请输入多边形的边数: "))
polygon = turtle.Turtle()
polygon.speed(0)
edge_colors = ['red', 'green', 'blue']
corner_colors = ['purple', 'orange', 'pink', 'brown']
angle = 360 / num_sides
for _ in range(num_sides):
    polygon.pencolor(edge_colors[_ % 3])  
    polygon.fillcolor(corner_colors[_ % 4]) 
    polygon.begin_fill()
    for _ in range(2):
        polygon.forward(100)  
        polygon.left(180 - angle)  
    polygon.end_fill()
    polygon.right(angle)  
turtle.done()
