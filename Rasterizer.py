
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
rend.glLoadBackground("texture/tornado.bmp")

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

#Aqui

# modelo3 = Model("OBJ/base.obj")
# modelo3.LoadTexture("texture/base.bmp")
# modelo3.vertexShader = vertexShader
# modelo3.fragmentShader = pixelationShader
# modelo3.translate[2] = -0.408
# modelo3.translate[1] = 0.04
# modelo3.translate[0] = -0.05
# modelo3.scale[0] = 0.002
# modelo3.scale[1] = 0.002
# modelo3.scale[2] = 0.002
# modelo3.rotate[1] = -50

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
# modelo4.rotate[1] = 70

#Aqui

#Tiburoncin
modelo5 = Model("OBJ/shark.obj")
modelo5.LoadTexture("texture/shark.bmp")
modelo5.vertexShader = vertexShader
modelo5.fragmentShader = dissolveShader
modelo5.translate[2] = -1.3
modelo5.translate[1] = 0.2
modelo5.translate[0] = -0.6
modelo5.scale[0] = 0.002
modelo5.scale[1] = 0.002
modelo5.scale[2] = 0.002
modelo5.rotate[1] = 150
modelo5.rotate[0] = 80
modelo5.rotate[2] = -30

#Banana
modelo6 = Model("OBJ/banan.obj")
modelo6.LoadTexture("texture/banan.bmp")
modelo6.vertexShader = vertexShader
modelo6.fragmentShader = hologramShader
modelo6.translate[2] = -0.1
modelo6.translate[1] = -0.03
modelo6.translate[0] = 0.01
modelo6.scale[0] = 0.025
modelo6.scale[1] = 0.025
modelo6.scale[2] = 0.025
modelo6.rotate[0] = 20
modelo6.rotate[1] = -140

#Shrek
modelo4 = Model("OBJ/Shrek.obj")
modelo4.LoadTexture("texture/sss.bmp")
modelo4.vertexShader = vertexShader
modelo4.fragmentShader = pixelationShader
modelo4.translate[2] = -0.7
modelo4.translate[1] = -0.15
modelo4.translate[0] = 0.5
modelo4.scale[0] = 0.025
modelo4.scale[1] = 0.025
modelo4.scale[2] = 0.025
modelo4.rotate[1] = -150

# Cangurocin uh ja ja
modelo3 = Model("OBJ/Kango.obj")
modelo3.LoadTexture("texture/kango.bmp")
modelo3.vertexShader = vertexShader
modelo3.fragmentShader = fireShader
modelo3.translate[2] = -0.9
modelo3.translate[1] = -0.18
modelo3.translate[0] = 0.3
modelo3.scale[0] = 0.0008
modelo3.scale[1] = 0.0008
modelo3.scale[2] = 0.0008
modelo3.rotate[2] = -90
modelo3.rotate[0] = -90

#BAse

modelo2 = Model("OBJ/base.obj")
modelo2.LoadTexture("texture/base.bmp")
modelo2.vertexShader = vertexShader
modelo2.fragmentShader = hologramShader
modelo2.translate[2] = -0.75
modelo2.translate[1] = -0.08
modelo2.translate[0] = 0.45
modelo2.scale[0] = 0.002
modelo2.scale[1] = 0.002
modelo2.scale[2] = 0.002
modelo2.rotate[1] = 105


#Barco
modelo7 = Model("OBJ/barc.obj")
modelo7.LoadTexture("texture/bar.bmp")
modelo7.vertexShader = vertexShader
modelo7.fragmentShader = wireframeShader
modelo7.translate[2] = -0.09
modelo7.translate[1] = 0.03
modelo7.translate[0] = 0.01
modelo7.scale[0] = 0.002
modelo7.scale[1] = 0.002
modelo7.scale[2] = 0.002
modelo7.rotate[0] = 30
modelo7.rotate[1] = 120
modelo7.rotate[2] = 30

modelo8 = Model("OBJ/shark.obj")
modelo8.LoadTexture("texture/shark.bmp")
modelo8.vertexShader = vertexShader
modelo8.fragmentShader = wireframeShader
modelo8.translate[2] = -1.6
modelo8.translate[1] = 0.5
modelo8.translate[0] = -1.3
modelo8.scale[0] = 0.002
modelo8.scale[1] = 0.002
modelo8.scale[2] = 0.002
modelo8.rotate[1] = 150
modelo8.rotate[0] = 0
modelo8.rotate[2] = -30



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

rend.models.append(modelo2)
rend.models.append(modelo3)
rend.models.append(modelo4)
rend.models.append(modelo5)
rend.models.append(modelo6)
rend.models.append(modelo7)
rend.models.append(modelo8)

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
				rend.glGenerateFrameBuffer("BMP/scene.bmp")
				
					
	rend.glClear()
	rend.glClearBackground()
	
	rend.glRender()
	#rend.glTriangle(puntoA, puntoB, puntoC)

	pygame.display.flip()
	clock.tick(60)
	
rend.glGenerateFrameBuffer("output.bmp")

pygame.quit()
