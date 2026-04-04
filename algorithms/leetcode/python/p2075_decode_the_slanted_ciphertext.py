class Solution:
  def decodeCiphertext(self, encodedText: str, rows: int) -> str:
    # column is len(str) / rows
    """
    3 by 4
    1,6,11...2,7,12...3,8,...4,9...

    4 by 6
    1,8,15,22...2,9,16,23...3,10,17,24,...4,11,18,...

    create str array
    start from i = 1 to rows
      from j = i to (rows * cols), skip (cols + 1).
      add str[j] to str array if not empty
    return "".join(array)
    """
    cells = len(encodedText)
    cols =  cells // rows
    res = []
    print(f"clles {cells} cols {cols} rows {rows}")
    for i in range(cols):
      for j in range(i, cells, cols + 1):
        res.append(encodedText[j])
    return "".join(res).rstrip()
