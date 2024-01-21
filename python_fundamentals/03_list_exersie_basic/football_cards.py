cards = input().split()

first_team_sent_off_player = []
second_team_sent_off_player = []

should_terminate = False

for card in cards:
    if card in first_team_sent_off_player or card in second_team_sent_off_player:
        continue

    cards_args = card.split('-')
    team_name = card[0]
    player_number = card[1]

    is_first_team = team_name == 'A'
    if is_first_team:
        first_team_sent_off_player.append(card)
    else:
        second_team_sent_off_player.append(card)

    if len(first_team_sent_off_player) > 4 or len(second_team_sent_off_player) > 4:
        should_terminate = True
        break

player_count = 11
first_team = player_count - len(first_team_sent_off_player)
second_team = player_count - len(second_team_sent_off_player)
print(f'Team A - {first_team}; Team B - {second_team}')

if should_terminate:
    print('Game was terminated')
