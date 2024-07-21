import struct
def char(c):
    # 1
    return struct.pack("=c", c.encode("ascii"))

def word(w):
    #2
    return struct.pack("=h", w)

def dword(d):
    #4
    return struct.pack("=l",d)

POINTS = 0
LINES = 1
TRIANGLES = 2

class Render(object):
    def __init__(self, screen):
        self.screen = screen
        _, _, self.width, self.height = screen.get_rect()
        
        self.glColor(1,1,1)
        self.glClearColor(0,0,0)
        self.glClear()

        self.vertexShader=None

        self.primitiveTypes = LINES
        
        self.models =[]

    def glColor(self, r, g, b):
        r = min(1, max(0, r))
        g = min(1, max(0, g))
        b = min(1, max(0, b))

        self.currColor = [ r, g, b]

    def glClearColor(self, r, g, b):
        r = min(1, max(0, r))
        g = min(1, max(0, g))
        b = min(1, max(0, b))

        self.clearColor = [r,g,b]

    def glClear(self):
        color = [int(i * 255) for i in self.clearColor]
        self.screen.fill(color)

        self.frameBuffer = [[self.clearColor for y in range(self.height)] for x in range(self.width)]

    def glPoint(self, x, y, color = None):
        # Pygame empieza a renderizar desde la esquina 
        # superior izquierda. Hay que volter el valor y

        if (0<=x<self.width) and (0 <= y <self.height):
            # Pygame recibe los colores en un rango de 0 a 255
            color = [int(i * 255) for i in (color or self.currColor)]
            self.screen.set_at((x, self.height - 1 - y), color)
            self.frameBuffer[x][y] = color

    def glLine(self, vo,  v1, color = None):
        # y = mx + b
        xo = int(vo[0])
        x1 = int(v1[0])
        yo = int(vo[1])
        y1 = int(v1[1])

        # Algoritmo de Lineas de Bresenham

        #Si el punto 0 es igual punto 1, solo se dibuja un punto
        if xo == x1 and yo == y1:
            self.glPoint(xo,yo)
            return
        
        dy = abs(y1 - yo)
        dx = abs(x1 - xo) 

        steep = dy > dx

        if steep:
            xo, yo = yo, xo
            x1, y1 = y1, x1
        
        if xo > x1:
            xo, x1 = x1, xo
            yo, y1 = y1, yo

        dy = abs(y1 - yo)
        dx = abs(x1 - xo) 

        offset = 0
        limit = 0.75
        m = dy / dx
        y = yo

        for x in range(xo, x1 + 1):

            if steep:
                self.glPoint(y, x, color or self.currColor)
            else:
                self.glPoint(x, y, color or self.currColor)

            offset += m

            if offset >= limit:
                if yo < y1:
                    y += 1
                else:
                    y -= 1
                limit += 1

    def glGenerateFrameBuffer(self, filename):
	
        with open(filename, "wb") as file:
            # Header
            file.write(char("B"))
            file.write(char("M"))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))
            
            # Info Header
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            
            # Color table
            for y in range(self.height):
                for x in range(self.width):
                    color = self.frameBuffer[x][y]
                    color = bytes([color[2],
                                color[1],
                                color[0]])
                    
                    file.write(color)

    def centerPolygon(self, coords):
        #Suponiendo que es cerrado
        #Formula: (1/6A) (xi + xi+1)(xiyi+1 - xi+1yi)
        coords.append(coords[0])
        a = 0
        cx = 0
        cy = 0

        for i in range(len(coords) - 1):
            x0, y0 = coords[i]
            x1, y1 = coords[i + 1]
            
            temp = x0 * y1 - x1 * y0
            
            a += temp
            cx += (x0 + x1) * temp
            cy += (y0 + y1) * temp

        a *= 0.5
        cx //= (6 * a)
        cy //= (6 * a)

        return int(cx), int(cy)

    def boundaryfill(self, x, y, fillColor = None, boundaryColor = None):
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if (0 <= x < self.width) and (0 <= y < self.height):
                color = [int(i * 255) for i in (boundaryColor or self.currColor)]
                if self.frameBuffer[x][y] == color:
                    continue
                self.glPoint(x, y, fillColor)
                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))

        #Alcanzo los limites de recursividad jajaja
        #self.boundaryfill(x + 1, y, fillColor, boundaryColor)
        #self.boundaryfill(x - 1, y, fillColor, boundaryColor)
        #self.boundaryfill(x, y + 1, fillColor, boundaryColor)
        #self.boundaryfill(x, y - 1, fillColor, boundaryColor)

    def glRender(self):
        
        for model in self.models: 
            #por cada modelo en la list, los dibujo
            # agarrar su matriz modelo 
            mMat  = model.GetModelMatrix()

            vertexBuffer = []
            #en el modelo hay que agarrar las caras y los vertices
            #por cada cara del modelo
            for face in model.faces: 
                # revisamos cuntos vertices tiene la cara
                #cuatro vertices, hay que crear un segundo triangulo
                vertCount = len(face)
                #obtenemos los vertices de la cara actual 
                v0 = model.vertices[face[0][0] - 1] #-1 porque en el obj los indices empiezan en 1
                v1 = model.vertices[face[1][0] - 1]
                v2 = model.vertices[face[2][0] - 1]
                
                if vertCount == 4:
                    v3 = model.vertices[face[3][0]-1]

                if self.vertexShader:
                    v0 = self.vertexShader(v0, modelMatrix = mMat)
                    v1 = self.vertexShader(v1, modelMatrix = mMat)
                    v2 = self.vertexShader(v2, modelMatrix = mMat)
                    if vertCount==4:
                        v3 = self.vertexShader(v3, modelMatrix = mMat)
                
                #dibujar la cara
                #self.glPoint(int(v0[0]),int(v0[1])) #x,y
                #self.glPoint(int(v1[0]),int(v1[1]))
                #self.glPoint(int(v2[0]),int(v2[1]))
                #if vertCount == 4:
                #    self.glPoint(int(v3[0]),int(v3[1]))
                    
                # self.glLine((v0[0],v0[1]), (v1[0],v1[1]))
                # self.glLine((v1[0],v1[1]), (v2[0],v2[1]))
                # self.glLine((v2[0],v2[1]), (v0[0],v0[1]))
                # if vertCount == 4: 
                #     self.glLine((v0[0],v0[1]), (v2[0],v2[1]))
                #     self.glLine((v2[0],v2[1]), (v3[0],v3[1]))
                #     self.glLine((v3[0], v3[1]), (v0[0],v0[1]))
                
                vertexBuffer.append(v0)
                vertexBuffer.append(v1)
                vertexBuffer.append(v2)

                if vertCount == 4:
                    vertexBuffer.append(v0)
                    vertexBuffer.append(v2)
                    vertexBuffer.append(v3)

            self.glDrawPRimitives(vertexBuffer)

                #     vertexBuffer.append(v0)
                #     vertexBuffer.append(v1)
                #     vertexBuffer.append(v2)
                #     if vertCount == 4:
                #         vertexBuffer.append(v3)


    def glDrawPRimitives(self, buffer):

        if self.primitiveTypes == POINTS:
            for point in buffer:
                self.glPoint(int(point[0]), int(point[1]))
        elif self.primitiveTypes == LINES:
            for i in range(0, len(buffer), 3):
                p0 = buffer[i]
                p1 = buffer[i + 1]
                p2 = buffer[i + 2]

                self.glLine((p0[0], p0[1]), (p1[0], p1[1]) )
                self.glLine((p1[0], p1[1]), (p2[0], p2[1]) )
                self.glLine((p2[0], p2[1]), (p0[0], p0[1]) )
    


        
        