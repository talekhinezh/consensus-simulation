import turtle
import time
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("utxo")
wn.tracer(0)


balls = []
free = []
tx_id = 0

def add_ball(parent, parent_id, tx_id):
	ball = free.pop() if len(free) > 0 else turtle.Turtle()
	ball.shape("circle")
	ball.penup()
	ball.speed(0)
	ball.color('green')
	ball.goto(550, random.randint(-200, 200))
	ball.parent = parent
	ball.parent_id = parent_id
	ball.weight = 0.0
	ball.is_parent = False
	ball.prepared = False
	ball.tx_id = tx_id
	balls.extend([ball])

pencil = turtle.Turtle()
pencil.penup()
pencil.speed(0)
pencil.color('gray')

add_ball(None, None, tx_id)

while True:
	wn.update()
	pencil.clear()
	for b in balls:
		if (b.weight < 0.5):
			b.weight += 0.002
			b.color((b.weight, 0.0, 0.0))

		if b.weight > 0.05 and not b.is_parent:
			b.is_parent = True
			tx_id = tx_id + 1
			parent = balls[random.randint(len(balls) / 2, len(balls) - 1)]
			parent_id = parent.tx_id
			add_ball(parent, parent_id, tx_id)

		pencil.penup()
		pencil.speed(1)
		if b.xcor() > -1000:
			b.setx(b.xcor() - 2)
			if (b.parent is not None) and (b.parent_id == b.parent.tx_id) and b.xcor() > -800:
				pencil.goto(b.xcor(), b.ycor())
				pencil.setheading(pencil.towards(b.parent.xcor(), b.parent.ycor()))
				pencil.pendown()
				distance = pow(pow(b.parent.xcor() - b.xcor(), 2) + pow(b.parent.ycor() - b.ycor(), 2), 0.5)
				pencil.fd(distance - 12)
				pencil.stamp()
		else:
			balls.remove(b)
			free.extend([b])
			b.clear()
			
	time.sleep(1 / 30.0)

turtle.mainloop()
