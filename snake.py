from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20 # When snake eat an item, the speed should be changed.
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]            # snake's head
        self.step = 20

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        # new_segment.speed("slowest")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
                seg.goto(1000, 1000) # 화면에서 사라지게 만듬
        self.segments.clear() # 뱀 삭제
        self.create_snake() # 새 뱀 생성
        self.head = self.segments[0]

    def extend(self):
        # Create a new one on where the last segment was.
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.step)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # else:
        #     self.head.setheading(self.head.heading())

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)      # 진행 방향과 반대로 움직일 수 없다(180도 꺾을 수 없다).

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
