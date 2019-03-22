'''Tracks the season perfomance of different teams and generates a
'''
from possible_values import *
from game import Game
from random import randint, uniform, sample


def generate_rand_games(n=15):
    '''Generate n random games using value lists in possible_values
    '''
    # Begin with enpty list
    games = []

    # For the specified number of games, create an instance of the Game
    # class...
    # TODO - You can also include the location and week number if desired
    for _ in list(range(n)):
        # Get team names by sampling team_names from possible_values
        game = Game(teams=sample(team_names, k=2))

        # Give each team a random number (from 0 to 3) of each:
        # touchdowns and field goals
        for i in list(range(randint(0, 4))):
            game.field_goal(game.teams[0])

        for j in list(range(randint(0, 4))):
            game.field_goal(game.teams[1])

        for k in list(range(randint(0, 4))):
            game.touchdown(game.teams[0])

        for l in list(range(randint(0, 4))):
            game.touchdown(game.teams[1])

        games.append(game)
    return games


def season_report(games):
    '''Print out a season report given a list of games

    Parameters
    -----------------------------
    games : list
        a list of Game class instances
    '''
    # Instantiate empty set and lists
    teams = set()
    winning_teams = []
    losing_teams = []
    winning_team_total_points = 0
    losing_team_total_points = 0

    # Loop through the games
    for game in games:
        # Ensure both teams are included in the set of teams
        teams.add(game.teams[0])
        teams.add(game.teams[1])

        # Record the winning and losing teams for each game
        winning_team, losing_team = game.get_winning_team()
        winning_teams.append(winning_team)
        losing_teams.append(losing_team)

        # Easy way to keep track of points
        winning_team_total_points += game.score[winning_team]
        losing_team_total_points += game.score[losing_team]

    # Calculates the average points scored by winning team and losing team
    # in a game
    winning_team_average = (winning_team_total_points /
                            len(winning_team))
    losing_team_average = (losing_team_total_points /
                           len(losing_team))

    # Instantiate dict to keep track of individual team records
    team_records = {}

    # Could use a defaultdict from collections, but I chose to
    # manually set the default value for each team in the teams set
    for team in list(teams):
        team_records[team] = [0, 0]

    # Add one for each of the wins (position 0) and losses (position 1)
    for team in winning_teams:
        team_records[team][0] += 1

    for team in losing_teams:
        team_records[team][1] += 1

    # Finally print the report
    print('\n\n--------Football Season Report--------\n')
    print('Team Records')
    print('---------------------------------')
    for team, record in team_records.items():
        print(f'{team}: {record[0]} W, {record[1]} L')
    print('---------------------------------')
    print(f'Average Score of Winning Team: {winning_team_average: .1f}')
    print(f'Average Score of Losing Team: {losing_team_average:.1f}\n')

    # You could choose to return something here if you wanted TODO


if __name__ == '__main__':
    season_report(generate_rand_games())
