# sprites.py
import pygame
from settings import *



def loadSpriteSheet(sheet, row, col, newSize, size):
  """ Creates a blank surface and loads and returns a portion of the spritesheet on to the surface. """
  image = pygame.Surface(size).convert_alpha()
  image.blit(sheet, (0, 0), (row * size[0], col * size[1], size[0], size[1]))
  image = pygame.transform.scale(image, newSize)
  image.set_colorkey('Black')
  return image

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

    image = pygame.Surface((960, 960))
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

    self.insertToken(grid, 1, 3, 3)
    self.insertToken(grid, -1, 3, 4)
    self.insertToken(grid, 1, 4, 4)
    self.insertToken(grid, -1, 4, 3)

    return grid
      # Create an array of characters from 'A' to GRID_SIZE (inclusive)
    

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


  def insertToken(self, grid, curplayer, y, x):
    tokenImage = white_token if curplayer == 1 else black_token
    self.tokens[(y, x)] = Token(curplayer, y, x, tokenImage, self.GAME)
    grid[y][x] = self.tokens[(y, x)].player



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