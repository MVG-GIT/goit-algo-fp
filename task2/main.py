import turtle

from figure import draw_figure

rec_bound_lw = 0
rec_bound_hi = 9

def main():
    while True:
            try:
                level = int(input(f"Enter recursion level {rec_bound_lw} to {rec_bound_hi}: "))
                if level < 0:
                    print("Level must be a positive number.")
                if level < rec_bound_lw or level > rec_bound_hi:
                    print(f"Level must be within {rec_bound_lw} to {rec_bound_hi}.")
                else:
                    break
            except ValueError:
                print("Integer only, try again.")


    screen = turtle.Screen()
    screen.setup(width=800, height=800)

    screen.bgcolor("white")

    t = turtle.Turtle()
    t.hideturtle()
    turtle.tracer(0, 0)   

    draw_figure(t, level)

    turtle.update()   
    screen.mainloop()








main()
