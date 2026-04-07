from typing import List

class Robot:
  # N, W, S, E (counter clockwise)
  DX = [0, -1, 0, 1]
  DY = [1, 0, -1, 0]

  def __init__(self, width: int, height: int):
    self.width = width
    self.height = height
    self.x = 0
    self.y = 0
    self.direction = 3

  def step(self, num: int) -> None:
    perimeter = 2 * (self.width + self.height - 2)
    num %= perimeter

    if num == 0:
        num = perimeter
    for _ in range(num):
      next_x = self.x + Robot.DX[self.direction]
      next_y = self.y + Robot.DY[self.direction]

      while next_x >= self.width or next_x < 0 or next_y  >= self.height or next_y < 0:
        self.direction = (self.direction + 1) % 4
        next_x = self.x + Robot.DX[self.direction]
        next_y = self.y + Robot.DY[self.direction]

      self.x, self.y = next_x, next_y

  def getPos(self) -> List[int]:
    return [self.x, self.y]

  def getDir(self) -> str:
    return ["North", "West", "South", "East"][self.direction]



# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
