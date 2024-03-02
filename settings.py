GRID_SIZE = 8

# Load and scale images
img = pygame.image.load(f"{path}").convert_alpha()
img = pygame.transform.scale(img, size)

white_token = pygame.transform.scale(pygame.image.load(os.path.join("assets", "WhiteToken.png")), (TILESIZE, TILESIZE))
black_token = pygame.transform.scale(pygame.image.load(os.path.join("assets", "BlackToken.png")), (TILESIZE, TILESIZE))
