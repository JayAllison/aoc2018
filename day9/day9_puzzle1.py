from collections import deque
import datetime
import pprint


pp = pprint.PrettyPrinter()


def play_marbles(players, marbles):
    # http://www.monitis.com/blog/python-performance-tips-part-1/
    # deque is way better for insertions/deletions than list for large data sets
    circle = deque([0, 1])
    scores = [0 for _player in range(players)]
    for marble in range(2, marbles+1):
        score = 0
        # initial condition
        # if the new marble is a multiple of 23, then don't place it - score it plus the marble CCW 7 from the current
        if marble % 23 == 0:
            score += marble
            circle.rotate(7)
            score += circle.pop()
            circle.rotate(-1)
        # insert the marble according to the rules - between CW 1 and CCW 2
        else:
            circle.rotate(-1)
            circle.append(marble)
        if score:
            scores[marble % players] += score
    return scores


games = [(9, 25, 32),
         (10, 1618, 8317),
         (13, 7999, 146373),
         (17, 1104, 2764),
         (21, 6111, 54718),
         (30, 5807, 37305),
         (411, 72059, 429943),          # this is Puzzle 1
         (411, 72059*100, 3615691746)]  # this is Puzzle 2

for game in games:
    before = datetime.datetime.now()
    player_scores = play_marbles(game[0], game[1])
    high_score = max(player_scores)
    elapsed = datetime.datetime.now() - before
    success_string = " - success!" if game[2] and high_score == game[2] else ""
    print(f'For Game {game}, high score is {high_score}{success_string}, calculated in {elapsed}')
