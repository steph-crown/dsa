class Solution:
  def judgeCircle(self, moves: str) -> bool:
    deltas = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    x, y = 0, 0
    for move in moves:
      dx, dy = deltas[move]
      x, y = x + dx, y + dy
    return x == 0 and y == 0
