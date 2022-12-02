def get_move_score(move):
    if (move == 'X'):
        return 1
    elif (move == 'Y'):
        return 2
    elif (move == 'Z'):
        return 3
    else:
        return 0


def get_total_score(opponent_move, user_move):
    points = get_move_score(user_move)

    if ((opponent_move == 'A' and user_move == 'X') or
            (opponent_move == 'B' and user_move == 'Y') or
            (opponent_move == 'C' and user_move == 'Z')):
        points += 3
    
    elif ((opponent_move == 'C' and user_move == 'X') or
          (opponent_move == 'A' and user_move == 'Y') or
            (opponent_move == 'B' and user_move == 'Z')):
        points += 6
    return points


with open('input.txt') as input:
    lines = input.readlines()

sum = 0

for line in lines:
    moves = line.split(' ')
    player_move = moves[1].split('\n')
    round_score = get_total_score(moves[0],player_move[0])
    sum += round_score

print(sum)    
    
