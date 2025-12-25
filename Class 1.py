import pygame #Importing libraries needed
import random
pygame.init()
# Making the window or display for the game
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Platformer Game using Python")
# Creating the dimensions for the player and platforms
player_height = 50
player_width = 50
player_x = 50
player_y = 50
player_speed = 5
platform_height = 30
platform_width = 100
list = []
ORANGE = (255, 165, 0)
BLACK = (0,0,0)
BLUE = (0,0,255)
# This is to make 5 platforms at random positions and insure they are within the screen and not outside
for i in range(5):
	platform_x = random.randint(0, WINDOW_WIDTH-platform_width)
	platform_y = random.randint(0, WINDOW_HEIGHT-platform_height)
	list.append(pygame.Rect(platform_x, platform_y, platform_width, platform_height))

# This is to run the game forever until the user clicks the red exit button
clock = pygame.time.Clock()
game_running = True
while game_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_running = False	
	keys = pygame.key.get_pressed() #These are the player controls
	if keys[pygame.K_LEFT]:
		player_x -= player_speed
	if keys[pygame.K_RIGHT]:
		player_x += player_speed
	if keys[pygame.K_UP]:
		player_y -= player_speed

	# This is so that the player has gravity and will slowly fall if not on a platform
	player_y += 1

	if player_y > WINDOW_HEIGHT:
		game_running = False 
	window.fill(BLACK)
		#The player will not be drawn onto the screen until this command is written
	player = pygame.draw.rect(window, ORANGE, (player_x, player_y, player_width, player_height))
	for platform in list: # Draw platforms and check collision for each one
		pygame.draw.rect(window, BLUE, platform)
		if player.colliderect(platform):
			player_y = platform.top - player_height
			break
	pygame.display.update() # This is so that when the player moves the screen updates to show the player moving every 60 frame
	clock.tick(60)
	





