import turtle as t

# Set up the turtle screen
t.setup(800, 600)
t.title("Lionel Messi")

# Function to draw a circle
def draw_circle(color, x, y, radius):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y - radius)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw an eye
def draw_eye(x, y):
    draw_circle("black", x, y, 15)
    draw_circle("white", x, y - 5, 5)

# Function to draw Messi's face
def draw_messi_face():
    t.speed(1)

    # Draw Messi's face
    draw_circle("lightgreen", 0, -100, 100)

    # Draw Messi's eyes
    draw_eye(-30, 0)
    draw_eye(30, 0)

    # Draw Messi's mouth
    t.penup()
    t.goto(-20, -30)
    t.pendown()
    t.goto(20, -30)

    # Hide the turtle
    t.hideturtle()

# Draw Messi's face
draw_messi_face()

# Close the turtle graphics window on click
t.exitonclick()
