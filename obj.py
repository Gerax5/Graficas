
class Obj(object):
    def __init__(self, filename):
        #Asumiendo que el archivo es un formato .obj
        with open(filename, "r") as file:
            lines = file.read().splitlines()

        self.vertices = []
        self.textcoords = []
        self.normals = []
        self.faces = []

        for line in lines:

            try:
                prefix, value = line.split(" ",1)
            except:
                continue

            # Dependiendo del prefijo, parseamos y guardamos
            # La informacion en el contenedor correcto

            if prefix == "v":
                self.vertices.append(list(map(float, value.split(" "))))
            elif prefix == "vt":
                self.textcoords.append(list(map(float, value.split(" "))))
            elif prefix == "vn":
                self.normals.append(list(map(float, value.split(" "))))
            elif prefix == "f":
                #
                 self.faces.append([
                        [int(x) if x else None for x in vert.split("/")]
                        for vert in line.strip().split()[1:]
                    ])
                
                # face = []
                # verts = value.split(" ")
                # for vert in verts:
                #     vert = list(map(int, vert.split("/")))
                #     face.append(vert)
                # self.faces.append(face)