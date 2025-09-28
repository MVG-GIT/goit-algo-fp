def draw_square(t, p1, p2, p3, p4):
    t.penup()
    t.goto(p1)
    t.pendown()
    for p in [p2, p3, p4, p1]:
        t.goto(p)


def pythagoras_tree(t, level, p1, p2):
    if level == 0:
        return
    
    # vector of the bottom side
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    # other two points of the square
    p3 = (p2[0] - dy, p2[1] + dx)
    p4 = (p1[0] - dy, p1[1] + dx)

    # draw current square
    draw_square(t, p1, p2, p3, p4)

    # top point (corner between p3 and p4)
    px = p4[0] + (dx - dy) / 2
    py = p4[1] + (dy + dx) / 2
    p5 = (px, py)

    # recursive calls for two branches
    pythagoras_tree(t, level - 1, p4, p5)
    pythagoras_tree(t, level - 1, p5, p3)





def draw_figure(turtle, level, p1=(-50, -250), p2=(50, -250)):
    return pythagoras_tree(turtle, level, p1, p2)