import pygame
# initialize pygame
pygame.init()
clock = pygame.time.Clock()

# define width of screen
width = 1000
# define height of screen
height = 600
screen_res = (width, height)
fps = 30

pygame.display.set_caption("GFG Bouncing game")
screen = pygame.display.set_mode(screen_res)

# define colors
red = (255, 0, 0)
black = (0, 0, 0)

# define ball
# ball_obj = pygame.draw.circle(
# 	surface=screen, color=red, center=[100, 100], radius=10)
# define speed of ball
# speed = [X direction speed, Y direction speed]
position = [width/2, height/2]
speed = [0, 0]
size = 50

# game loop
while True:
	# event loop
	for event in pygame.event.get():
		# check if a user wants to exit the game or not
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				speed = [5,5]

	# fill black color on screen
	screen.fill(black)

	# move the ball
	# Let center of the ball is (100,100) and the speed is (1,1)
	# ball_obj = ball_obj.move(speed)
	# Now center of the ball is (101,101)
	# In this way our wall will move
	
	position[0] += speed[0]
	position[1] += speed[1]

	# if ball goes out of screen then change direction of movement
	# if ball_obj.left <= 0 or ball_obj.right >= width:
	# 	speed[0] = -speed[0]
	# if ball_obj.top <= 0 or ball_obj.bottom >= height:
	# 	speed[1] = -speed[1]
	
	if position[0]-size <= 0 or position[0]+size >= width:
		speed[0] = -speed[0]
		
	if position[1]-size <= 0 or position[1]+size >= height:
		speed[1] = -speed[1]
        
	# draw ball at new centers that are obtained after moving ball_obj
	pygame.draw.circle(screen, red, (int(position[0]), int(position[1])), size)

	# update screen
	pygame.display.flip()
	clock.tick(fps)
