import math
import random
import noise
import os
import getch

X = int(input("Enter the size of grid > "))


gridPlayer = [5, 5]

wall = "🟧"
octaves = 1
freq = 7.0 / octaves

while True:
  grid = [['⬛' for x in range(X)] for y in range(X)]
  for x in range(len(grid)):
    for y in range(len(grid[0])):
      if x == gridPlayer[0] and y == gridPlayer[1]:
        grid[x][y] = "🧍"
      elif noise.snoise2(x / freq, y / freq, octaves) > 0.8:
        grid[x][y] = "🟩" 
      elif noise.snoise2(x / freq, y / freq, octaves) > 0:
        grid[x][y] = wall
      else:
        grid[x][y] = "⬛"

  os.system("clear")
  for s in grid:
    print(*s)

  print("Press either: 'w', 's', 'a' or 'd' to move")
  if grid[gridPlayer[0]][gridPlayer[1]] == "🟩":
    print("Treasure :")
  while True:
    move = getch.getch()
    try:
      if move == 'w':
        if grid[gridPlayer[0] - 1][gridPlayer[1]] == "⬛":
          continue
        gridPlayer[0] = gridPlayer[0] - 1
        break
      if move == 's':
        if grid[gridPlayer[0] + 1][gridPlayer[1]] == "⬛":
          continue
        gridPlayer[0] = gridPlayer[0] + 1
        break
      if move == 'a':
        if grid[gridPlayer[0]][gridPlayer[1] - 1] == "⬛":
          continue
        gridPlayer[1] = gridPlayer[1] - 1
        break
      if move == 'd':
        if grid[gridPlayer[0]][gridPlayer[1] + 1] == "⬛":
          continue
        gridPlayer[1] = gridPlayer[1] + 1
        break
    except IndexError:
      continue