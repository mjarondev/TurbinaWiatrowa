
from PyQt5 import QtGui
from PyQt5 import QtOpenGL

import OpenGL.GL as gl
from OpenGL import GLU
import pyrr
import numpy as np

from math import sin, cos

import ObjLoader



class GLWidget(QtOpenGL.QGLWidget):
    def __init__(self, width, height, parent=None):
        self.parent = parent
        self.winWidth = width
        self.winHeight = height
        QtOpenGL.QGLWidget.__init__(self, parent)

    def initializeGL(self):
        self.qglClearColor(QtGui.QColor(0, 0, 45)) #init screen to RGB color
        self.OmegaX = 0.0
        self.OmegaY = 0.0
        self.OmegaPitch = 0
        self.OmegaYaw = 0

        self.pitchAdd = 0.0
        self.pitchAngle = 0.0
        self.lastPithcAngle = 0.0
        self.yawAngle = 0.0
        self.lastYawAngle = 0.0

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

        self.stojak = ObjLoader.LoadedObj("wiatrak/myStojak.obj", "wiatrak/stojakVert.vs", "wiatrak/stojakFrag.fs")
        self.chwytak = ObjLoader.LoadedObj("wiatrak/myChwytak.obj", "wiatrak/chwytVert.vs", "wiatrak/chwytFrag.fs")
        self.skrzydla = []
        for i in range(3):
            self.skrzydla.append(ObjLoader.LoadedObj("wiatrak/mySkrzydlo.obj", "wiatrak/skrzydloVert.vs", "wiatrak/skrzydloFrag.fs"))

        self.stojak.load_texture("wiatrak/a.jpg")
        self.chwytak.load_texture("wiatrak/a.jpg")
        for skrzydlo in self.skrzydla:
            skrzydlo.load_texture("wiatrak/a.jpg")

        #self.view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, -42.0, -75.0]))
        #self.view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, -60.0, -25.0])) #testowe rzut na nasele
        self.view = pyrr.matrix44.create_look_at([0.0, 60.0, 45.0], [0.0, 60.0, 0.0], [0.0, 1.0, 0.0])
        self.projection = pyrr.matrix44.create_perspective_projection_matrix(60.0, self.winWidth/self.winHeight, 0.1, 100.0)
        self.modelStojak = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0]))
        self.modelChwytak = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 60.0, 0.0]))
        self.modelSkrzydla = []
        for i in range(3):
            self.modelSkrzydla.append(pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 61.5, 0])))

        self.stojak.useShader(self.view, self.projection, self.modelStojak)
        self.chwytak.useShader(self.view, self.projection, self.modelChwytak)
        for i in range(3):
            self.skrzydla[i].useShader(self.view, self.projection, self.modelSkrzydla[i])

        self.OmegaY -= 1.57

    def setView(self, przod, obrot, wysokosc):
        self.view = pyrr.matrix44.create_look_at([przod*sin(obrot/100), wysokosc, przod*cos(obrot/100)], [0.0, wysokosc, 0.0], [0.0, 1.0, 0.0])

    def setRot(self, RPM, yawAngle, pitchAngle):
        RPS = RPM/60
        self.pitchAdd = (RPS/50)*2*3.14
        self.pitchAngle = pitchAngle
        self.yawAngle = yawAngle

    def updateRot(self):
        self.OmegaX += self.pitchAdd#0.02
        self.OmegaY += 0#0.02

        self.OmegaPitch -= (self.pitchAngle-self.lastPithcAngle)*np.pi/180
        self.OmegaYaw += (self.yawAngle-self.lastYawAngle)*np.pi/180

        self.lastPithcAngle = self.pitchAngle
        self.lastYawAngle = self.yawAngle

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        #miejsce na drawArrays (chyba petla)
        rotX = pyrr.Matrix44.from_x_rotation(1 * self.OmegaX)
        rotPitch = pyrr.Matrix44.from_y_rotation(1 * self.OmegaPitch)

        rotY = pyrr.Matrix44.from_y_rotation(1 * self.OmegaY)
        rotYaw = pyrr.Matrix44.from_y_rotation(1 * self.OmegaYaw)
        rotYawBlades = rotYaw * pyrr.Matrix44.from_translation([-2.5, 0.0, 0.0])

        self.stojak.useObject(rotY, rotY*self.view)
        self.chwytak.useObject(rotY * rotYaw, rotY*rotYaw*self.view)
        for i in range(3):
            rotX2 = pyrr.Matrix44.from_x_rotation(2 * i * np.pi / 3)
            self.skrzydla[i].useObject(rotY * rotYawBlades * rotX2 * rotX * rotPitch, rotY*rotYaw*self.view)

        self.stojak.useShader(self.view, self.projection, self.modelStojak)
        self.chwytak.useShader(self.view, self.projection, self.modelChwytak)
        for i in range(3):
            self.skrzydla[i].useShader(self.view, self.projection, self.modelSkrzydla[i])


