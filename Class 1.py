import pygame
import random
pygame.init()
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 600
window = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
pygame.display.set_caption("Platformer Game using Python")
player_height = 50
player_width = 50
player_x = 50
player_y = 50
player_speed = 5
platform_height = 30
platform_width = 100
list = []
# This is to make 5 platforms at random positions and insure they are within the screen and not outside
for i in range(5):
	platform_x = random.randint(0, WINDOW_WIDTH-platform_width)
	platform_y = random.randint(0, WINDOW_HEIGHT-platform_height)
	list.append(pygame.Rect(platform_x, platform_y, platform_width, platform_height))


running = True
clock = pygame.time.Clock()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Fill background with white (RGB 255,255,255)
	window.fill((255, 255, 255))

	pygame.display.update()
	clock.tick(60)

pygame.quit()