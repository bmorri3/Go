import pygame
import random
import copy

from sprites import *
from settings import *



class Go():
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption(TITLE)

    self.player1 = 1
    self.player2 = -1

    self.curPlayer = 1

    self.rows = NUM_ROWS_AND_COLS
    self.cols = NUM_ROWS_AND_COLS

    self.grid = Grid(self.rows, self.cols, (TILESIZE, TILESIZE), self)

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

        if event.button == 1:
          x, y = pygame.mouse.get_pos()
          x, y = (x - TILESIZE) // TILESIZE, (y - TILESIZE) // TILESIZE
          self.grid.insertToken(self.grid.gridLogic, self.curPlayer, y, x)
          self.curPlayer *= -1

  def update(self):
    pass


  def draw(self):
    self.screen.fill((0, 0, 0))
    self.grid.drawGrid(self.screen)
    pygame.display.update()

  

if __name__ == '__main__':
  game = Go()
  game.run()
  pygame.quit()