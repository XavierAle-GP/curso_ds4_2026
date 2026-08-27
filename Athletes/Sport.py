class Sport:
    """Sport class represents a sport in a tournament"""
    max_score = {
        "Soccer":20,
        "Baseball":50,
        "Football":70,
        "Basketball": 150,
        "Volleyball": 3,
        "Tennis":3
    }
    def __init__(self, sport_name:str, num_players:int, league:str):
        if sport_name in self.max_score:
            self.sport_name = sport_name
            self.num_players = num_players
            self.league = league
        else:
            raise ValueError(
                "Sport name should be:{', '.join(self.max_score.keys{})}"
            )
    def __srt__(self):
        return ("{self.sport_name} with{self.num_players} in league: {self.league}")
    def __repr__(self) -> str:
        return f"Sport('{self.sport_name}','{self.num_players}','{self.league}')"
    def display(self):
        print(f"|{self.sport_name}|{self.num_players}|{self.league}")
if __name__ == '__main__':
    s = Sport('Soccer',11,'LigaMX')
    b = Sport('Baseball',9,'LMP')
    print(b)
    print(s)
    s.display()
    b.display()
    """r = Sport('Rugby',10,'RugbyAus')"""