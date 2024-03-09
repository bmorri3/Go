# TODO: Check for key errors when popping values

import pygame
import random
import copy

from sprites import *
from settings import *



class Pente():
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption(TITLE)

    self.player1 = 1
    self.player2 = -1

    self.tokens_taken_by_player1 = 0
    self.tokens_taken_by_player2 = 0

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


  def freeze_screen(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
          return


  def check_if_winner(self, grid, curPlayer, y, x):   
    in_a_row = self.grid.check_for_in_a_row(grid, curPlayer, y, x)

    if self.tokens_taken_by_player1 >= TOKENS_TO_WIN or (curPlayer == 1 and in_a_row):
      self.update()
      self.draw()
      print("PLAYER 1 WINS!")
      self.RUN = False
      self.end_screen()
      
    elif self.tokens_taken_by_player2 >= TOKENS_TO_WIN or (curPlayer == -1 and in_a_row):
      self.update()
      self.draw()
      print("PLAYER 2 WINS!")
      self.RUN = False
      self.end_screen()


  def input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit(0)

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 3:
          self.grid.printGameLogicBoard()

        if event.button == 1:
          x, y = pygame.mouse.get_pos()
          x, y = (x - TILESIZE) // TILESIZE, (y - TILESIZE) // TILESIZE

          if 0 <= x < NUM_ROWS_AND_COLS and 0 <= y < NUM_ROWS_AND_COLS and not self.grid.tokens.get((y,x)):
            self.grid.insert_token(self.grid.gridLogic, self.curPlayer, y, x)
            tokens_taken = self.grid.remove_tokens_if_taken(self.grid.gridLogic, y, x, self.curPlayer)
            if self.curPlayer == 1 and tokens_taken:
              self.tokens_taken_by_player1 += tokens_taken
              print("tokens_taken_by_player1:", self.tokens_taken_by_player1)
            elif self.curPlayer == -1 and tokens_taken:
              self.tokens_taken_by_player2 += tokens_taken
              print("tokens_taken_by_player2:", self.tokens_taken_by_player2)
             

            self.check_if_winner(self.grid.gridLogic, self.curPlayer, y, x)
                            
            # Move to new player
            self.curPlayer *= -1


  def update(self):
    pass


  def draw(self):
    self.screen.fill((0, 0, 0))
    self.grid.drawGrid(self.screen)
    pygame.display.update()


  def end_screen(self):
    # Wait until quit or mouse click
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
          return 



if __name__ == '__main__':
  
  while True:
    game = Pente()
    game.run()
    print("NEW GAME")
  