

import numpy as np
from OpenGL.GL import *
import OpenGL.GL.shaders
from PIL import Image
import pyassimp as pa

class LoadedObj:

    def __init__(self, filePath, vertShaderPath, fragShaderPath):
        super().__init__()
        self.loadObject(filePath)
        self.makeObject(vertShaderPath, fragShaderPath)

    #object
    def loadObject(self, filePath):
        """Load object. One per file(first)."""
        scene = pa.load(filePath)
        self.obj = scene.meshes[0]


        # vector for vertices, textures and normals
        self.model = np.concatenate((self.obj.vertices, self.obj.texturecoords[0], self.obj.normals), axis=0)
        self.textureOffset = self.model.itemsize * (len(self.model) // 3) * 3
        self.normalsOffset = self.model.itemsize * (len(self.model) // 3) * 2 * 3


    def makeObject(self, vertShaderPath, fragShaderPath):
        """Make and send buffer to GPU. Needs compiled shader and loaded object."""

        self.compileShader(vertShaderPath, fragShaderPath)

        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)

        # VBO(vertex array buffer) tablica ze wspolrzednymi wierzcholkow, wektorow normalnych itp wyslana do gpu
        # renderowanie polega na uzywaniu numerow wyslanych tablic
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, self.model.nbytes, self.model, GL_STATIC_DRAW)

        #shaders
        #position
        position = glGetAttribLocation(self.shader, "position")
        glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, self.model.itemsize*3, ctypes.c_void_p(0))
        glEnableVertexAttribArray(position)

        #texture
        textureCoords = glGetAttribLocation(self.shader, "texCoords")
        glVertexAttribPointer(textureCoords, 3, GL_FLOAT, GL_FALSE, self.model.itemsize*3, ctypes.c_void_p(self.textureOffset))
        glEnableVertexAttribArray(textureCoords)

        #normals
        normals = glGetAttribLocation(self.shader, "vertNormals")
        glVertexAttribPointer(normals, 3, GL_FLOAT, GL_FALSE, self.model.itemsize * 3, ctypes.c_void_p(self.normalsOffset))
        glEnableVertexAttribArray(normals)

        glBindVertexArray(0)

    def useObject(self, objRotation, lightRotation):
        glBindVertexArray(self.VAO)
        glUseProgram(self.shader)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glUniformMatrix4fv(self.rotateLoc, 1, GL_FALSE, objRotation)
        glUniformMatrix4fv(self.lightLoc, 1, GL_FALSE, lightRotation)
        glDrawArrays(GL_TRIANGLES, 0, len(self.obj.vertices))
        glUseProgram(0)
        glBindVertexArray(0)

    #shaders
    def loadShader(self, shaderFile):
        shaderSource = ""
        with open(shaderFile) as f:
            shaderSource = f.read()
        f.close()

        return str.encode(shaderSource)

    def compileShader(self, vs, fs):
        vertexShader = self.loadShader(vs)
        fragmentShader = self.loadShader(fs)

        self.shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertexShader, GL_VERTEX_SHADER),
                                                  OpenGL.GL.shaders.compileShader(fragmentShader, GL_FRAGMENT_SHADER))

    def useShader(self, globalView, globalProjection, globalModel):
        glUseProgram(self.shader)
        self.viewLoc = glGetUniformLocation(self.shader, "view")
        self.projectionLoc = glGetUniformLocation(self.shader, "projection")
        self.modelLoc = glGetUniformLocation(self.shader, "model")
        self.rotateLoc = glGetUniformLocation(self.shader, "rotate")
        self.lightLoc = glGetUniformLocation(self.shader, "light")

        glUniformMatrix4fv(self.viewLoc, 1, GL_FALSE, globalView)
        glUniformMatrix4fv(self.projectionLoc, 1, GL_FALSE, globalProjection)
        glUniformMatrix4fv(self.modelLoc, 1, GL_FALSE, globalModel)
        glUseProgram(0)

    #textures
    def load_texture(self, path):
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        # Set the texture wrapping parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        # Set texture filtering parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        # load image
        image = Image.open(path)
        img_data = np.array(list(image.getdata()), np.uint8)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

