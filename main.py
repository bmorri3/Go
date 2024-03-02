import pygame
import random
import copy

from settings import *

class Othello():
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((1100, 800))
    pygame.display.set_caption('Othello')

    self.rows = GRID_SIZE
    self.cols = GRID_SIZE

    self.grid = Grid(self.rows, self.cols, (80, 80), self)

    self.RUN = True


  def run(self):
    while self.RUN == True:
      self.input()
      self.update()
      self.draw()


  def input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.RUN = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 3:
          print("right click")
          self.grid.printGameLogicBoard()

  def update(self):
    pass


  def draw(self):
    self.screen.fill((0, 0, 0))

    pygame.display.update()



class Grid:
  def __init__(self, rows, cols, size, main):
    self.GAME = main
    self.x = rows
    self.y = cols
    self.size = size

    self.gridLogic = self.regenGrid(self.x, self.y)


  def regenGrid(self, rows, cols):
    """ Generate an empty grid for terminal """
    grid = []
    for x in range(rows):
      line = []
      for y in range(cols):
        line.append(0)  
      grid.append(line)


    return grid
      # Create an array of characters from 'A' to GRID_SIZE (inclusive)
    

  def printGameLogicBoard(self):
    chars = [chr(i) for i in range(ord('A'), ord('A') + GRID_SIZE)]

    # Construct the column headers
    output_string = "  |"
    for char in chars:
      output_string += f" {char} |"

    print(output_string)

    # Construct each row
    for i, row in enumerate(self.gridLogic):
      line = f"{i} |".ljust(3, " ")
      for item in row:
        line += f"{item}".center(3, " ") + "|"
      print(line)

    print()

  

if __name__ == '__main__':
  game = Othello()
  game.run()
  pygame.quit()