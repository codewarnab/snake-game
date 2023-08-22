# shows scoreboard in the screen 

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.highscore = 0 
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        '''update the score every time '''
        with open("pyhon programs/day24/high_score.txt") as file :
            highscore = file.read()
        self.write(f"Score: {self.score} High Score :{highscore}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score>self.highscore:
            self.highscore = self.score
            with open("pyhon programs/day24/high_score.txt",mode= "w") as file : 
                file.write(str(self.highscore))
                


    def increase_score(self):
        ''' increase the score everytime snake eats food '''
        self.score += 1
        
        self.update_scoreboard()
