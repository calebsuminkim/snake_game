from food import Food


class Item(Food):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.goto(-100, -100)
