# Dessiner en utilisant paintEvent
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5.QtWidgets import *
class ZoneDessin(QtGui.QWidget) :
    def __init__(self,parent=None) :
        super().__init__(parent)
        self.listepoints=[]
 
    def mousePressEvent(self,e) :
        self.listepoints.append((e.x(),e.y()))
        self.repaint()
 
    def paintEvent(self,e) :
        p=QtGui.QPainter(self)
        p.setBrush(QtGui.QColor(255,0,0))
        for l in self.listepoints :
            p.drawEllipse(l[0],l[1],15,15)
 
class Fenetre(QtGui.QMainWindow):
    def __init__(self,parent=None) :
        super().__init__(parent)
        self.resize(420,420)
        self.setWindowTitle("Dessin painEvent")
        dessin=ZoneDessin(self)
        dessin.setGeometry(10,10,400,400)
 
app=QtGui.QApplication(sys.argv)
frame=Fenetre()
frame.show()
sys.exit(app.exec_())
