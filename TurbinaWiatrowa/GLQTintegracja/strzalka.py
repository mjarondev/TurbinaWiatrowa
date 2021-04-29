
from PyQt5 import QtGui
from PyQt5 import QtOpenGL

import OpenGL.GL as gl
from OpenGL import GLU
import pyrr
import numpy as np


import ObjLoader



class GLWidget(QtOpenGL.QGLWidget):
    def __init__(self, width, height, parent=None):
        self.parent = parent
        self.winWidth = width
        self.winHeight = height
        QtOpenGL.QGLWidget.__init__(self, parent)

    def initializeGL(self):
        self.qglClearColor(QtGui.QColor(0, 0, 45)) #init screen to RGB color

        self.angle = 0.0
        self.lastAngle = 0.0
        self.updateAngle = 0.0

        gl.glEnable(gl.GL_DEPTH_TEST) #enable depth testing (?)

        self.initGeometry()

    def resizeGL(self, width, height):
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        self.aspect = width/float(height)

        GLU.gluPerspective(45.0, self.aspect, 1.0, 100.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)


    def initGeometry(self):
        #wczytanie modelu

        self.strzalka = ObjLoader.LoadedObj("wiatrak/Arrow.obj",  "wiatrak/Arrow.vs", "wiatrak/Arrow.fs")

        self.strzalka.load_texture("wiatrak/a.jpg")


        self.view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, -15.0]))
        self.projection = pyrr.matrix44.create_perspective_projection_matrix(45.0, self.winWidth/self.winHeight, 0.1, 100.0)
        self.modelStrzalka = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0]))

        self.strzalka.useShader(self.view, self.projection, self.modelStrzalka)


    def setYawAngle(self, yawAngle):
        self.angle = yawAngle*np.pi/180

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        rot = pyrr.Matrix44.from_z_rotation(1 * self.angle)

        self.strzalka.useObject(rot, rot)



