class Team:
    def __init__(self, name):
        self.name = name
        self.opponents = []

    def get_ops(self):
        return self.opponents

    def create_ops(self, teams):
        for team in teams:
            if team.name == self.name:
                pass
            else:
                self.opponents.append(team.name)
       
       



        