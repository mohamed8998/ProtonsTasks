
def manage_scoreboard(round):
  scoreboard = {}
  for player, score in round:
    scoreboard[player] = scoreboard.get(player, 0) + score
  return scoreboard

rounds = [(1, 10), (2, 15), (3, -5), (1, 20), (2, -10)]
final = manage_scoreboard(rounds)
print(final)