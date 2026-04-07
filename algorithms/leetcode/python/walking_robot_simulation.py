from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        obstacle_set = set(map(tuple, obstacles))

        x = 0
        y = 0
        direction = 0
        max_dist_sq = 0

        for cmd in commands:
            if cmd == -2:
                direction = (direction - 1) % 4
            elif cmd == -1:
                direction = (direction + 1) % 4
            else:
                for _ in range(cmd):
                    next_x = x + dx[direction]
                    next_y = y + dy[direction]

                    if (next_x, next_y) in obstacle_set:
                        break

                    x = next_x
                    y = next_y

                    dist_sq = x * x + y * y
                    max_dist_sq = max(max_dist_sq, dist_sq)

        return max_dist_sq
