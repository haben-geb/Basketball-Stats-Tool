import constants
import copy



team = {
    'A': {'name': 'Panthers', 'experienced': [], 'inexperienced': []},
    'B': {'name': 'Bandits', 'experienced': [], 'inexperienced': []},
    'C': {'name': 'Warriors', 'experienced': [], 'inexperienced': []}
}


def clean_data():
    players = copy.deepcopy(constants.PLAYERS)

    for player in players:
        player['height'] = int(player['height'][0:2])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
    return players


def balance_teams():
    players = copy.deepcopy(clean_data())

    for data in ['A', 'B', 'C']:
        for player in players.copy():
            if len(team[data]['experienced']) != 3 and player['experience'] == True:
                team[data]['experienced'].append(player)
                players.remove(player)
            elif len(team[data]['inexperienced']) != 3 and player['experience'] == False:
                team[data]['inexperienced'].append(player)
                players.remove(player)




def get_team_stats():
    try:
        data = input('Pick a team: ').upper()
        players = team[data]['experienced'] + team[data]['inexperienced']
    except KeyError:
        print('Invalid input. Please enter only A, B, or C.')
    else:
        print('\nTeam: {} Stats'.format(team[data]['name']))
        print('-' * 20)
        print('Total players:', len(players))
        print('Total experience:', len(team[data]['experienced']))
        print('Total inexperience:', len(team[data]['inexperienced']))

        heights = [height['height'] for height in players]
        average_height = sum(heights) / len(heights)
        print(f'Average height: {average_height:.1f}')
        print('\nPlayers on Team:')
        player_names = [player['name'] for player in players]
        print('', ', '.join(player_names))

        guardian_list  = []
        for player in players:
            if 'and' in player['guardians']:
                guardian_list.append(player['guardians'].split(' and '))
            else:
                guardian_list.append(player['guardians'])

        guardian_name = []
        for guardian in guardian_list:
            if len(guardian) == 2:
                guardian_name.append(guardian[0])
                guardian_name.append(guardian[1])
            else:
                guardian_name.append(guardian)
        print('\nGuardians:')
        print('', ', '.join(guardian_name), '\n')


def run_app():
    clean_data()
    balance_teams()
    while True:
        print('BASKETBALL TEAM STATS TOOL\n\n', '-' * 4, 'MENU', '-' * 4, '\n')
        print('Here are your choices:\nA) Display Team Stats \nB) Quit\n')
        try:
            menu_option = input('Enter an option: ').upper()
            if menu_option not in ['A', 'B']:
                raise ValueError('-----> ERROR: Enter only A or B <-----')
        except ValueError as e:
            print(e)
        else:
            if menu_option == 'A':
                print(' A) Panthers\n', 'B) Bandits\n', 'C) Warriors\n')
                get_team_stats()
            elif menu_option == 'B':
                break
            to_continue = input('Press ENTER to continue...')
            print()
            if to_continue == '':
                continue







if __name__ == "__main__":
    run_app()
