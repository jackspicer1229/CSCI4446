import turtle, math


smallestLength = 1
length = 200
rightAngle = 70
leftAngle = 10
rightShorten = .64
leftShorten = .64

def draw_tree(t, length):
	if(length > smallestLength):
		t.forward(length)
		t.right(rightAngle)
		draw_tree(t, length*rightShorten)
		t.left(rightAngle + leftAngle)
		draw_tree(t, length*leftShorten)
		t.right(leftAngle)
		t.backward(length)

def main():
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.backward(200)
    t.tracer(False)
    window = turtle.Screen()
    t.color("#000000")

    draw_tree(t, length)
    window.exitonclick()

if __name__ == "__main__":
    main()