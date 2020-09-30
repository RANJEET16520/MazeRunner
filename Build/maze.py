import pygame
import sys

TotalN = int(input("Enter the size of Grid (NxN):"))
sol = [[0 for i in range(TotalN)] for j in range(TotalN)]

def ratMovement(sol,n):
	pointImage = pygame.image.load("point1.jpg")

	pygame.init()
	gridSize = pygame.display.set_mode((32*n, 32*n))
	pygame.display.set_caption("Grid")
	gridImage = pygame.image.load("chess.png")
	index = 0

	font = pygame.font.SysFont("Ubuntu",16)
	text = []
	surface =[]
	white = (255, 255, 255)

	while True:
		gridSize.blit(gridImage,(0,0))
		if index < len(sol):
			gridImage.blit(pointImage,(sol[index][0]*32, sol[index][1]*32))
			text.append(font.render(str(index+1),True, white ))
			surface.append(text[index].get_rect())
			surface[index].center = (sol[index][0]*32+16, sol[index][1]*32+16)
			index+=1
		else:
			gridImage.blit(pointImage,(sol[index-1][0]*32, sol[index-1][1]*32))

		for x in range(10000000):
			pass
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == 27:
					pygame.quit()
					sys.exit()

		for i in range(index):
			gridImage.blit(text[i],surface[i])

		pygame.display.update()


def travel(MazeMatrix, x, y, n):
	if ((x>=0 and x<n) and (y>=0 and y<n) and(MazeMatrix[x][y] == 1)):
		return True
	return False

def startTracking(MazeMatrix, x, y, n):
	if (x == n-1 and y == n-1):
		if MazeMatrix[x][y] == 1:
			sol[x][y]=1
			return True
		return False

	if travel(MazeMatrix, x, y, n) == True:
		sol[x][y]=1
		if startTracking(MazeMatrix, x+1, y, n) == True:
			return True
		if startTracking(MazeMatrix, x, y+1, n) == True:
			return True
		return False

n = TotalN
# setting the element
print("Enter the element in 0||1\n0: Block is occupied\n1: Block is free")
MazeMatrix = [[0 for i in range(n)] for j in range(n)]
print(MazeMatrix)
# getting the input
for i in range(n):
	MazeMatrix[i] = [int(j) for j in input().split()]
print(MazeMatrix)

check = startTracking(MazeMatrix, 0, 0, n)

print(sol)
if check:
	print(sol)
else:
	print('There is no solution')
newMatxix = []
# ratMovement(sol,n)

for i in range(n):
	for j in range(n):
		if sol[i][j] == 1:
			newMatxix.append([j,i])

print(newMatxix)
ratMovement(newMatxix,n)