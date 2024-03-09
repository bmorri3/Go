# sprites.py
import pygame
from settings import *


def directions(x, y):
  """ Check to determine which directions are valid from the current cell """
  minX = 0
  minY = 0
  maxX = NUM_ROWS_AND_COLS - 1
  maxY = NUM_ROWS_AND_COLS - 1
  valid_directions = []

  for dx in range(-1, 2):
    for dy in range(-1, 2):
      if dx == 0 and dy == 0:
        continue  # Skip the case where dx and dy are both 0
      new_x, new_y = x + dx, y + dy
      if minX <= new_x <= maxX and minY <= new_y <= maxY:
        valid_directions.append((new_x, new_y))

  return valid_directions
  

def loadSpriteSheet(sheet, row, col, newSize, size):
  """ Creates a blank surface and loads and returns a portion of the spritesheet on to the surface. """
  image = pygame.Surface(size).convert_alpha()
  image.blit(sheet, (0, 0), (row * size[0], col * size[1], size[0], size[1]))
  image = pygame.transform.scale(image, newSize)
  image.set_colorkey('Black')
  return image

def cellInRange(x, y):
  return 0 <= x < NUM_ROWS_AND_COLS and 0 <= y < NUM_ROWS_AND_COLS



class Grid:
  def __init__(self, rows, cols, size, main):   
    self.GAME = main
    self.x = rows
    self.y = cols
    self.size = size        
    self.bg = self.loadBackGroundImages()
    self.tokens = {}
    self.gridBg = self.createbgimg()
    self.gridLogic = self.regenGrid(self.x, self.y)


  def loadBackGroundImages(self):
    spriteSheet = pygame.image.load(os.path.join("assets", "wood.png")).convert_alpha()
    imgDict = {}
    for i in range(3):
      for j in range(7):
        imgDict[ALPHA[j] + str(i)] = loadSpriteSheet(spriteSheet, j, i, (self.size), (32, 32))
    return imgDict


  def createbgimg(self):
    num_rows = 10
    num_cols = 10

    gridBg = [
            ['C0', 'D0', 'D0', 'D0', 'D0', 'D0', 'D0', 'D0', 'D0', 'E0'],
            ['C1', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'E1'],
            ['C1', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'E1'],
            ['C1', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'E1'],
            ['C1', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'E1'],
            ['C1', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'E1'],
            ['C1', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'E1'],
            ['C1', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'E1'],
            ['C1', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'E1'],
            ['C2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'E2'],
    ]

    image = pygame.Surface((800, 800))
    for j, row in enumerate(gridBg):
      for i, img in enumerate(row):
        image.blit(self.bg[img], (i * self.size[0], j * self.size[1]))
    return image


  def regenGrid(self, rows, cols):
    """ Generate an empty grid for terminal """
    grid = []
    for x in range(rows):
      line = []
      for y in range(cols):
        line.append(0)  
      grid.append(line)

    return grid


  def drawGrid(self, window):
    window.blit(self.gridBg, (0, 0))

    for token in self.tokens.values():
      token.draw(window)


  def printGameLogicBoard(self):
    chars = [chr(i) for i in range(ord('A'), ord('A') + NUM_ROWS_AND_COLS)]

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


  def findValidCells(self, grid, curPlayer):
    """ Performs a check to find all empty cells that are adjacent to opposing player """
    validCellToClick = []
    for gridX, row in enumerate(grid):
      for gridY, col in enumerate(row):
        if grid[gridX][gridY] != 0:
          continue
        DIRECTIONS = directions(gridX, gridY)

        for direction in DIRECTIONS:
          dirX, dirY = direction
          checkedCell = grid[dirX][dirY]

          if checkedCell == 0 or checkedCell == curPlayer:
            continue

          if (gridX, gridY) in validCellToClick:
            continue
          
          validCellToClick.append((gridX, gridY))

    return validCellToClick


  def remove_tokens_if_taken(self, grid, y, x, curPlayer):

    tokens_taken = 0

    # Loop through all adjacent cells to current token   
    for dx in range(-1, 2):
      for dy in range(-1, 2):
        if dx == 0 and dy == 0:
          continue  # Skip the case where dx and dy are both 0
        
        # If the token is the opponent's
        new_x, new_y = x + dx, y + dy
        if cellInRange(new_x, new_y) and grid[new_y][new_x] == curPlayer * -1:

          # Check if the next token in the same direction is the opponent's
          new_x, new_y = new_x + dx, new_y + dy
          if cellInRange(new_x, new_y) and grid[new_y][new_x] == curPlayer * -1:            
            
            # Check if the third token in the same direction is the player's
            new_x, new_y = new_x + dx, new_y + dy
            if cellInRange(new_x, new_y) and grid[new_y][new_x] == curPlayer:
              
              # Remove the previous token              
              new_x, new_y = new_x - dx, new_y - dy
              self.tokens.pop((new_y, new_x))
              grid[new_y][new_x] = 0

              # Remove the token before the previous token              
              new_x, new_y = new_x - dx, new_y - dy
              self.tokens.pop((new_y, new_x))
              grid[new_y][new_x] = 0

              tokens_taken += 2

    return tokens_taken


  def insert_token(self, grid, curplayer, y, x):
    tokenImage = white_token if curplayer == 1 else black_token
    self.tokens[(y, x)] = Token(curplayer, y, x, tokenImage, self.GAME)
    grid[y][x] = self.tokens[(y, x)].player

  
  def check_for_in_a_row(self, grid, curPlayer, y, x):
         
    # Loop through all adjacent cells to current token   
    for dx in range(-1, 2):
      for dy in range(-1, 2):
        if dx == 0 and dy == 0:
          continue  # Skip the case where dx and dy are both 0
        
        in_a_row = 1
        new_x, new_y = x + dx, y + dy

        while in_a_row <= IN_A_ROW_TO_WIN:
          if cellInRange(new_x, new_y) and grid[new_y][new_x] == curPlayer:
            in_a_row += 1
            new_x += dx
            new_y += dy
          else:
            break

        if in_a_row >= IN_A_ROW_TO_WIN:
          return True
          
    return False


class Token:
    def __init__(self, player, gridX, gridY, image, main):
      self.player = player
      self.gridX = gridX
      self.gridY = gridY
      self.posX = TILESIZE + (gridY * TILESIZE)
      self.posY = TILESIZE + (gridX * TILESIZE)
      self.game = main
      self.image = image

    def transition(self):
      pass

    def draw(self, window):
      window.blit(self.image, (self.posX, self.posY))