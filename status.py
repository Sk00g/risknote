import requests
from skraper import Skraper

url = 'https://www.conquerclub.com/login.php'

payload = {
    'username': 'Sk00g',
    'password': 'nautica',
    'connect': "",
    'direct': '35###www.conquerclub.com###',
    'submit': 'Login',
    'redirect': "",
    'protocol': 'HTTPS'
}

response = requests.post(url, data=payload)

# with open('test_data.dat', 'w') as file:
#     file.write(response.text)

scraper = Skraper()
scraper.set_data(response.text)
# with open('test_data.dat', 'r') as file:
#     scraper.set_data(file.read())

games = []

game_summaries = scraper.get_indices_within('class=game_summary',
                                             '</span></span></li></ul></div></td>')

for id_pair in game_summaries:
    map_tag = scraper.get_values_within('rel=\'lightbox\' title=\'',
                                         'border=0  height=30 src=',
                                        id_pair[0],
                                        id_pair[1])[0]
    player_tags = scraper.get_values_within('class=\'status_',
                                            '</A>',
                                            id_pair[0],
                                            id_pair[1])

    game = {
        'map': map_tag.split(',')[0],
        'map_id': int(map_tag.split('=')[1][6:-4]),
        'players': []
    }

    for tag in player_tags:
        game['players'].append({
            'name': tag.split('>')[-1],
            'has_turn': tag[:tag.find('\'')] == 'green',
            'id': int(tag.split('&')[-1][2:7])
        })

    games.append(game)

for game in games:
    print('--- MAP: %s (%d) - %d PLAYER ---' % (game['map'],
                                                game['map_id'],
                                                len(game['players'])))
    count = 0
    for player in game['players']:
        count += 1
        print('\t(%d) - %s     %s' % (player['id'],
                                       player['name'],
                                       'ACTIVE' if player['has_turn'] else ''))

    print('\n')

for game in games:
    for player in game['players']:
        if player['name'] == 'Sk00g' and player['has_turn']:
            print('\n---------------------------')
            print('Sk00g your turn on %s!!!' % game['map'])
            print('---------------------------\n')


print('\n... finished')