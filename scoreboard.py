from turtle import Turtle
ALLIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()       # Score: 0

    def update_score(self):
        self.clear()  # clear everytime scoreboard is updated
        self.write(f'Score: {self.score} High Score: {self.highscore}', align= ALLIGNMENT, font= FONT)   # FOR EASY CUSTOMISATIONS

    def increase_score(self):
        self.score += 1
        self.clear() # To avoid overlapping scores
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt',mode='w') as data:
                data.write(f'{self.highscore}')

        self.score = 0  # reset score
        self.update_score()


    # def game_over(self):
    #     # Write this at center
    #     self.goto(0, 0)
    #     self.write('GAME OVER', align=ALLIGNMENT, font=FONT)
    #




