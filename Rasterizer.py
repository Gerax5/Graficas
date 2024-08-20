
import random
import pygame
from pygame.locals import *
from gl import *
from model import Model
from shaders import *

width = 960
height = 540

screen = pygame.display.set_mode((width, height), pygame.SCALED  )
clock = pygame.time.Clock()

rend = Render(screen)
rend.glLoadBackground("texture/OIPJ.bmp")

puntoA = [50, 50, 0]
puntoB = [250, 500, 0]
puntoC = [500, 50, 0]

# modelo2 = Model("OBJ/model.obj")
# modelo2.LoadTexture("texture/model.bmp")
# modelo2.vertexShader = vertexShader
# modelo2.fragmentShader = fireShader
# #modelo1.fragmentShader = dissolveShader
# #modelo1.fragmentShader = wireframeShader
# #modelo1.fragmentShader = fireShader
# #modelo1.fragmentShader = depthOfFieldShader
# # modelo1.fragmentShader = hologramShader
# modelo2.translate[2] = -5
# # modelo2.translate[2] = 0.03
# # modelo2.translate[1] = -0.15
# # modelo2.translate[0] = 0.2
# modelo2.scale[0] = 1.5
# modelo2.scale[1] = 1.5
# modelo2.scale[2] = 1.5


# modelo1 = Model("OBJ/Shrek.obj")
# modelo1.LoadTexture("texture/sss.bmp")
# modelo1.vertexShader = vertexShader
# #modelo1.fragmentShader = pixelationShader
# modelo1.fragmentShader = dissolveShader
# #modelo1.fragmentShader = hologramShader
# #modelo1.fragmentShader = wireframeShader
# #modelo1.fragmentShader = fireShader
# #modelo1.fragmentShader = depthOfFieldShader
# # modelo1.fragmentShader = hologramShader
# modelo1.translate[2] = -0.3
# modelo1.translate[1] = -0.15
# modelo1.translate[0] = -0.2
# modelo1.scale[0] = 0.025
# modelo1.scale[1] = 0.025
# modelo1.scale[2] = 0.025

modelo3 = Model("OBJ/Penguin.obj")
#modelo3 = Model("OBJ/Shrek.obj")
#modelo3.LoadTexture("texture/sss.bmp")
modelo3.LoadTexture("texture/Pen.bmp")
modelo3.vertexShader = vertexShader
modelo3.fragmentShader = gouradShader
modelo3.translate[2] = -0.3
modelo3.translate[1] = -0.15
modelo3.translate[0] = 0
modelo3.scale[0] = 0.025
modelo3.scale[1] = 0.025
modelo3.scale[2] = 0.025

# modelo4 = Model("OBJ/Shrek.obj")
# modelo4.LoadTexture("texture/sss.bmp")
# modelo4.vertexShader = vertexShader
# modelo4.fragmentShader = hologramShader
# modelo4.translate[2] = -0.4
# modelo4.translate[1] = -0.03
# modelo4.translate[0] = -0.12
# modelo4.scale[0] = 0.025
# modelo4.scale[1] = 0.025
# modelo4.scale[2] = 0.025

# modelo5 = Model("OBJ/Shrek.obj")
# modelo5.LoadTexture("texture/sss.bmp")
# modelo5.vertexShader = vertexShader
# #modelo5.fragmentShader = pixelationShader
# #modelo1.fragmentShader = dissolveShader
# #modelo1.fragmentShader = wireframeShader
# modelo5.fragmentShader = fireShader
# #modelo1.fragmentShader = depthOfFieldShader
# # modelo1.fragmentShader = hologramShader
# modelo5.translate[2] = -0.4
# modelo5.translate[1] = -0.03
# modelo5.translate[0] = 0.12
# modelo5.scale[0] = 0.025
# modelo5.scale[1] = 0.025
# modelo5.scale[2] = 0.025

# Modelo Wol
# modelo1 = Model("OBJ/wol.obj")
# modelo1.LoadTexture("texture/wol.bmp")

# modelo1.translate[2] = -0.3
# modelo1.translate[1] = -0.1
# modelo1.scale[0] = 0.1
# modelo1.scale[1] = 0.1
# modelo1.scale[2] = 0.1

#rend.models.append(modelo3)
# rend.models.append(modelo1)
# rend.models.append(modelo3)
# rend.models.append(modelo4)
# rend.models.append(modelo5)

isRunning = True
while isRunning:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				isRunning = False
				
			elif event.key == pygame.K_1:
				rend.primitiveType = POINTS
				
			elif event.key == pygame.K_2:
				rend.primitiveType = LINES
				
			elif event.key == pygame.K_3:
				rend.primitiveType = TRIANGLES
			elif event.key == pygame.K_RIGHT:
				rend.camera.translate[0] += 1
			elif event.key == pygame.K_LEFT:
				rend.camera.translate[0] -= 1
			elif event.key == pygame.K_UP:
				rend.camera.translate[1] += 1
			elif event.key == pygame.K_DOWN:
				rend.camera.translate[1] -= 1
			elif event.key == pygame.K_p:
				rend.glGenerateFrameBuffer("BMP/army.bmp")
				
					
	rend.glClear()
	rend.glClearBackground()
	
	rend.glRender()
	#rend.glTriangle(puntoA, puntoB, puntoC)

	pygame.display.flip()
	clock.tick(60)
	
rend.glGenerateFrameBuffer("output.bmp")

pygame.quit()
