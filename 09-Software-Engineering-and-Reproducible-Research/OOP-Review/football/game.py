'''Game class to model a football game
'''
from teams import team_names
import random


class Game:
    '''Models a football game.

    Parameters
    -----------------------------
    teams : list
        list of length 2, strings of team names
    location : str
        city
    score : dict
        key - team name
        value - score for the team
    week : int
        week number during the season

    Attributes - only shows up after you run get_winning_team
    -----------------------------
    winning_team_ : str
        team name
    losing_team_ : str
        team name
    '''

    def __init__(self, teams=None, location=None, score=None, week=None):
        self.teams = teams
        self.location = location
        if teams and not score:
            self.score = {teams[0]: 0, teams[1]: 0}
        else:
            self.score = score
        self.week = week

    def touchdown(self, team, extra_point=1):
        '''record td for a team
        Parameters
        -----------------------------
        team : str
            team that scored
        extra_point : int
            extra points earned in extra point play
        '''
        if team not in self.teams:
            raise ValueError('team parameter must be in self.teams')
        else:
            self.score[team] += (6 + extra_point)

    def field_goal(self, team):
        '''record td for a team
        Parameters
        -----------------------------
        team : str
            team that scored
        '''
        if team not in self.teams:
            raise ValueError('team parameter must be in self.teams')
        else:
            self.score[team] += 3

    def safety(self, TODO):
        pass  # TODO (a safety is worth 2 points)

    def get_winning_team(self):
        '''When game is done, this can be run to add attributes
        winning_team_ and losing_team_ to the game to easily see who won
        '''
        # If it's a tie, let's randomly break that tie and say one
        # team scored a touchdown in over time...
        if self.score[self.teams[1]] == self.score[self.teams[0]]:
            self.touchdown(self.teams[0])

        v = list(self.score.values())
        k = list(self.score.keys())
        self.winning_team_ = k[v.index(max(v))]
        self.losing_team_ = k[v.index(min(v))]

        return self.winning_team_, self.losing_team_
