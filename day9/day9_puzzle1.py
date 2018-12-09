from collections import defaultdict
import datetime
import pprint


pp = pprint.PrettyPrinter()


def place_marble(current, marble, circle):
    score = 0
    # initial condition
    if not circle and marble == 0:
        insertion_point = 0
        circle = [0]
    # initial condition
    elif marble == 1:
        insertion_point = 1
        circle.append(1)
    # if the new marble is a multiple of 23, then don't place it - score it plus the marble CCW 7 from the current
    elif marble % 23 == 0:
        score += marble
        deletion_point = current - 7
        if deletion_point < 0:
            deletion_point += len(circle)
        score += circle[deletion_point]
        del circle[deletion_point]
        insertion_point = deletion_point
        if insertion_point > len(circle):
            insertion_point = 0
    # insert the marble according to the rules - between CW 1 and CCW 2
    else:
        insertion_point = current + 2
        if insertion_point > len(circle):
            insertion_point -= len(circle)
        circle.insert(insertion_point, marble)
    return insertion_point, score, circle


def play_marbles(players, marbles):
    circle = []
    current = 0
    scores = defaultdict(int)
    for marble in range(marbles+1):
        current, score, circle = place_marble(current, marble, circle)
        scores[marble % players] += score
    return scores


games = [(9, 25, 32),
         (10, 1618, 8317),
         (13, 7999, 146373),
         (17, 1104, 2764),
         (21, 6111, 54718),
         (30, 5807, 37305),
         (411, 72059, None),
         (411, 72059*100, None)]

for game in games:
    before = datetime.datetime.now()
    player_scores = play_marbles(game[0], game[1])
    high_score = max(player_scores, key=player_scores.get)
    elapsed = datetime.datetime.now() - before
    success_string = " - success!" if game[2] and player_scores[high_score] == game[2] else ""
    print(f'For Game {game}, high score is {player_scores[high_score]}{success_string}, calculated in {elapsed}')
