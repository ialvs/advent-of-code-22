def get_move_score(move):
    if (move == 'A'):
        return 1
    elif (move == 'B'):
        return 2
    elif (move == 'C'):
        return 3
    else:
        return 0


def get_total_score(opponent_move, user_move):
    points = get_move_score(user_move)

    if (opponent_move == user_move):
        points += 3

    elif ((opponent_move == 'A' and user_move == 'C') or
          (opponent_move == 'B' and user_move == 'A') or
            (opponent_move == 'C' and user_move == 'B')):
        points += 0

    elif ((opponent_move == 'C' and user_move == 'A') or
          (opponent_move == 'A' and user_move == 'B') or
            (opponent_move == 'B' and user_move == 'C')):
        points += 6
    return points

def choose_user_move(desired_outcome,opponent_move):
    if (desired_outcome == 'Y'):
        return opponent_move
    
    elif (desired_outcome == 'X'):
        
        if (opponent_move == 'A'):
            return 'C'
        elif (opponent_move == 'B'):
            return 'A'
        elif(opponent_move == 'C'):
            return 'B'
    
    elif (desired_outcome == 'Z'):

        if (opponent_move == 'A'):
            return 'B'
        elif (opponent_move == 'B'):
            return 'C'
        elif (opponent_move == 'C'):
            return 'A'

with open('input.txt') as input:
    lines = input.readlines()

sum = 0

for line in lines:
    moves = line.split(' ')
    desired_outcome = moves[1].split('\n')
    round_score = get_total_score(moves[0],choose_user_move(desired_outcome[0],moves[0]))
    sum += round_score

print(sum)    
    
