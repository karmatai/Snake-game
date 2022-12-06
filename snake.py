from turtle import Turtle
UP=90
DOWN=270
LEFT=180
RIGHT=0

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

move_distance=20





class Snake:
    def __init__(self):
        self.segment = []
        self.call_snake()
        self.head = self.segment[0]

    def call_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)



    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            new_x=self.segment[seg_num - 1].xcor()
            new_y= self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)



    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() !=UP:
            self.head.setheading(270)

    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.call_snake()
        self.head = self.segment[0]


    def extend(self):
        self.add_segment(self.segment[-1].position())




