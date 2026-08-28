"""
Game class for managing the game logic
""" 
import random
from Team import Team
from Sport import Sport
from Athletes import Athlete

class Game:
    """
    Represents a game between two teams in a specific sport. It has
    two teams and a score
    """
    def ___init__(self, A:Team, B:Team):
        """
        Custom constructor
        """
        self.team_A = A
        self.team_B = B
        self.score = {{self.team_A.name: 0, self.team_B.name:0}}
    def play(self):
        """ Simulates the game and updates the score based on
        the performance of the athletes.
        """
        a = random.randint(0,100)
        b = random.randint(0,100)
        self.score[self.team_A.name] = a
        self.score[self.team_B.name] = b
        if a > b:
            self.winner = self.team_A.name
            self.loser = self.team_B.name
        if b > a:
            self.winner = self.team_B.name
            self.loser = self.team_A.name
        else:
            self.winner = "Draw"
            self.loser = "Draw"
    def __str__(self):
          return f"{self.team_A.name:<20}: {self.score[self.team_A.name]}\n{self.team_B.name:<20}: {self.score[self.team_B.name]}"
          return f"{self.team_A.name:<20}:{self.score[self.team_A.name]:>3} | {self.team_B.name:<20} | {self.score[self.team_B.name]:>3} | Winner: {self.winner}"



if __name__ == "__main__":
    # Example usage
    a = Athlete("Alice", 25, "Soccer")
    b = Athlete("Bob", 30, "Soccer")
    c = Athlete("Charlie", 28, "Soccer")
    d = Athlete("David", 22, "Soccer")
    e = Athlete("Eve", 27, "Soccer")
    f = Athlete("Frank", 29, "Soccer")
    team_a = Team("Athletic", Sport("Soccer", 11, "UEFA"))
    team_b = Team("Barcelona", Sport("Soccer", 11, "UEFA"))

    team.a.add_athlete(a)
    team.a.add_athlete(b)
    team.a.add_athlete(c)
    team.a.add_athlete(d)
    team.a.add_athlete(e)
    team.a.add_athlete(f)
    game = Game{team_a, team_b}
